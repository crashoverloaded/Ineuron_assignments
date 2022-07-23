class Person :
    # Initialization of a class or passing data to classname
    # __init__ is used to pass data to class
    # It is a constructor
    # self can be replaced by any variable
    # the first variable "self" is just a pointer to the class Person
    def __init__(self,name ,surname, email_id,yob):
        self.name1 = name
        self.surname1 = surname
        self.email_id = email_id
        self.yob = yob

    def age(self,current_year):
        return current_year - self.yob

# priyank is a variable of Person class
# So these class variables priyank and rahul are known as objects
priyank = Person("Priyank","Agarwal","priyank@gmail.com",2000)
rahul = Person("rahul","sharma","rahul@gmail.com",2122)
print(priyank.name1)
print(rahul.surname1)
print(priyank.email_id)
# using age function in Person class
print(priyank.age(2022))
