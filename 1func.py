list1=[1,2,3,4,4]
def povtor(list1):
    set_a = set(list1)
    max = 0
    for x in set_a:
        if list1.count(x) > max:
            max = list1.count(x)
    return(max)
