class DateAndTime:
    def __init__(self, year, month, day, hour_in_24, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour_in_24
        self.minute = minute
    def __str__(self):
        if int(self.hour) > 24 or int(self.hour) < 0:
            return 'error'
        return self.year +'-' + self.month + '-' + self.day + ' ' + self.hour + ':' + self.minute

# This is demo
dateAndTime1 = DateAndTime('2019', '11', '30', '22', '31')
print(dateAndTime1) # 2019-11-30 22:31

dateAndTime2 = DateAndTime('2020', '11', '30', '25', '00')
print(dateAndTime2) # 2019-11-30 22:31