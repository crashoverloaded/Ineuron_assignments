class Person:
    def __init__(self,name,surname,yob):
        # _name1  is a protected variable , we can tell by underscore before variable
        # __surname1  is a private variable , we can tell by double underscore before variable
        # while yob1 is a public variable
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

priyank = Person("Priyank","Agarwal",1999)
# calling a protected variable
print(priyank._name1)
# print(priyank.__surname1) will give error , since it is a private variable
# This is how one can call a private variable in class
print(priyank._Person__surname1)