# without encapsulation
class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model


# without encapsulation
my_car = Car("Red", "Toyota", "Tes1223")
my_car.color = "White"

# print(my_car.color)


# with encapsulation
class EncapsulatedCar:
    def __init__(self, color, brand, model):
        self.__color = color
        self.__brand = brand
        self.__model = model

    def get_color(self):
        return self.__color

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def update_brand(self, value):
        self.__brand = value

    def get_details(self):
        print("Here are the details of the car")
        print(f"Color: {self.__color}")
        print(f"Brand: {self.__brand}")
        print(f"Model: {self.__model}")


# encap = EncapsulatedCar("Red", "Toyota", "Tes1223")
# encap.update_brand("Benz")
# print(encap.get_color())
# print(encap.get_brand())

color = input("Tell me the color of the car: ")
brand = input("Tell me the brand of the car: ")
model = input("Tell me the model of the car: ")

the_car = EncapsulatedCar(color, brand, model)
the_car.get_details()
