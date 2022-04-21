"""This file reads and writes the score to a file"""

import os
import json
#from exeptions import EmptyFileError


def save(json_dict: {}, path: str):
    """
    This method saves the score in a json file

    :param json_dict: The state of all players of the game
    :param path: The file path
    :returns: None
    """
    acess = "w" if os.path.isfile(f"{path}.json") else "x"
    with open(f"{path}.json", acess, encoding="UTF-8") as file:
        json.dump(json_dict, file)


def load(path: str):
    """
    This method gets the score from a json file.

    :param path: the path to the save file
    :return: A dictionray containing the players state or None
    """
    if os.stat(f"{path}.json").st_size > 0:
        with open("score_yahtzee.json", "r", encoding="UTF-8") as file:
            file_content = json.load(file)
            return file_content

    return None
