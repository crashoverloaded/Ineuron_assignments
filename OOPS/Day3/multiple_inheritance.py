class Bank:
    def transaction(self):
        print("Total transaction value")

    def account_opening(self):
        print("Account opening status")

    def __deposit(self):
        print("Deposited amount")

    def test(self):
        print("Test method in Bank class")

# These two classes are independent of each other
class HDFC:
    def hdfc_to_icici(self):
        print("Show transactions to icici from hdfc")
    def test(self):
        print("Test method in HDFC class")
# Using multiple inheritance, inheriting from both Bank and HDFC classes
class icici(Bank , HDFC):
    pass

object_icici = icici()
object_icici.hdfc_to_icici()
object_icici._Bank__deposit()
# In multiple inheritance , If function name is same in both or any number of parent classes
# It will choose from the order of parameters in the definition of icici class
# hence while defining icici class , we have mentioned Bank class first
# So it will take the test() fucntion from Bank class and not the HDFC class
object_icici.test()