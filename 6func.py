from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_sixth.txt', 'r') as open_file:
          number_from_file = int(open_file.read()) 


def element(n):
    znach = 0
    for i in range(1, n+1):
       znach += i**i
    wwznach = str(znach)
    return(wwznach[-10:])

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_sixth.txt', 'a') as open_file:
    open_file.write('\nLast 10 symbols : ' + str(element(number_from_file)))