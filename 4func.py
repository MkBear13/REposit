import calendar


def visokosn(year):
    if calendar.isleap(year)==True:
        print('Год високосный')
    else:
        print('Год не високосный')
def visocosn2(year):
    if year%400==0  or (year%4==0 and year%100!=0):
        print('Год  високосный')
    else:
        print('Год не високосный')