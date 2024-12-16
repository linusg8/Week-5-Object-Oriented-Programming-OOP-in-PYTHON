# activity 1

class Aeroplan:

  def __init__(self, model, capacity, range):
    self.model = model
    self.capacity = capacity
    self.range = range

  def fly(self):
    print(f"{self.model} is flying with a capacity of {self.capacity} and a range of {self.range}.")

class Boeing747(Aeroplan):
  def __init__(self):
    super().__init__("Boeing 747", 400, 7000)

class AirbusA380(Aeroplan):
  def __init__(self):
    super().__init__("Airbus A380", 500, 8000)

if __name__ == "__main__":
  boeing747 = Boeing747()
  airbusA380 = AirbusA380()

  boeing747.fly()
  airbusA380.fly()

# activity 2
  class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"The {self.make} {self.model} is driving")


class Plane:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"The {self.make} {self.model} is flying")


def main():
    animal = Animal("dog")
    animal.move()  # Output: dog is moving

    car = Car("Toyota", "Camry")
    car.move()  # Output: The Toyota Camry is driving

    plane = Plane("Boeing", "747")
    plane.move()  # Output: The Boeing 747 is flying


if __name__ == "__main__":
    main()