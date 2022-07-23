import test1
from Utils.utils1 import person2
# we have defined the class in the test1.py , Hence we don't have to define it again in this file
object = test1.Person("Rahul","Sharma",1991)
print(object._name1)
print(object._Person__surname1)
print(object.yob1)

# this object is created from the utils file in Utils folder
obj2 = person2("Henabny","Agarwal",2121)
print(obj2._name1)
print(obj2._person2__surname1)
print(obj2.yob1)
