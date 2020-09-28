import datetime
import pandas as pd

def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


a = datetime.datetime.now().time()
b = addSecs(a, 300)
print(a)
print(b)

f = pd.read_csv('wifi_duration.csv')
