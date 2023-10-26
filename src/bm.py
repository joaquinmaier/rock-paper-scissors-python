# BM = https://www.urbandictionary.com/define.php?term=BM
import time
from .ui import BM_LINE_COLOR, NO_COLOR

start_time: float = -1

def start_bm_counter() -> None:
    global start_time

    start_time = time.time()

def show_bm_message() -> None:
    total_time_spent = time.time() - start_time

    if total_time_spent > 60 and (total_time_spent / 60) > 60:
        hours_spent = (total_time_spent / 60) / 60
        minutes_spent = (total_time_spent / 60) % 60
        seconds_spent = total_time_spent % 60

        print(f'{BM_LINE_COLOR}You\'ve been owned for {(int)(hours_spent)}h {(int)(minutes_spent)}m and {(int)(seconds_spent)}s (sheesh!).{NO_COLOR}')

    elif total_time_spent > 60:
        minutes_spent = total_time_spent / 60
        seconds_spent = total_time_spent % 60

        print(f'{BM_LINE_COLOR}You\'ve been owned for {(int)(minutes_spent)}m and {(int)(seconds_spent)}s.{NO_COLOR}')

    else:
        print(f'{BM_LINE_COLOR}You\'ve been owned for {(int)(total_time_spent)} seconds.{NO_COLOR}')
