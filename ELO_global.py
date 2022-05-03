import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import sys

def update_ratings(player_rating, question_rating, p_win, k_value):
    """
    :param playerA_rating: Current rating of player A
    :param playerB_rating: Current rating of player B

    :param k_value: The value that determines how much a rating should change
    :param perturbation: Float between 0-1 which fluctuates that actual score
    :return:
    """
    # -------- Predicted outcome --------
    # Predicted ratings
    p1_rat = player_rating
    p2_rat = question_rating

    # Define q1 and q2 for simplification of the calculation for expected score
    q1 = 10**(p1_rat / 400)
    q2 = 10**(p2_rat / 400)

    # Expected for each player respectively
    exp_1 = q1 / (q1 + q2)
    exp_2 = q2 / (q1 + q2)

    # -------- Actual outcome --------
    # Calculate the actual score from the outcome of the match (in our case completion of integrals)

    if p_win > 1:
        p_win = 0.99

    outcome = random.choices([0,1], weights = (1-p_win, p_win), k = 1)[0]
    # Calculate the new player ratings
    new_p1_rat = p1_rat + k_value * (outcome - exp_1)
    new_p2_rat = p2_rat + k_value * (1 - outcome - exp_2)

    return new_p1_rat, new_p2_rat, outcome


def simulate_elo(games, learning_rate = 0.1):
    """
    :param games: Number of games for each player to play
    :param perturbation: The randomness for each game played
    :return:
    """
    # The predicted elo ratings of the students
    starting_rating = 500
    student_rating = {'student1': starting_rating, 'student2': starting_rating,
    'student2': starting_rating, 'student3': starting_rating, 'student4': starting_rating,
    'student5': starting_rating, 'student6': starting_rating, 'student7': starting_rating,
    'student8': starting_rating, 'student9': starting_rating, 'student10': starting_rating}

    # Elo ratings for questions

    groups = [['Blueprint 1.1','Blueprint 1.2','Blueprint 1.3'],
    ['Blueprint 7.1','Blueprint 7.2','Blueprint 7.3',
    'Blueprint 7.4'], ['Blueprint 10.1', 'Blueprint 10.2',
    'Blueprint 10.3'], ['Blueprint 11.1', 'Blueprint 11.2','Blueprint 11.3',
    'Blueprint 11.4', 'Blueprint 11.5']]

    question_ratings = {'Blueprint 1.1':50, 'Blueprint 1.2':100, 'Blueprint 1.3':150,
    'Blueprint 2':150,'Blueprint 3':200,'Blueprint 4':250,'Blueprint 5': 300,
    'Blueprint 6':350,'Blueprint 7.1':400,'Blueprint 7.2':450,'Blueprint 7.3':500,
    'Blueprint 7.4':550,'Blueprint 8':600,'Blueprint 9':650,'Blueprint 10.1':700,
    'Blueprint 10.2':750, 'Blueprint 10.3':800,'Blueprint 11.1':850,
    'Blueprint 11.2':900,'Blueprint 11.3':950,'Blueprint 11.4':1000, 'Blueprint 11.5':1050,
    'Blueprint 12':1100,'Blueprint 13':1150, 'Blueprint 14':1200, 'Blueprint 15':1350,
    'Blueprint 16':1400, 'Blueprint 17':1500}

    question_probability = {'Blueprint 1.1': 0.9 , 'Blueprint 1.2': 0.85, 'Blueprint 1.3': 0.82,
    'Blueprint 2': 0.8, 'Blueprint 3': 0.75, 'Blueprint 4': 0.72,
    'Blueprint 5': 0.65, 'Blueprint 6': 0.68, 'Blueprint 7.1': 0.65,
    'Blueprint 7.2': 0.62, 'Blueprint 7.3': 0.6, 'Blueprint 7.4': 0.56,
    'Blueprint 8': 0.52, 'Blueprint 9': 0.5, 'Blueprint 10.1': 0.45,
    'Blueprint 10.2': 0.54, 'Blueprint 10.3': 0.52, 'Blueprint 11.1': 0.5,
    'Blueprint 11.2': 0.475, 'Blueprint 11.3': 0.45, 'Blueprint 11.4': 0.25,
    'Blueprint 11.5': 0.225, 'Blueprint 12': 0.2, 'Blueprint 13': 0.175,
    'Blueprint 14': 0.15, 'Blueprint 15': 0.05, 'Blueprint 16': 0.08,
    'Blueprint 17': 0.05}

    # List of keys for dictionaries
    student_keys = list(student_rating.keys())
    question_keys = list(question_ratings.keys())

    # Set up a list for data
    player_data = np.empty(games)
    player_data[:, 0] = starting_rating

    # question_data = [0]*games
    question_data = np.zeros(shape = (games, len(question_ratings)))
    question_data[0] = list(question_ratings.values())

    for i in range(1, games):
        if i < 100:  # k value varies depending on the number of games played
            k = 32
        elif 100 <= i < 500:
            k = 32
        else:
            k = 10

        # Initialise the player rating
        # player = student_keys[0]
        for student in student_keys:
            player_rating = student_rating[student]

            sample_list = list(question_keys)  # Create a list to sample from without replacement

            # Use normal distribution of player rating to select a number, and then
            # choose question with closest score to that number
            varied_value = np.random.normal(loc = player_rating, scale = 200)

            # Selects question from question bank with ELO score closest to value
            # selected from distribution

            question, question_rating = min(question_ratings.items(), key = lambda x: abs(varied_value - x[1]))
            p_win = question_probability[question]

            # Calculate new ratings and assign the new values into the dictionary
            new_ratings = update_ratings(player_rating, question_rating, p_win, k)
            student_rating['student'], question_ratings[question], outcome = new_ratings

            # Fill in the new data point for the ratings of each player
            player_data[i] = student_rating['student']
            question_data[i] = list(question_ratings.values())

    # Plot data
    plt.plot(player_data, 'k')#, linewidth = 2)
    plt.plot(question_data)#, linewidth = 2)
    plt.legend(['Player'], loc = 1)
    # plt.title('Example student ELO graph')
    plt.xlabel('Number of questions answered')
    plt.ylabel('Elo score')
    print(player_data)
    plt.show()
    # plt.savefig('with_learning.svg', bbox_inches='tight')

simulate_elo(200, learning_rate = 0.01)
