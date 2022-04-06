import term_info
#import os

c = "a"
terminal = term_info.terminal()
while(c != "q"):
    c = terminal.getch()
    s = c * terminal.columns
    for i in range(0, terminal.rows):
        print(s)



#print(terminal.columns)
