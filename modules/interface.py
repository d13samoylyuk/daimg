from time import sleep
from modules.system import clear_terminal


def inform(text='Loading...',
               sleep_time=0,
               clear_term=False):
    if clear_term:
        clear_terminal()
    print(text)
    sleep(sleep_time)