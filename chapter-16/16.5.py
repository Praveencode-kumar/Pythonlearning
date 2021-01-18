

#Exercise 16.5. Rewrite increment using time_to_int and int_to_time.
#In some ways, converting from base 60 to base 10 and back is harder than just dealing with
#times. Base conversion is more abstract; our intuition for dealing with time values is better.
#But if we have the insight to treat times as base 60 numbers and make the investment of
#writing the conversion functions (time_to_int and int_to_time), we get a program that
#is shorter, easier to read and debug, and more reliable.

import copy


class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment(time, seconds):
    new_time = copy.deepcopy(time)
    new_time = time_to_int(new_time) + seconds
    new_time = int_to_time(new_time)
    print ("New time is: %.2d:%.2d:%.2d"
          % (new_time.hour, new_time.minute, new_time.second))

increment(time, 300)


