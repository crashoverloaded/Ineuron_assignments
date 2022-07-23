# Parent class
class Person :
    # protected variable
    _name = "sudh"
    # private variable
    __surname = "kumar"
    # public variable
    yob = 1999

    # Protected Function
    def _age1(self,current_year):
        return current_year - self.yob

    # Private Function
    def __age2(self,current_year):
        return current_year - self.yob
obj1 = Person()

# Inheritance -> passing all properties of parent class
# Child class
class Employee(Person):
    _name = "Priyank"
    __surname = "Agarwal"
    yob = 1990

obj2 = Employee()
print(obj2.yob)
print(obj2._name)
print(obj2._Employee__surname)
print(obj2._Person__surname)


