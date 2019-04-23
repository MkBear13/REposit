import calendar

from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_fourth.txt', 'r') as open_file:
          year_from_file = int(open_file.read()) 


def leap(year):
    return (calendar.isleap(year))


def leap_2(year):
    return year%400 == 0  or (year%4 == 0 and year%100 != 0)

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_fourth.txt', 'a') as open_file:
    open_file.write('\n' + str(leap(year_from_file)))
    open_file.write('\n' + str(leap_2(year_from_file)))