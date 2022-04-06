import term_info
import exceptions


#terminal = term_info.terminal()

class tui_engine:
    def __init__(self):
        self.terminal = term_info.terminal()
        self.__grid_init()

    def __grid_init(self):
    #grid[y][x]
        self.grid = [[" " for j in range(self.terminal.columns)] for i in range(self.terminal.rows)]

    def render(self):
        for i in range(0, len(self.grid)):
            print("".join(self.grid[i]))

    def pixel(self, x, y, char):
        if len(char) != 1:
            raise InvalidLenght
        self.grid[y][x] = char






if __name__ == "__main__":
    tui = tui_engine()
    tui.render()
    for i in range(0, 10):
        tui.pixel(10,10, tui.terminal.getch())
        tui.render()

