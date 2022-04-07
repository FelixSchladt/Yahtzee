import random as generate_random_number_between


class Dice:

    def slice_the_dice(self, dice_numbers, keep_rolling):
        """
        :param dice_numbers:
        :param keep_rolling:
        :return: dice_number (shuffled array dependent on parameters)
        """
        for i in range(0, 5):
            if keep_rolling[i]:
                dice_numbers[i] = int(generate_random_number_between.uniform(1, 7))
       
        return dice_numbers





dice_object = Dice()

dice_object.slice_the_dice(dice_numbers=[1, 2, 3, 4, 5], keep_rolling=[True, True, False, False, False])
