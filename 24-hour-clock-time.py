"""
The 24-hour clock time system is a method of calculating time in a day beginning from one mid night till the next mid-night. A day is divided into 24 hours and is written using numbers between 0 and 23. It does not apply the a.m or p.m. label as being used in the 12-hour clock time system.

Given is the time that is shown in a digital clock, and total of seconds that has passed after the given time.
You are required to find the time to be displayed, after the given seconds have passed.
"""

hour, minute, second = input().split(":")
seconds_to_add = int(input())

# Add the seconds to the current second
second = int(second) + seconds_to_add

# if seconds is greater than 60, add the minutes and subtract the seconds
if second >= 60:
    minute = int(minute) + (second // 60)
    second = second % 60

    # if minutes is greater than 60, add the hours and subtract the minutes
    if minute >= 60:
        hour = int(hour) + (minute // 60)
        minute = minute % 60

        # if hours is greater than 24, subtract the hours
        if hour >= 24:
            hour = hour % 24

# If the hour, minute and seconds < 10, add a 0 in front of the hour, minute and seconds
if hour < 10:
    hour = "0" + str(hour)

if minute < 10:
    minute = "0" + str(minute)

if second < 10:
    second = "0" + str(second)

# join the hour, minute and second to a string
time = str(hour) + ":" + str(minute) + ":" + str(second)
print(time)