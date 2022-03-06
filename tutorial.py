import curses
from curses import wrapper
import enum
from multiprocessing.reduction import steal_handle
from sys import stderr
from textwrap import wrap




def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("welcome to the speed typing test")
    stdscr.addstr("\npress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target_text)
        
    for i, char in enumerate(current_text):
        stdscr.addstr(0, i, char, curses.color_pair(1))



def wpm_test(stdscr):
    target_text = "hellow world this is some text for this app"
    current_text = []
    
    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)        


        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)