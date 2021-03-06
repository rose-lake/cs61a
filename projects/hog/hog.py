"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact
from operator import add, sub   # for free_bacon
from math import log10, floor   # for is_swap

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'

    # BEGIN PROBLEM 1
    results = []
    while num_rolls:
        results.append(dice())
        num_rolls -= 1
    if 1 in results:
        return 1            # 'pig out' rule
    else:
        return sum(results)
    # END PROBLEM 1

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    LOGIC: The points scored from free bacon are equal to...
    - the absolute value
        - of the alternating sum of the digits
            - of the score cubed
    - plus one

    SCORE:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'

    # BEGIN PROBLEM 2
    def digits(n):
        """Return the digits of a natural number N (>=0) in a list

        n:          The natural number
        digits:     The list of digits of N
        """
        assert n >= 0, 'Cannot apply digits to a negative number'
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        return digits

    def next_func(f):
        """Toggle the function F between add and sub

        f:  The function add or sub
        """
        if f == sub:
            return add
        else:
            return sub

    total, func = 0, add   # first step will be 'add first digit to zero'
    cube = score**3
    digits = digits(cube)

    while digits:
        total = func(total, digits.pop())
        func = next_func(func)

    return abs(total) + 1
    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    LOGIC:
    - if the number of rolls is zero, apply free_bacon to the opponent's score
    - otherwise, roll the dice the requested number of times

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped

    GOAL:
    - excitement = 3 ** (player_score + opponent_score)
    - if the first and last digits of excitement are equal, then True, else False

    LOGIC: to grab the first digit of c directly:
    first, let c = log10(a^b) = b * log10(a)
            where b is the power (player_score + opponent_score)
            and a is 3
    by definition of logarithm, c is the POWER of 10 which gives a^b.

    then, truncate c to its whole-number portion by calling floor(c)
    this will give the power of 10 to floor-divide by,
    which in turn gives us the first digit of 'excitement'
        - suppose c were already exact
            then the first digit of a^b is 1
            rounding it makes no difference to the result
        - suppose c had a decimal-fraction
            the whole number part of c will exactly represent the power of 10 we want
                because c+1 is when we go to the next place value
                by definition, c+decimal-fraction < c+1, so we're good
    """
    # BEGIN PROBLEM 4

    # set up for computing 10^c == 3^b
    b = player_score + opponent_score
    c = b * log10(3)

    place_value = floor(c)
    excitement = 3 ** b

    first_digit = excitement // 10 ** place_value
    last_digit = excitement % 10

    return first_digit == last_digit
    # END PROBLEM 4

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    feral_hogs: A boolean indicating whether the feral hogs rule should be active.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    turn0, turn1 = 0, 0
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            turn0_curr = take_turn(num_rolls, score1, dice)
            if feral_hogs and abs(num_rolls - turn0) == 2:
                score0 = score0 + turn0_curr + 3
            else:
                score0 = score0 + turn0_curr
            turn0 = turn0_curr
        else:
            num_rolls = strategy1(score1, score0)
            turn1_curr = take_turn(num_rolls, score0, dice)
            if feral_hogs and abs(num_rolls - turn1) == 2:
                score1 = score1 + turn1_curr + 3
            else:
                score1 = score1 + turn1_curr
            turn1 = turn1_curr
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        who = other(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
        say = say(score0, score1)
    # END PROBLEM 6
    return score0, score1


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores

def announce_lead_changes(prev_leader=None):
    """Return a commentary function that announces lead changes.

    >>> f0 = announce_lead_changes()
    >>> f1 = f0(5, 0)
    Player 0 takes the lead by 5
    >>> f2 = f1(5, 12)
    Player 1 takes the lead by 7
    >>> f3 = f2(8, 12)
    >>> f4 = f3(8, 13)
    >>> f5 = f4(15, 13)
    Player 0 takes the lead by 2
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != prev_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say

def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> h0 = both(say_scores, announce_lead_changes())
    >>> h1 = h0(10, 0)
    Player 0 now has 10 and Player 1 now has 0
    Player 0 takes the lead by 10
    >>> h2 = h1(10, 6)
    Player 0 now has 10 and Player 1 now has 6
    >>> h3 = h2(6, 17)
    Player 0 now has 6 and Player 1 now has 17
    Player 1 takes the lead by 11
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def announce_highest(who, prev_high=0, prev_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 11)
    11 point(s)! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 11)
    >>> f4 = f3(13, 20)
    >>> f5 = f4(20, 35)
    15 point(s)! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 47) # Player 1 gets 12 points; not enough for a new high
    >>> f7 = f6(21, 47)
    >>> f8 = f7(21, 77)
    30 point(s)! That's the biggest gain yet for Player 1
    >>> f9 = f8(77, 22) # Swap!
    >>> f10 = f9(33, 77) # Swap!
    55 point(s)! That's the biggest gain yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    def say(score0, score1):
        if who == 0:
            new_high = score0 - prev_score
            if new_high > prev_high:
                print(new_high, "point(s)! That's the biggest gain yet for Player", who)
                return announce_highest(who, new_high, score0)
            else:
                return announce_highest(who, prev_high, score0)
        else:
            new_high = score1 - prev_score
            if new_high > prev_high:
                print(new_high, "point(s)! That's the biggest gain yet for Player", who)
                return announce_highest(who, new_high, score1)
            else:
                return announce_highest(who, prev_high, score1)
    return say
    # END PROBLEM 7


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(g, num_samples=1000):
    """Return a function that returns the average value of G when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    assert num_samples > 0, "you can only request a positive number of samples"
    def average_and_return(*args):
        # initialize for loop by taking first sample
        result, n = g(*args), num_samples - 1
        # loop through the rest of the samples, if any
        while n:
            result += g(*args)
            n = n - 1
        return result / num_samples
    return average_and_return
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    Solving a Tie: If two numbers of rolls are tied for the maximum average score, return the lower number of rolls.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    num_dice = 10
    results, n = [], num_dice
    average_roll_dice = make_averaged(roll_dice,num_samples)
    while n:
        # roll dice from 1 to 10
        results.append(average_roll_dice(num_dice - n + 1,dice))
        n = n - 1
    # Because our number of rolls start from 1 dice and go up to 10 dice,
    # our results list is populated from smallest to largest number of rolls,
    # and we can easily satisfy the 'Solving a Tie' requirement
    # by exploiting the default behavior of Python's max() function
    # which, in case of a tie, will return the FIRST max value it encountered,
    # which in this case, would be the value for the lower number of rolls.
    return results.index(max(results)) + 1
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    # Explantory note to self:
    # this call structure builds the make_averaged function using 'winner'
    # calls it immediately with the arguments required by 'winner'
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test always_roll(7)
        print('always_roll(7) win rate:', average_win_rate(always_roll(7)))

    if False:  # Change to True to test always_roll(N) for varied N
        print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))
        print('bacon_strategy win rate against always_roll(4):', average_win_rate(bacon_strategy, always_roll(4)))
        # question: how to test with other margins than the default margin of 8 ?

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))
        # print('swap_strategy win rate against always_roll(4):',
        #       average_win_rate(swap_strategy, always_roll(4)))
        # print('swap_strategy win rate against always_roll(6):',
        #       average_win_rate(swap_strategy, always_roll(6)))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if free_bacon(opponent_score) >= margin:
        return 0
    else:
        return num_rolls
    # return 6  # Replace this statement
    # END PROBLEM 10


def swap_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and does not trigger a
    non-beneficial swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    free_score = free_bacon(opponent_score)
    new_score = score + free_score

    # swap is triggered
    if is_swap(new_score, opponent_score):

        # if it's a good swap, roll 0 to trigger it
        if opponent_score >= new_score:
            return 0
        else:
            return num_rolls

    # swap is not triggered.
    else:

        # if free_bacon is AT LEAST margin, roll 0
        if free_score >= margin:
            return 0

        # roll num_rolls to avoid less than margin result
        else:
            return num_rolls

    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    Since MARGIN=8 is the default value passed into swap_strategy (*see note*), the key is to check when this margin works against us rather than for us, namely, check to see when we are within MARGIN of GOAL_SCORE. In such a case, we simply modify the MARGIN parameter to be the distance to GOAL_SCORE.

    Another tweak is to modify the NUM_ROLLS parameter as we approach GOAL_SCORE, we wish to reduce NUM_ROLLS to reduce risk.

    This strategy gives a consistently higher win_rate than calling swap_strategy alone.
    """
    # BEGIN PROBLEM 12
    # always higher than swap_stratgey
    # consistently returns win rates between .59 and .62+ win rate
    # the lowest win rate I've seen was .5855, and a rate this low is rare
    margin = 8
    if score > GOAL_SCORE - margin:
        return swap_strategy(score, opponent_score, GOAL_SCORE - score, 2)
    elif score > GOAL_SCORE - 2*margin:
        return swap_strategy(score, opponent_score, margin, 4)
    else:
        return swap_strategy(score, opponent_score)
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
