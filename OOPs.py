class Human:
    def _init_(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def eating(self, food):
        return "{} is eating {}".format(self.name, food)

Adi = Human("Aditya", 6, 60)
preet = Human("Preetpal", 5.5, 46)

print("Height of {} is {}".format(Adi.name, Adi.height))
print("Weight of {} is {}".format(Adi.name, Adi.weight))
print(Adi.eating("Burger"))
print("Weight of {} is {}".format(preet.name, preet.height))
print("Weight of {} is {}".format(preet.name, preet.weight))
print(preet.eating("Cheese Pizza"))
