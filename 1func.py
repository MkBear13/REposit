list_of_elements = [1,2,3,4,4]
def povtor(list_of_elements):
    set_a = set(list_of_elements)
    max = 0
    for x in set_a:
        if list_of_elements.count(x) > max:
            max = list_of_elements.count(x)
    return(max)
