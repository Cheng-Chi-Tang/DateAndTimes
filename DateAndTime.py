class DateAndTime:
    def __init__(self, year, month, day, hour_in_24, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour_in_24
        self.minute = minute
    def __str__(self):
        if self.hour > 24 or self.hour < 0:
            return 'error'
        return str(self.year) +'-' + str(self.month) + '-' + str(self.day) + ' ' + str(self.hour) + ':' + str(self.minute)

# This is demo
dateAndTime1 = DateAndTime(2019, 11, 30, 22, 30)
print(dateAndTime1) # 2019-11-30 22:31

dateAndTime2 = DateAndTime(2019, 11, 30, 25, 30)
print(dateAndTime2) # 2019-11-30 22:31