import curses


def loop(stdscr):
    stdscr.clear()
    stdscr_y, stdscr_x = stdscr.getmaxyx()

    stdscr.border(0)
    str = "Python curses test is go!"
    stdscr.addstr(stdscr_y/2, (stdscr_x/2) - (len(str)/2), str)
    stdscr.refresh()
    stdscr.getch()

    stdscr.endwin

def main(stdscr):
    loop(stdscr) # Main loop

if __name__ == '__main__':
    curses.wrapper(main)