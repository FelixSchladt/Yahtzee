import os
import json
from exeptions import EmptyFileError


def save_score(json_dict):
    """
    This methods saves the score in a json file
    :rtype: object
    """
    # json_dict = json_dict.to_json()           //Falls es ein Objekt ist
    acess = "w" if os.path.isfile("score_yahtzee.json") else "x"
    with open("score_yahtzee.json", acess, encoding="UTF-8") as file:
        json.dump(json_dict, file)


def get_score():
    """
    This mehtod gets the score from a json file.
    :rtype: object
    """
    if os.stat("score_yahtzee.json").st_size > 0:

        with open("score_yahtzee.json", "r", encoding="UTF-8") as file:
            file_content = json.load(file)
            if not file_content:
                print("no data in file")

        print(file_content)
    else:
        raise EmptyFileError("File is empty")