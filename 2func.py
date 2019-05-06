from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_second.txt', 'r') as open_file:
          list_of_numbers_from_file = list(map(str, open_file.read().split(','))) 

def length(list_of_lines):
    return sorted(list_of_lines, key=len)

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_second.txt', 'a') as open_file:
    open_file.write('\n' + str(length(list_of_numbers_from_file)))