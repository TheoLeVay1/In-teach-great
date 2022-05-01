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

    print(new_p1_rat, new_p2_rat)
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
    starting_rating = 400
    pred_student_ratings = {'student1': starting_rating, 'student2': starting_rating, 'student3': starting_rating,
                            'student4': starting_rating, 'student5': starting_rating, 'student6': starting_rating,
                            'student7': starting_rating, 'student8': starting_rating, 'student9': starting_rating,
                            'student10': starting_rating}
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
        if i < 100:  # k value varies depending on the number of games played
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
def student_vs_question(games, perturbation, question_dist, individual):
    """
    :param games: How many questions each student will do
    :param perturbation: How much randomness there is in students solving questions
    :param question_dist: The (+-)percentage range of levels for questions
    :param individual: Whether questions vary for each individual student
    :return:
    """

    # Define student elo ratings
    # The real elo ratings of the students
    act_student_ratings = {'student1': 300, 'student2': 500, 'student3': 700, 'student4': 800, 'student5': 900, 'student6': 1100,
                           'student7': 1200, 'student8': 1300, 'student9': 1500, 'student10': 1700}

    # The predicted elo ratings of the students
    starting_rating = 200
    pred_student_ratings = {'student1': starting_rating, 'student2': starting_rating, 'student3': starting_rating,
                            'student4': starting_rating, 'student5': starting_rating, 'student6': starting_rating,
                            'student7': starting_rating, 'student8': starting_rating, 'student9': starting_rating,
                            'student10': starting_rating}

    # List of keys for students (i.e student1, student2 ... student10)
    student_keys = list(act_student_ratings.keys())

    total_question_ratings ={'question1': 200, 'question2': 250, 'question3': 300, 'question4': 350, 'question5': 400,
                             'question6': 450, 'question7': 500, 'question8': 550, 'question9': 600,
                             'question10': 650, 'question11': 700, 'question12': 750, 'question13': 800,
                             'question14': 850, 'question15': 900, 'question16': 950, 'question17': 1000,
                             'question18': 1050, 'question19': 1100, 'question20': 1150, 'question21': 1200,
                             'question22': 1250, 'question23': 1300, 'question24': 1350, 'question25': 1400,
                             'question26': 1450, 'question27': 1500, 'question28': 1550, 'question29': 1600,
                             'question30': 1650, 'question31': 1700, 'question32': 1750, 'question33': 1800,
                             'question34': 1850, 'question35': 1900, 'question36': 1950, 'question37': 2000,
                             'question38': 2050, 'question39': 2100, 'question40': 2150}

    if individual:  # If the questions are for the individual or global
        for i in student_keys:
            student_rating = pred_student_ratings[i]
            student_act_rating = act_student_ratings[i]

            # Elo ratings for questions
            question_ratings = {'question1': 100, 'question2': 200, 'question3': 300, 'question4': 400, 'question5': 500,
                                'question6': 600, 'question7': 700, 'question8': 800, 'question9': 900,
                                'question10': 1000, 'question11': 1100, 'question12': 1200, 'question13': 1300,
                                'question14': 1400, 'question15': 1500, 'question16': 1600, 'question17': 1700,
                                'question18': 1800, 'question19': 1900, 'question20': 2000}

            # Create empty lists for the data points
            student_data = [0]*games
            question_data = [0]*games

            # Run for the number of games specified
            for j in range(0, games):
                if j < 100:  # k value varies depending on the number of games playedd
                    k = 32
                elif 100 <= j < 500:
                    k = 16
                else:
                    k = 10
                # Set the range of questions that the student can get based off their rating
                question_range = dict((k, v) for k, v in question_ratings.items()
                                      if student_rating*(1 + question_dist) >= v >= student_rating/(1 + question_dist))

                # Get the question rating and question name
                question_keys = list(question_range.keys())  # Question names within the rating range
                question = random.choice(question_keys)  # Choose randomly, a question name
                question_rating = question_ratings[question]  # Question rating

                # Update the ratings by using the predicted ratings and actual ratings of questions and students
                new_ratings = update_ratings(student_rating, question_rating, student_act_rating, question_rating,
                                             k, perturbation)

                # Set the question ratings and update the data points
                student_rating, question_ratings[question] = new_ratings
                student_data[j] = student_rating
                question_data[j] = list(question_ratings.values())

            plt.plot(student_data)
            plt.plot(question_data)
            plt.show()

    else:  # If the questions are for the individual or global
        # Create empty lists for the data points
        student_data = [0]*games
        question_data = [0]*games

        # Run for the number of games specified
        for j in range(0, games):
            if j < 100:  # k value varies depending on the number of games playedd
                k = 32
            elif 100 <= j < 500:
                k = 16
            else:
                k = 10

            # List of students
            sample_list = list(student_keys)

            # For each student
            for i in range(0, len(list(pred_student_ratings))):

                # Select a student and remove them from the sample list
                test_student = random.choice(sample_list)
                sample_list.remove(test_student)

                # Find the actual and predicted rating of the student
                student_rating = pred_student_ratings[test_student]
                student_act_rating = act_student_ratings[test_student]

                # Set the range of questions that the student can get based off their rating
                question_range = dict((k, v) for k, v in total_question_ratings.items()
                                      if student_rating*(1 + question_dist) >= v >= student_rating/(1 + question_dist))

                # Choose a random question from that list
                question_keys = list(question_range.keys())
                question = random.choice(question_keys)

                # Find rating of the question
                question_rating = total_question_ratings[question]

                # Find the updated ratings of both the student and question
                new_ratings = update_ratings(student_rating, question_rating, student_act_rating, question_rating, k,
                                             perturbation)
                pred_student_ratings[test_student], total_question_ratings[question] = new_ratings

            # Updating the data for students and questions
            student_data[j] = list(pred_student_ratings.values())
            question_data[j] = list(total_question_ratings.values())

        # Plot graph
        plt.plot(student_data)
        plt.show()
        plt.plot(question_data)
        plt.show()


# simulate_elo(800, 0.1)
student_vs_question(800, 0, 1, False)
