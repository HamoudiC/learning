#dates and times

#uses computers clock
import datetime


date = datetime.date(2026, 12, 16)
today = datetime.date.today()

time = datetime.time(12,30,0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2020,1,1, 12,30,0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(f"We have passed the date: {target_datetime} ")

else:
    print("Target date has not passed.")