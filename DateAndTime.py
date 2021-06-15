class DateAndTime:
    def __init__(self, year, month, day, hour_in_24, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour_in_24
        self.minute = minute
    def __str__(self):
        return self.year +'-' + self.month + '-' + self.day + ' ' + self.hour + ':' + self.minute

# This is demo
dateAndTime = DateAndTime('2019', '11', '30', '22', '31')
print(dateAndTime)
    