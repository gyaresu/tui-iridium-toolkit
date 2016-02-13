#!/usr/bin/env python

from os import system
import curses

def get_param(screen, y, x, prompt_string):
    #textbox = curses.textpad.Textbox(screen)
    screen.clear()
    screen.border(0)
    screen.addstr(y, x, prompt_string)
    screen.refresh()
    #input = textbox.
    input = screen.getstr(y+5,x, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a == 0:
        print "Command executed correctly"
    else:
        print "Command terminated with an error"
    raw_input("Press enter")
    print ""

def main(stdscr):
    x = 0
    while x != ord('q'):
        stdscr.clear()
        stdscr_y, stdscr_x = stdscr.getmaxyx()
        y = (stdscr_y/3)
        x = (stdscr_x/2)- 20
        stdscr.border(0)
        stdscr.addstr(y+1, x, "1 - Select the iridium-tools directory")
        stdscr.addstr(y+2, x, "3 - Select a save folder")
        stdscr.addstr(y+3, x, "4 - Exit")
        #toolpath = stdscr.getstr(stdscr_y, stdscr_x, 60)
        #stdscr.addstr(y, , toolpath)
        stdscr.refresh()

        x = stdscr.getch()

        if x == ord('1'):
            tools = get_param(stdscr, y, x, "Enter the tools path, (default: /root/iridium-tools)")
            curses.endwin()
            execute_cmd("ls -al " + tools)



            #stdscr.endwin




if __name__ == '__main__':
    curses.wrapper(main)