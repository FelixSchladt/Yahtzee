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


def quadrupel(throws: []) -> int:
    '''This method checks whether the eyes fullfill
       the requirements of a triplet and returns the score

       :param throws: the throws that will be checked
       :returns: whether the rule was fullfilled or not as well as the potential score
    '''
    return multiple(throws, 4)


def full_house(throws: []) -> int:
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


def small_road() -> int:
    return 30


def big_road() -> int:
    return 40


def yahtzee() -> int:
    return 50


def chance() -> int:
    # return sum of all eyes
    pass
