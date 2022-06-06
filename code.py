def func(*args):
    newlist = []
    for i in args:
        for j in i:
            newlist.append(j)
    return newlist

print(func([21,32],[634,21],[33],["dsa"]))
