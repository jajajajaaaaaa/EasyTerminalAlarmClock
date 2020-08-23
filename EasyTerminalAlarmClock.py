import datetime

alarmHour = int(input("What Hour Do You Want To Wake Up? "))
alarmMinute = int(input("What Minute Do You Want To Wake Up? "))
amPm = str(input("Pm or Am? "))

if(amPm == "Pm"):
    alarmHour = alarmHour + 12

while(True):
    if (alarmHour == datetime.datetime.now().hour and
        alarmMinute == datetime.datetime.now().minute):
       print("WAKE UUUUUUUUUUUUUP!!!!!!!")
       break

print("Exit")