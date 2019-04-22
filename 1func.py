from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_first.txt', 'r') as open_file:
          list_of_numbers_from_file = list(map(int, open_file.read().split(','))) 


def povtor(list_of_elements):
    set_a = set(list_of_elements)
    max = 0
    for x in set_a:
        if list_of_elements.count(x) > max:
            max = list_of_elements.count(x)
    return max

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_first.txt', 'a') as open_file:
    open_file.write('\nMax element is: ' + str(povtor(list_of_numbers_from_file)))