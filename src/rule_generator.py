#!/usr/bin/python3

def check_rules(throws: []) -> int:
    pass

def check_upper_block() -> int:
    pass

def check_lower_block() -> int:
    pass

#
# LOWER BLOCK RULES
#

def triplet(throws: []) -> (bool, int):
    '''This method checks whether the eyes fullfill
       the requirements of a triplet and returns the score

       :param throws: the throws that will be checked
       :returns: whether the rule was fullfilled or not as well as the potential score
    '''
    equal: int = 0
    score: int = 0
    is_rule = False

    for i in range(1,6):
        for eyes in throws:
            if eyes == i:
                equal += 1

        if equal == 3:
            score = i*3
            is_rule = True
            break

        equal = 0

    return (is_rule, score)


def quadrupel(throws: []) -> int:
    '''This method checks whether the eyes fullfill
       the requirements of a triplet and returns the score

       :param throws: the throws that will be checked
       :returns: whether the rule was fullfilled or not as well as the potential score
    '''
    equal: int = 0
    score: int = 0
    is_rule = False

    for i in range(1,6):
        for eyes in throws:
            if eyes == i:
                equal += 1

        if equal == 4:
            score = i*4
            is_rule = True
            break

        equal = 0

    return (is_rule, score)


def full_house() -> int:
    return 25


def small_road() -> int:
    return 30


def big_road() -> int:
    return 40


def yahtzee() -> int:
    return 50


def chance() -> int:
    # return sum of all eyes
    pass
