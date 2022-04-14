import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


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

    # Define student elo ratings
    # The real elo ratings of the students
    # act_student_ratings = {'student1': 300, 'student2': 500, 'student3': 700, 'student4': 800, 'student5': 900, 'student6': 1100,
    #                        'student7': 1200, 'student8': 1300, 'student9': 1500, 'student10': 1700}

    # The predicted elo ratings of the students
    starting_rating = 0
    student_rating = {'student': starting_rating}

    # Elo ratings for questions
    question_ratings = {'question1': 300 , 'question2': 500, 'question3': 700, 'question4': 800, 'question5': 900, 'question6': 1100,
                        'question7': 1200, 'question8': 1300, 'question9': 1500, 'question10': 1700}

    question_probability = {'question1': 0.6 , 'question2': 0.2, 'question3': 0.3, 'question4': 0.6, 'question5': 0.4, 'question6': 0.2,
                        'question7': 0.5, 'question8': 0.1, 'question9': 0.05, 'question10': 0.01}

    # List of keys for dictionaries
    student_keys = list(student_rating.keys())
    question_keys = list(question_ratings.keys())

    # Set up a list for data
    player_data = [0]*games
    player_data[0] = starting_rating

    # question_data = [0]*games
    question_data = np.zeros(shape = (games, len(question_ratings)))
    question_data[0] = list(question_ratings.values())

    for i in range(1, games):
        if i < 100:  # k value varies depending on the number of games played
            k = 32
        elif 100 <= i < 500:
            k = 16
        else:
            k = 10
        # Initialise the player rating
        player = student_keys[0]
        player_rating = student_rating[player]

        sample_list = list(question_keys)  # Create a list to sample from without replacement

        # Use normal distribution of player rating to select a number, and then
        # choose question with closest score to that number
        varied_value = np.random.normal(loc = player_rating, scale = 200)
        # scale decreases with number of games played by 1 every time
        question, question_rating = min(question_ratings.items(), key=lambda x: abs(varied_value - x[1]))
        p_win = question_probability[question]

        # Calculate new ratings and assign the new values into the dictionary
        new_ratings = update_ratings(player_rating, question_rating, p_win, k)
        student_rating['student'], question_ratings[question], outcome = new_ratings

        # Fill in the new data point for the ratings of each player
        player_data[i] = student_rating['student']
        question_data[i] = list(question_ratings.values())

        if outcome == 1:
            question_probability[question] += learning_rate
        else:
            question_probability[question] += learning_rate/2

    # Plot data
    plt.plot(player_data)
    plt.plot(question_data)
    plt.show()


simulate_elo(10)
