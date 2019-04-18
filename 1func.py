list1=[1,2,3,4,4]
def function(list):
    set_a = set(list1)
    max = 0
    for x in set_a:
        if list1.count(x) > max:
            max = list1.count(x)
        else:
            max = 0
    print(max)
