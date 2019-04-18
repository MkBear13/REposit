def f(list1,list2,dictor={}):
    d=dict(zip(list1, list2))
    if dictor=={}:
        print(d)
    else:
        dictor.update(d)
        print(dictor)


