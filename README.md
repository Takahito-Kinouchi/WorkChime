# WorkChime
Have you ever got focused on your work so bad you worked overtime or skipped lunch unintentionally?
If so, this is exactly for you!

## How to use

- Download this folder
- Run `main.py` when you start your work  
** This program uses `winsound` to make beeping sound, so you can't run this on Mac obviously.
- I highly recommend using `pyinstaller` to create a standalone exe file.

## Setting

```python
end_datetime = start_datetime + datetime.timedelta(hours=9)
start_time = start_datetime.time()
end_time = end_datetime.strftime('%H:%M')
lunch_begin = '12:00'
lunch_end = '13:00'
```
- In `timer.py`, `class Timer` has time schedule properties.  
You can modify lunch break time and workhours per day however you like.  
** make sure you put string as properties. Otherwise this program won't work.
