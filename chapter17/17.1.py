#Exercise 17.1

class Time(object):
    def time_to_int(self):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print time.time_to_int()
