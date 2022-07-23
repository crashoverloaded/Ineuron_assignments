# Without init  function
class Person:
        def age(self,current_year,yob):
            return current_year - yob

        def email(self,email_id):
            print("Take Mail ID from a person and print it ",email_id)

        def ask_name(self):
            name  = input("WHat is your name: ")
            return name

        def ask_dob(self):
            dob = input("Enter your DOB: ")
            return dob

sudh = Person()
anuj = Person()
honey = Person()

sudh.email("gdshjkag@gmail.com")
sudh.ask_name()