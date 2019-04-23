from context_manager import ContextManager

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_third.txt', 'r') as open_file:
          all_lines = open_file.readlines()
          first_list_from_file = list(all_lines[0].replace('\n', '').split(','))
          second_list_from_file = list(map(str, all_lines[1].replace('\n', '').split(',')))
          dictor_from_file = dict(zip(list(all_lines[2].replace('\n', '').split(',')),
                          list(map(str, all_lines[3].replace('\n', '').split(',')))))

def slovar(first_list, second_list, dictor={}):
    final_dictionary = dict(zip(first_list, second_list))
    if dictor == {}:
        return(final_dictionary)
    dictor.update(final_dictionary)
    return(dictor)

with ContextManager(r'C:\Users\Mikhail.Kavaliov\Desktop\New folder\for_third.txt', 'a') as open_file:
    open_file.write('\n' + str(slovar(first_list_from_file, second_list_from_file, dictor_from_file)))