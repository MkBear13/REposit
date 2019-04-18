import calendar
def f(arg):
    if calendar.isleap(arg)==True:
        print('Год високосный')
    else:
        print('Год не високосный')
def func(arg):
    if arg%400==0  or (arg%4==0 and arg%100!=0):
        print('Год  високосный')
    else:
        print('Год не високосный')

