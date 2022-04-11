import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


def update_ratings(p1_name, p2_name, actual_ratings, predicted_ratings, k_value, perturbation):
    """
    :param p1_name: String of key for player A
    :param p2_name: String of key for player B
    :param actual_ratings: Dictionary of players true ratings
    :param predicted_ratings: Dictionary of players predicted ratings
    :param k_value: The value that determines how much a rating should change
    :param perturbation: Float between 0-1 which fluctuates that actual score
    :return:
    """
    # -------- Predicted outcome --------
    # Predicted ratings
    p1_rat = predicted_ratings[p1_name]
    p2_rat = predicted_ratings[p2_name]

    # Define q1 and q2 for simplification of the calculation for expected score
    q1 = 10**(p1_rat / 400)
    q2 = 10**(p2_rat / 400)

    # Expected for each player respectively
    exp_1 = q1 / (q1 + q2)
    exp_2 = q2 / (q1 + q2)

    # -------- Actual outcome --------
    # Calculate the actual score from the outcome of the match (in our case completion of integrals)
    # Could have player 1 as positive and player 2 as negative (this is useful for calculations of the
    # new ratings.
    # Predicted ratings
    act_p1_rat = actual_ratings[p1_name]
    act_p2_rat = actual_ratings[p2_name]

    # Define q1 and q2 for simplification of the calculation for expected score
    act_q1 = 10**(act_p1_rat / 400)
    act_q2 = 10**(act_p2_rat / 400)

    # Actual score (in perspective of player A)
    if 0 > perturbation or perturbation > 1:
        raise ValueError('Invalid value for perturbation')
    act_score = act_q1 / (act_q1 + act_q2)
    lower_lim = act_score - perturbation
    upper_lim = act_score + perturbation
    if lower_lim < 0:
        lower_lim = 0
    if upper_lim > 1:
        upper_lim = 1
    act_score = uniform(lower_lim, upper_lim)


    # Define the K value of the algorithm. This should ideally vary depending on the players and how
    # many games have been played. (I.e someone whos played 100 games should have a lower K value than
    # someone who has played only 3 games)
    # E.g k = 32

    # Calculate the new player rating using this equation
    # Note that player 2 has the negative of the result
    new_p1_rat = p1_rat + k_value * (act_score - exp_1)
    predicted_ratings[p1_name] = new_p1_rat

    new_p2_rat = p2_rat + k_value * (1 - act_score - exp_2)
    predicted_ratings[p2_name] = new_p2_rat

    return predicted_ratings


def simulate_elo(games, perturbation):
    # Define Player ratings
    act_player_ratings = {'player1': 300, 'player2': 500, 'player3': 700, 'player4': 800, 'player5': 900, 'player6': 1100,
                          'player7': 1200, 'player8': 1300, 'player9': 1500, 'player10': 1700}

    pred_player_ratings = {'player1': 1000, 'player2': 1000, 'player3': 1000, 'player4': 1000, 'player5': 1000,
                           'player6': 1000, 'player7': 1000, 'player8': 1000, 'player9': 1000, 'player10': 1000}

    keys = list(act_player_ratings.keys())

    data_points = [0]*games
    data_points[0] = list(pred_player_ratings.values())

    for i in range(1, games):
        if i < 100:
            k = 32
        elif 100 <= i < 500:
            k = 16
        else:
            k = 10
        sample_list = list(keys)
        while sample_list:
            playerA, playerB = random.sample(sample_list, 2)
            sample_list.remove(playerA)
            sample_list.remove(playerB)
            pred_player_ratings = update_ratings(playerA, playerB, act_player_ratings, pred_player_ratings, k, perturbation)
        data_points[i] = list(pred_player_ratings.values())

    plt.plot(data_points)
    plt.show()


simulate_elo(800, 0.2)
