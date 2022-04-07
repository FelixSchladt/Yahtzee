#!/usr/bin/python3
'''This file contains all kniffel rules.
   All results will be returned with the following tupel:
   - (bool, int)

   The boolean is true if the rule applies to a set of given numbers
   and the int is the score that can be earned from each rule in
   combination with a given array of numbers.
'''


def multiple(throws: [], amount: int) -> (bool, int):
    '''This method checks whether a set of numbers contains a given amount of duplicates

       :param throws: the throws that will be checked
       :param amount: how many duplicates are wanted
       :returns: whether the rule was fullfilled or not as well as the sum of the duplicate elements
    '''
    equal: int = 0
    score: int = 0
    is_rule: bool = False

    for i in range(1,6):
        for eyes in throws:
            if eyes == i:
                equal += 1

        if equal == amount:
            score = i*amount
            is_rule = True
            break

        equal = 0

    return (is_rule, score)

def triplet(throws: []) -> (bool, int):
    '''This method checks whether the eyes fullfill
       the requirements of a triplet and returns the score

       :param throws: the throws that will be checked
       :returns: whether the rule was fullfilled or not as well as the potential score
    '''
    return multiple(throws, 3)


def quadrupel(throws: []) -> (bool, int):
    '''This method checks whether the eyes fullfill
       the requirements of a triplet and returns the score

       :param throws: the throws that will be checked
       :returns: whether the rule was fullfilled or not as well as the potential score
    '''
    return multiple(throws, 4)


def full_house(throws: []) -> (bool, int):
    '''This method checks whether the numbers in an array match a full house.

    :param throws: the throws that will be checked
    :returns: whether the rule was fullfilled and the potential score
    '''
    score: int = 0
    is_rule: bool = False

    first_set = multiple(throws, 2)
    second_set = multiple(throws, 3)

    if first_set[0]\
       and second_set[0]\
       and first_set[1] != second_set[1]:
        score = 25
        is_rule = True

    return (is_rule, score)


def small_road(throws: []) -> (bool, int):
    '''This fuction checks whether the numbers in an array match a "small road".

       :param throws: an array of numbers to be checked
       :returns: whether the rule was fullfilled as well as the potential score
    '''
    return 30


def big_road(throws: []) -> (bool, int):
    '''This fuction checks whether the numbers in an array match a "big road".

       :param throws: an array of numbers to be checked
       :returns: whether the rule was fullfilled as well as the potential score
    '''
    return 40


def yahtzee(throws: []) -> (bool, int):
    '''This method checks whether the numbers in an array match a "full house".

       :param throws: an array of the numbers to be checked
       :returns: whether the rule was fullfilled as well as the potential score
    '''
    score: int = 0
    is_rule: bool = False

    dice_set = multiple(throws, 5)

    if dice_set[0]:
        score = 50
        is_rule = True

    return (is_rule, score)


def chance(throws: []) -> (bool, int):
    '''This method simply returns the sum of all numbers in a given aray

    :param throws: the array whichs numbers should be added up
    :returns: whether the rule is fullfilled or not (here: always True)
              and the potential score
    '''
    score: int = 0
    is_rule: bool = True

    for eyes in throws:
        score += eyes

    return (is_rule, score)
