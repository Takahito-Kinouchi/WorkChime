import winsound
import datetime


class Timer:

    start_datetime = datetime.datetime.now()
    end_datetime = start_datetime + datetime.timedelta(hours=9)
    start_time = start_datetime.time()
    end_time = end_datetime.strftime('%H:%M')
    lunch_begin = '12:00'
    lunch_end = '13:00'

    def __init__(self):
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
        print(f'今日の勤務終了時間は{self.end_datetime.time()}')

    def lunch_break_begin(self):
        print('昼休憩開始')
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 200)

    def lunch_break_end(self):
        print('昼休憩終わり')
        winsound.Beep(1000, 200)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)

    def work_end(self):
        print('勤務終了')
        winsound.Beep(1000, 200)
        winsound.Beep(1000, 200)
        winsound.Beep(1000, 200)
