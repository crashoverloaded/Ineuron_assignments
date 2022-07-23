class Car:
    def __init__(self,body , engine , tyre):
        self.body1 = body
        self.engine1 = engine
        self.tyre1 = tyre

    def mileage(self):
        print("Mileage of this car")

class newCar(Car):
    pass

object_car = Car("red","v8","17inch")
object_newCar = newCar("blue","v7","16inch")
object_newCar.mileage()