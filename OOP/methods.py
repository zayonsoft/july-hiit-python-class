class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.is_running = False
        self.programmer = "Favour"

    def start(self):
        self.is_running = True
        print("The car is starting.....")

    def stop(self):
        self.is_running = False
        print("The car is stopping.....")


my_car = Car("Black", "Tesla", "I don't know o")

"""
print(f"Color: {my_car.color}")
print(f"Brand: {my_car.brand}")
print(f"Model: {my_car.model}")
print(f"IS running: {my_car.is_running}")

my_car.start()

print(f"IS running: {my_car.is_running}")
my_car.stop()
"""


# inheritance
class Train(Car):
    pass


t1 = Train("red", "Tanko", "TT34")
