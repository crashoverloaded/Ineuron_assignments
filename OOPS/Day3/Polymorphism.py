class Ineuron:
    def students(self):
        print("Student details")

class class_type:
    def students(self):
        print("Class type of students")

# This function is behaving like a bridge between both the classes Ineuron and class_type
# As per the object passed to the function , it is behaving differently
# This property is known as Polymorphism
def ineuron_external(object):
    object.students()

obj_ineuron = Ineuron()
obj_classtype = class_type()

ineuron_external(obj_ineuron)
ineuron_external(obj_classtype)