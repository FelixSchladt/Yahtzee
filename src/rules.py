#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''This file contains all kniffel rules.
   All results will be returned with the following tupel:
   - (bool, int)

   The boolean is true if the rule applies to a set of given numbers
   and the int is the score that can be earned from each rule in
   combination with a given array of numbers.
'''

def add_faces(throws: [], face: int):
    '''Adds up all numbers equal to self.face

    :param throws: an array of the numbers that are to be added up
    :returns: True to fit the general 'rule'-format
                  and the sum of the numbers
    '''
    score: int = 0

    for i in throws:
        if i == face:
            score += face

    return (score > 0, score)

# TODO better docstrings
# TODO was ist daran besser als an der Multiple class ??? -> unnötige wiederholungen

def aces(throws: []) -> (bool, int):
    '''Returns hthe sum of all ones
    '''
    return add_faces(throws, 1)

def twos(throws: []) -> (bool, int):
    '''Returns hthe sum of all twos
    '''
    return add_faces(throws, 2)

def threes(throws: []) -> (bool, int):
    '''Returns hthe sum of all threes
    '''
    return add_faces(throws, 3)

def fours(throws: []) -> (bool, int):
    '''Returns hthe sum of all fours
    '''
    return add_faces(throws, 4)

def fives(throws: []) -> (bool, int):
    '''Returns hthe sum of all fives
    '''
    return add_faces(throws, 5)

def sixes(throws: []) -> (bool, int):
    '''Returns hthe sum of all sixes
    '''
    return add_faces(throws, 6)

def multiple(throws: [], amount: int) -> (bool, int):
    '''This method checks whether a set of numbers contains a given amount of duplicates

       :param throws: the throws that will be checked
       :param amount: how many duplicates are wanted
       :returns: whether the the amount of multiples exists or not
                 as well as the sum of the duplicate elements
    '''
    equal: int = 0
    score: int = 0
    is_rule: bool = False

    for i in range(1, 7):
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


def small_straight(throws: []) -> (bool, int):
    '''This fuction checks whether the numbers in an array match a "small road".

       :param throws: an array of numbers to be checked
       :returns: whether the rule was fullfilled as well as the potential score
    '''
    score: int = 0
    is_rule: bool = False

    for i in range(1, 4):
        if i in throws\
        and i+1 in throws\
        and i+2 in throws\
        and i+3 in throws:
            score = 30
            is_rule = True
            break

    return (is_rule, score)


def big_straight(throws: []) -> (bool, int):
    '''This fuction checks whether the numbers in an array match a "big road".

       :param throws: an array of numbers to be checked
       :returns: whether the rule was fullfilled as well as the potential score
    '''
    score: int = 0
    is_rule: bool = False

    for i in (1, 2):
        if i in throws\
        and i+1 in throws\
        and i+2 in throws\
        and i+3 in throws\
        and i+4 in throws:
            score = 40
            is_rule = True
            break

    return (is_rule, score)


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


CATEGORIES =["", "Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Total ->"]\
                + [ "Bonus", "Triplet", "Quadrupel", "Full House"]\
                + ["Small Straight", "Large Straight", "Yahtzee", "Chance", "Total"]

RULES = ["multiple", "triplet", "quadrupel", "full_house",
         "small_road", "big_road", "yahtzee", "chance"]

OPTIONS = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes"]\
          + ["Triplet", "Quadrupel", "Full House"]\
          + ["Small Straight", "Large Straight", "Yahtzee", "Chance"]

CATEGORY_FUNCTIONS = [ aces, twos, threes, fours, fives, sixes ]\
                   + [ triplet, quadrupel, full_house, small_straight ]\
                   + [ big_straight, yahtzee, chance]
# TODO ich fand meine implementierung besser, mit der multiple class, wo soll hierdrann der vorteil sein?
