import term_info
import exceptions

class tui_engine:
    def __init__(self):
        self.terminal = term_info.terminal()
        self.__grid_init()
        self.display_width = self.terminal.columns
        self.display_height = self.terminal.rows-1


    def __grid_init(self):
        #grid[y][x]
        self.grid = [[" " for j in range(self.terminal.columns)] for i in range(self.terminal.rows)]


    def clear(self):
        self.__grid_init()


    def flush(self):
        for i in range(0, len(self.grid)):
            print("".join(self.grid[i]))

    def pixel(self, x, y, char):
        if len(char) != 1:
            raise InvalidLenght
        if len(self.grid) < y or len(self.grid[0]) < x:
            raise OutOfBounds
        self.grid[y+1][x] = char

    def text(self, x, y, txt, length=None):
        lenght = len(txt) if length is None else length
        i = 0
        for x0 in range(x, x + int(lenght)):
            self.pixel(x0, y, txt[i])
            i+=1


    def frame(self, x0 = 0, y0 = 0, x1 = None, y1 = None):
        x1 = self.display_width-1 if x1 is None else x1
        y1 = self.display_height-1 if y1 is None else y1

        self.pixel(x0, y0, "┌")
        self.pixel(x0, y1, "└")
        self.pixel(x1, y0, "┐")
        self.pixel(x1, y1, "┘")

        self.line_horizontal(y0, x0+1, x1, color = "─")
        self.line_horizontal(y1, x0+1, x1, color = "─")

        self.line_vertical( x0, y0+1, y1, color = "│")
        self.line_vertical( x1, y0+1, y1, color = "│")


    ### Draw line horizontal ###
    # draw a horizontal line spannign the total display
    #
    # y       -> start point (x = 0, y = ?)
    # color   -> 0 = black , 1 = colored | optional

    def line_horizontal(self, y, x0 = 0, x1 = None, width = 1, color = " "):
        x1 = self.display_width-1 if x1 is None else x1
        for offset in range(0, width, 1 if 0 < width else -1):
            for x in range(x0, x1):
                self.pixel(x, y + offset, color)


    ### Draw line vertical ###
    # draw a vertical line spannign the total display
    #
    # y       -> start point (x = ?, y = 0)
    # color   -> 0 = black , 1 = colored  | optional

    def line_vertical(self, x, y0 = 0, y1 = None, width = 1, color = " "):
        y1 = self.display_height-1 if y1 is None else y1
        for offset in range(0, width, 1 if 0 < width else -1):
            for y in range(y0, y1):
                self.pixel(x + offset, y, color)


if __name__ == "__main__":
    tui = tui_engine()
    for i in range(0, 10):
        tui.clear()
        #tui.line_vertical(10+i, color = tui.terminal.getch())
        #tui.circle(color = tui.terminal.getch())
        tui.frame()
        tui.frame(10, 10, 30, 30)
        tui.text(12, 12, "TesT")
        tui.terminal.getch()
        tui.flush()

