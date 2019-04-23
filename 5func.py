from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_fifth.txt', 'r') as open_file:
          list_of_numbers_from_file = list(map(int, open_file.read().split(',')))  

def sorting(list_of_data):
    for i in range(len(list_of_data) - 1):
        for j in range(len(list_of_data) - i - 1):
            if list_of_data[j] > list_of_data[j + 1]:
                buff = list_of_data[j]
                list_of_data[j] = list_of_data[j + 1]
                list_of_data[j + 1] = buff
    return list_of_data

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_fifth.txt', 'a') as open_file:
    open_file.write('\nSorted list: ' + str(sorting(list_of_numbers_from_file)))