# File Handler
The file handler is responsible for reading and writing the score of the game to a file.

# Functions
The file handler contains two function for reading from a file and writing to a file.

- save_score(json_dict):
      This method saves the score of the game in a json file in form of a dictionary. 
      Either it saves the data to an existing file or it creates a new one.

- get_score:
      This mehtod reads the score of the game from the json file „score_yatzee.json“. 
      If the file is empty, it will return None. 
      If the file is not empty, it will return the file content.

