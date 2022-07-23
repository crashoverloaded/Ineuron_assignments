try:
    a = 5/0
except ZeroDivisionError as z:
    print("GALAT baat", z)

# Finally block will execute always
finally:
    print("Ye blcodecodeock pakka chalega")
