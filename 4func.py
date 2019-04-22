import calendar


def leap(year):
    return (calendar.isleap(year))


def leap_2(year):
    return year%400 == 0  or (year%4 == 0 and year%100 != 0)