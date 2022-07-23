def askforint():
    while True:
        try:
            a = int(input("Enter an integer: "))
        except Exception as e:
            print("Error Message: ",e)
        else:
            print("Correct value")
            print("You entered: ",a)
            break
        finally:
            print("close this issue")
askforint()