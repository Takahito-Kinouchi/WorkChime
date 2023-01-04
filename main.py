import schedule
from timer import Timer
from time import sleep


def main():
    timer = Timer()
    schedule.every().day.at(timer.lunch_begin).do(timer.lunch_break_begin)
    schedule.every().day.at(timer.lunch_end).do(timer.lunch_break_end)
    schedule.every().day.at(timer.end_time).do(timer.work_end)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
