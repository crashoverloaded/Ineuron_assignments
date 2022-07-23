class Ineuron:
    __student = "DATA science"

    def students(self):
        print("Class of students is: ",Ineuron.__student)

object_Ineuron = Ineuron()
object_Ineuron.students()
# This below statement is known as Data abstraction
# Hiding a variable of class from object
# Hence it is using _Ineuron to abstract student variable
print(object_Ineuron._Ineuron__student)