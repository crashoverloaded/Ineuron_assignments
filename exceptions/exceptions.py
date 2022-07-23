# Keep suspicious code inside try
try:
    a = 5/4
except ZeroDivisionError as z:
    print("GALAT baat", z)
else:
    print("this will execute when try will execute")
    try:
        f = open("test.txt",'r')
    except:
        print("Issue with internal try code")
