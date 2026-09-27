class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} with {self.doors} doors"


if __name__ == "__main__":
    my_car = Car("Ford", "Mustang", 2024, 2)
    print(my_car.display_info())
    print(isinstance(my_car, Car))
    print(isinstance(my_car, Vehicle))
    print(issubclass(Car, Vehicle))