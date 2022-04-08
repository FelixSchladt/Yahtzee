from random import randint

class dice:
     def __init__(self):
         self.roll()

     def roll(self):
         self.value = randint(0, 6)
         return self.value

def get_dices():
    return [dice() for i in range(5)]

if __name__ == "__main__":
    dices = get_dices()
    for die in dices:
        print(die.value)
