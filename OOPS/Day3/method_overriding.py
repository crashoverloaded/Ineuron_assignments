class Ineuron:
    def Student(self):
        print("Details of student")

    def achievers(self):
        print("List of all achievers")

    def hall_of_fame(self):
        print("list of all hall of famers")

class Ineuron_vision(Ineuron):
    # Method overriding
    # Same name of method in parent and child classes
    # Overriding a method inherited from parent class is method overriding
    def Student(self):
        print("Ineuron vision filtered student")

object_I_vision = Ineuron_vision()
object_I_vision.Student()