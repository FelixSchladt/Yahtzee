from dices import get_dices
from random import getrandbits
from tui_engine import CATEGORIES

class Player:
    def __init__(self, name, active = False):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

        self.dices = get_dices()
        for key in CATEGORIES:
            self.value[key] = None



def new_players(name_1, name_2):
    if getrandbits(1):
        return Player(name_1, True), Player(name_2)
    else:
        return Player(name_2, True), Player(name_1)


if __name__ == "__main__":
    p = Player("Peter", True)
    print(p.active)

