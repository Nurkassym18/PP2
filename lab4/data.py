import datetime 
x = datetime.date.today()
y = x-datetime.timedelta(days=5)  # меняет дату на пять дней 
print(y)

#2
x_today = datetime.date.today()
x_yesterday = x_today - datetime.timedelta(days=1)
x_tomorrow = x_today + datetime.timedelta(days=1)
print(x_today)
print(x_yesterday)
print(x_tomorrow)

#3
today = datetime.datetime.now()
x = today.strftime("%x") + " " +  today.strftime("%X") #02/10/25 17:03:44
print(x)
print(today) #2025-02-10 17:03:44.991276

#4
from datetime import datetime
def sec(now,not_now):
    res = now - not_now
    return int(res.total_seconds())
now = datetime.now()
not_now = datetime.strptime("2020-12-26 02:00:07","%Y-%m-%d %H:%M:%S")
print(sec(now,not_now))