yearOne = int(input("Enter year of birth: "))
monthOne = int(input("Enter month of birth: "))
dayOne = int(input("Enter day of birth: "))
yearTwo = int(input("Enter current year: "))
monthTwo = int(input("Enter current month: "))
dayTwo = int(input("Enter current day: "))

def isLeapYear(year):
    # Check if the year is a Leap Year
    if year % 400 == 0: #
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    # check how many days in the month there are
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            # check if leap year or not
            if isLeapYear(year):
                return 29
            else:
                return 28
    return 30

def nextDay(year, month, day):
    # Move count to next day, month, year
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def isDateBefore(year1, month1, day1, year2, month2, day2):
    # Check to make sure valid dates
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # count the days between dates
    assert not isDateBefore(year2, month2, day2, year1, month1, day1)
    # if not valid dates quit running here
    days = 0
    while isDateBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days+= 1
    return days

print (daysBetweenDates(yearOne, monthOne, dayOne, yearTwo, monthTwo, dayTwo))
