# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     def start(self):
#         print("Bus started")

# School_bus = Bus("School Volvo", 180, 12)
# School_bus.start()
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage,"Km")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Vishnu", 23)
# p2 = Person("Jishnu",21)
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = Person("Vishnu", 23)
# print(p1)

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#     x.move()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move!")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()