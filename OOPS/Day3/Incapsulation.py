class Ineuron:
    def __init__(self):
        self.student1 = "I - Data Science"

    def students(self):
        print(self.student1)

obj_ineuron = Ineuron()
obj_ineuron.students()
# We can change the value of class variable since it's public
obj_ineuron.student1 = "I - Analytics"
obj_ineuron.students()

class Ineuron1:
    def __init__(self):
        # Declaring a private variable
        self.__student1 = "I1 - Data Science"

    def students(self):
        print(self.__student1)

    def student_change(self):
        self.__student1 = "I1 - Big data"

obj_ineuron1 = Ineuron1()
obj_ineuron1.students()
obj_ineuron1.__student1 = "I1 - Analytics"
# Above statement will not change the class variable , since the student1 is a private variable
obj_ineuron1.students()

# Having private variable , we cannot change the value by using the object of that class , BUT
# we can change / update the value of private variable in the class itself using method which is student_change in this example
# This process of not allowing a user to change the value of variable using object , but can change
# using method in the class itself is known as incapsulation
obj_ineuron1.student_change()
obj_ineuron1.students()