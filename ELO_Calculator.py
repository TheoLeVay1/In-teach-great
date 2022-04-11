import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


def update_ratings(playerA_rating, playerB_rating, playerA_act_rating, playerB_act_rating, k_value, perturbation):
    """
    :param playerA_rating: Current rating of player A
    :param playerB_rating: Current rating of player B
    :param playerA_act_rating: True rating of player A
    :param playerB_act_rating: True rating of player B
    :param k_value: The value that determines how much a rating should change
    :param perturbation: Float between 0-1 which fluctuates that actual score
    :return:
    """
    # -------- Predicted outcome --------
    # Predicted ratings
    p1_rat = playerA_rating
    p2_rat = playerB_rating

    # Define q1 and q2 for simplification of the calculation for expected score
    q1 = 10**(p1_rat / 400)
    q2 = 10**(p2_rat / 400)

    # Expected for each player respectively
    exp_1 = q1 / (q1 + q2)
    exp_2 = q2 / (q1 + q2)

    # -------- Actual outcome --------
    # Calculate the actual score from the outcome of the match (in our case completion of integrals)

    # Predicted ratings
    act_p1_rat = playerA_act_rating
    act_p2_rat = playerB_act_rating

    # Define q1 and q2 for simplification of the calculation for expected score
    act_q1 = 10**(act_p1_rat / 400)
    act_q2 = 10**(act_p2_rat / 400)

    # Actual score (in perspective of player A)
    # Added perturbation
    if 0 > perturbation or perturbation > 1:
        raise ValueError('Invalid value for perturbation')
    act_score = act_q1 / (act_q1 + act_q2)
    lower_lim = act_score - perturbation
    upper_lim = act_score + perturbation
    if lower_lim < 0:
        lower_lim = 0  # Actual score can't be smaller than 0
    if upper_lim > 1:
        upper_lim = 1  # Actual score can't be greater than 1
    act_score = uniform(lower_lim, upper_lim)  # Randomly chooses value between the upper and lower limits

    # Define the K value of the algorithm. This should ideally vary depending on the players and how
    # many games have been played. (I.e someone whos played 100 games should have a lower K value than
    # someone who has played only 3 games)
    # E.g k = 32

    # Calculate the new player ratings
    new_p1_rat = p1_rat + k_value * (act_score - exp_1)
    new_p2_rat = p2_rat + k_value * (1 - act_score - exp_2)

    return new_p1_rat, new_p2_rat


def simulate_elo(games, perturbation):
    """
    :param games: Number of games for each player to play
    :param perturbation: The randomness for each game played
    :return:
    """

    # Define student elo ratings
    # The real elo ratings of the students
    act_student_ratings = {'student1': 300, 'student2': 500, 'student3': 700, 'student4': 800, 'student5': 900, 'student6': 1100,
                          'student7': 1200, 'student8': 1300, 'student9': 1500, 'student10': 1700}

    # The predicted elo ratings of the students
    pred_student_ratings = {'student1': 1000, 'student2': 1000, 'student3': 1000, 'student4': 1000, 'student5': 1000,
                           'student6': 1000, 'student7': 1000, 'student8': 1000, 'student9': 1000, 'student10': 1000}

    # Elo ratings for questions
    question_ratings = {'question1': 300, 'question2': 500, 'question3': 700, 'question4': 800, 'question5': 900, 'question6': 1100,
                        'question7': 1200, 'question8': 1300, 'question9': 1500, 'question10': 1700}

    # List of keys for dictionaries
    student_keys = list(act_student_ratings.keys())
    question_keys = list(question_ratings.keys())

    # Set up a list for data
    data_points = [0]*games
    data_points[0] = list(pred_student_ratings.values())
    for i in range(1, games):
        if i < 100:  # k value varies depending on the number of games playedd
            k = 32
        elif 100 <= i < 500:
            k = 16
        else:
            k = 10
        sample_list = list(student_keys)  # Create a list to sample from without replacement
        while sample_list:
            playerA, playerB = random.sample(sample_list, 2)
            sample_list.remove(playerA)
            sample_list.remove(playerB)

            # Find values for elo ratings
            playerA_rating = pred_student_ratings[playerA]
            playerB_rating = pred_student_ratings[playerB]
            act_playerA_rating = act_student_ratings[playerA]
            act_playerB_rating = act_student_ratings[playerB]

            # Calculate new ratings and assign the new values into the dictionary
            new_ratings = update_ratings(playerA_rating, playerB_rating, act_playerA_rating, act_playerB_rating, k, perturbation)
            pred_student_ratings[playerA], pred_student_ratings[playerB] = new_ratings

        # Fill in the new data point for the ratings of each player
        data_points[i] = list(pred_student_ratings.values())

    # Plot data
    plt.plot(data_points)
    plt.show()


# IGNORE THIS FUNCTION FOR NOW
def student_vs_question(games, perturbation):
    # Define student elo ratings
    # The real elo ratings of the students
    act_student_ratings = {'student1': 300, 'student2': 500, 'student3': 700, 'student4': 800, 'student5': 900, 'student6': 1100,
                           'student7': 1200, 'student8': 1300, 'student9': 1500, 'student10': 1700}

    # The predicted elo ratings of the students
    pred_student_ratings = {'student1': 1000, 'student2': 1000, 'student3': 1000, 'student4': 1000, 'student5': 1000,
                            'student6': 1000, 'student7': 1000, 'student8': 1000, 'student9': 1000, 'student10': 1000}

    # Elo ratings for questions
    question_ratings = {'question1': 300, 'question2': 500, 'question3': 700, 'question4': 800, 'question5': 900, 'question6': 1100,
                        'question7': 1200, 'question8': 1300, 'question9': 1500, 'question10': 1700}

    student_keys = list(act_student_ratings.keys())
    question_keys = list(question_ratings.keys())

    for i in student_keys:
        for _ in range(0, games):
            pass


simulate_elo(800, 0.1)
