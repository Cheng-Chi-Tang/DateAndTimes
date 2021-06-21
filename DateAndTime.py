class DateAndTime:
    CONST_LEAP_YEAR_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    CONST_COMM_YEAR_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, year, month, day, hour_in_24, minute):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour_in_24
        self.minute = minute
    def __str__(self):
        if self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0: # Leap Year Condition
            if self.hour > 24 or self.hour < 0 or self.month <= 0 or self.month > 12 or self.day <= 0 or self.day > DateAndTime.CONST_LEAP_YEAR_DAYS[self.month - 1]:
                return 'error'
        else: # Common Year Condition
            if self.hour > 24 or self.hour < 0 or self.month <= 0 or self.month > 12 or self.day <= 0 or self.day > DateAndTime.CONST_COMM_YEAR_DAYS[self.month - 1]:
                return 'error'
        return str(self.year) +'-' + str(self.month) + '-' + str(self.day) + ' ' + str(self.hour) + ':' + str(self.minute)

# This is demo
dateAndTime1 = DateAndTime(2019, 11, 30, 22, 30)
print(dateAndTime1) # 2019-11-30 22:31

dateAndTime2 = DateAndTime(2019, 11, 30, 25, 30)
print(dateAndTime2) # 2019-11-30 22:31


dateAndTime3 = DateAndTime(2000, 2, 29, 23, 30)
print(dateAndTime3) # 2019-11-30 22:31