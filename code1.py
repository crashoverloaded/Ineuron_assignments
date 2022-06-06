def func(*args):

    dt = {}
    for i in args:
        if str(type(i))[8:-2] in dt:
            dt[str(type(i))[8:-2]].append(i)
        else:
            dt[str(type(i))[8:-2]] = [i]

    return dt
print(func(2.5,3,56,[2,312],[433,21],"sa","dtfgd","dsa",32,52,1,2.5,6.2,True,False,True,2+2j))
