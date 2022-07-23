class Bank:
    def transaction(self):
        print("Total transaction value")

    def account_opening(self):
        print("Account opening status")

    def deposit(self):
        print("Deposited amount")

    def test(self):
        print("Test method from Bank class")

class HDFC(Bank):
    def hdfc_to_icici(self):
        print("Show transactions to icici from hdfc")
    def test(self):
        print("Test method from HDFC class")
class icici(HDFC):
    pass

# multilevel inheritance
object_icici = icici()
object_icici.hdfc_to_icici()
object_icici.deposit()
# In multilevel inheritance if the function name is same in both the classes ,
# It will use the function from next parent class , not the super class(Bank)
# Hence it will use test function from HDFC class
object_icici.test()