import time
from plyer import notification

time_hour=float(input("set the time in minute you want to drink water: "))

while(True):
    time.sleep(60*time_hour)
    notification.notify(title="water",message="you should drink water")