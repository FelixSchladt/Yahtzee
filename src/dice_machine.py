import random as generate_random_number_between


class Dice:
    """class for testing the function "slice_the_dice"""


def slice_the_dice(self, dice_numbers, keep_rolling):
    """
    :param dice_numbers:
    :param keep_rolling:
    :return: dice_number (shuffled array dependent on parameters)
    """

    for i in range(0, 5):
        if keep_rolling[i]:
            dice_numbers[i] = int(generate_random_number_between.uniform(1, 7))
    print(dice_numbers)

    return print


dice_object = Dice()

dice_object.slice_the_dice(keep_rolling=[True, True, False, False, False],
                           dice_numbers=[1, 2, 3, 4, 5])
