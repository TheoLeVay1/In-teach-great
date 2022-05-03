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
    'student5': starting_rating}#, 'student6': starting_rating, 'student7': starting_rating,
    # 'student8': starting_rating, 'student9': starting_rating, 'student10': starting_rating}

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

    question_probability = {'Blueprint 1.1': 0.95 , 'Blueprint 1.2': 0.9, 'Blueprint 1.3': 0.85,
    'Blueprint 2': 0.825, 'Blueprint 3': 0.8, 'Blueprint 4': 0.775,
    'Blueprint 5': 0.75, 'Blueprint 6': 0.72, 'Blueprint 7.1': 0.7,
    'Blueprint 7.2': 0.65, 'Blueprint 7.3': 0.6, 'Blueprint 7.4': 0.82,
    'Blueprint 8': 0.8, 'Blueprint 9': 0.78, 'Blueprint 10.1': 0.76,
    'Blueprint 10.2': 0.74, 'Blueprint 10.3': 0.72, 'Blueprint 11.1': 0.7,
    'Blueprint 11.2': 0.69, 'Blueprint 11.3': 0.675, 'Blueprint 11.4': 0.65,
    'Blueprint 11.5': 0.625, 'Blueprint 12': 0.6, 'Blueprint 13': 0.58,
    'Blueprint 14': 0.575, 'Blueprint 15': 0.55, 'Blueprint 16': 0.525,
    'Blueprint 17': 0.5}

    # List of keys for dictionaries
    student_keys = list(student_rating.keys())
    question_keys = list(question_ratings.keys())

    # Set up a list for data
    player_data = np.empty([len(student_keys), games])
    player_data[:, 0] = starting_rating

    # question_data = [0]*games
    question_data = np.empty([len(question_keys), games])
    question_data[:, 0] = list(question_ratings.values())

    for i in range(1, games):
        if i < 50:
            scale = 500
        if 50 < i < 100:
            scale = 250
        if i < 100:  # k value varies depending on the number of games played
            k = 32
        elif 100 <= i < 500:
            k = 16
            scale = 200
        else:
            k = 10
            scale = 100

        # Initialise the player rating
        # player = student_keys[0]
        for student in student_keys:
            player_rating = student_rating[student]
            idx = student_keys.index(student)

            sample_list = list(question_keys)  # Create a list to sample from without replacement

            # Use normal distribution of player rating to select a number, and then
            # choose question with closest score to that number
            varied_value = np.random.normal(loc = player_rating, scale = scale)

            # Selects question from question bank with ELO score closest to value
            # selected from distribution

            question, question_rating = min(question_ratings.items(), key = lambda x: abs(varied_value - x[1]))

            # Require varying abilities --> linspace between different ranges by students

            p_win = question_probability[question] - 0.1 * idx

            # Calculate new ratings and assign the new values into the dictionary
            new_ratings = update_ratings(player_rating, question_rating, p_win, k)
            student_rating[student], question_ratings[question], outcome = new_ratings

            # Fill in the new data point for the ratings of each player
        player_data[:, i] = list(student_rating.values())
        question_data[:, i] = list(question_ratings.values())
    # print(question_data)

    # Plot data
    plt.figure()
    for i in range(player_data.shape[0]):
        plt.plot(player_data[i], 'k', linewidth = 1)
    for i in range(question_data.shape[0]):
        plt.plot(question_data[i], linewidth = 0.5)

    plt.xlabel('Number of questions answered')
    plt.ylabel('Elo score')

    plt.show()

simulate_elo(500, learning_rate = 0.01)
