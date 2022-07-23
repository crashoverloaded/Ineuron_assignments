def create_exception(a):
    if a == 6:
        # if 6 is passed in function then , a exception will be raised
        raise Exception(a)
    else:
        print("INput is OK")
    return a
try:
    create_exception(6)
except Exception as e:
    print("Error is: ",e)