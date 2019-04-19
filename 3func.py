def slovar(list1,list2,dictor={}):
    d=dict(zip(list1, list2))
    if dictor=={}:
        return(d)
    else:
        dictor.update(d)
        return(dictor)