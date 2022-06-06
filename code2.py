def func(*args, **wargs):
    finallist = []
    for i in args:
        finallist.append(i)
    for j in wargs:
        finallist.append(wargs[j])
    return finallist

print(func(21,43,"sasa",a=1,b=2,c="sa"))
