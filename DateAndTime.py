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
    
    def __ge__(self, other):
        return self.year > other.year or \
                (self.year == other.year and self.month > other.month) or \
                (self.year == other.year and self.month == other.month and self.day > self.month)

    def getHourDifference(dateAndTime1, dateAndTime2): # Assume dateAndTime2 is after dateAndTime1, and at most one month difference

        cross_month_set = {"1-31,2-1", "2-28,3-1", "3-31,4-1", "4-30,5-1", "5-31,6-1", "6-30,7-1", 
                        "7-31,8-1", "8-31,9-1", "9-30,10-1", "10-31,11-1", "11-30,12-1", "1-31,1-1"}
        if dateAndTime1 >= dateAndTime2: # swap
            temp = dateAndTime1
            dateAndTime1 = dateAndTime2
            dateAndTime2 = temp

        month1 = dateAndTime1.month
        month2 = dateAndTime2.month
        day1 = dateAndTime1.day
        day2 = dateAndTime2.day
        hour1 = dateAndTime1.hour
        hour2 = dateAndTime2.hour
        total_hour = 0
        total_day = 0
        
        date_pair = str(dateAndTime1.month) + '-' + str(dateAndTime1.day) + ',' + str(dateAndTime2.month) + '-' + str(dateAndTime2.day)
        if date_pair in cross_month_set or (month1 == month2 and day2 - day1 == 1):
            return hour2 + (24 - hour1)
        if (month1 == month2 and day2 == day1):
            return hour2 - hour1
        if (month1 == month2 and day2 != day1):
            return 24 * (day2 - day1 - 1) + hour2 + (24 - hour1)
        
        delta_month = month2 - month1 + 1
        for i in range(delta_month):
            print('i in delta_month:' + str(i))
            if i == 0:
                total_day += DateAndTime.CONST_COMM_YEAR_DAYS[month1-1] - day1 - 1
            if i == delta_month - 1:
                total_day += (day2 - 1)
            if i != 0 and i != delta_month - 1:
                total_day += DateAndTime.CONST_COMM_YEAR_DAYS[month1 + i]
        total_hour += total_day * 24
        total_hour += hour2 + (24 - hour1)
        return total_hour

# Demo Part
dateAndTime1 = DateAndTime(2019, 11, 30, 22, 30)
print(dateAndTime1) # 2019-11-30 22:31

dateAndTime2 = DateAndTime(2019, 12, 1, 12, 30)
print(dateAndTime2) # 2019-11-30 22:31

dateAndTime3 = DateAndTime(2000, 2, 29, 23, 30)
print(dateAndTime3) # 2019-2-29 23:30

print('difference hour between dateAndTime1 and dateAndTime2:')
print(str(DateAndTime.getHourDifference(dateAndTime1, dateAndTime1)))