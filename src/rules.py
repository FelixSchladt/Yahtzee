#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''This file contains all kniffel rules.
   All results will be returned with the following tupel:
   - (bool, int)

   The boolean is true if the rule applies to a set of given numbers
   and the int is the score that can be earned from each rule in
   combination with a given array of numbers.
'''

class Multiple:
    def __init__(self, face):
        self.face  = face

    def __call__(self, throws):
        return add_faces(throws, self.face)

#TODO REFACTOR MULTIPLE FUNCITON TO BE ASSIGNED OF ONE TYPE OF FACE INSTEAD OF AMOUNT

def add_faces(throws, face):
    score = 0
    print(throws)

    for dice_face in throws:
        if dice_face == face:
            score += face
    return (True, score)

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


def small_road(throws: []) -> (bool, int):
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


def big_road(throws: []) -> (bool, int):
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


CATEGORIES =["", "Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Total ->",\
                "Bonus", "Three Of A Kind", "Four Of A Kind", "Full House",\
                "Small Straight", "Large Straight", "Yahtzee", "Chance", "Total"]

RULES = ["multiple", "triplet", "quadrupel", "full_house", "small_road", "big_road", "yahtzee", "chance"]


CATEGORY_FUNCTIONS = [ Multiple(face) for face in range(1, 7) ]\
                   + [ eval(item) for item in RULES[3:] ]

