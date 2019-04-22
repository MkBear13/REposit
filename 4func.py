import calendar


def leap(year):
    return (calendar.isleap(year))


def leap_2(year):
    if year%400==0  or (year%4==0 and year%100!=0):
        return (True)
    return(False)      