def slovar(first_list, second_list, dictor={}):
    final_dictionary = dict(zip(list1, list2))
    if dictor == {}:
        return(final_dictionary)
    dictor.update(final_dictionary)
    return(dictor)