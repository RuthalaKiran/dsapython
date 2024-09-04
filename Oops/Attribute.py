# Class Attributes
# Definition: Class attributes are variables that are shared among all instances of a class. They are defined within the class but outside any instance methods.
# Scope: They are accessible using the class name as well as through any instance of the class.
# Usage: Useful for attributes that should be the same for all instances.
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Accessing class attribute
print(Dog.species)  # Output: Canis familiaris

# Accessing class attribute through an instance
my_dog = Dog("Buddy", 3)
print(my_dog.species)  # Output: Canis familiaris


# Instance Attributes
# Definition: Instance attributes are variables that are unique to each instance of a class. They are typically defined within the __init__ method or other instance methods.
# Scope: They are accessible only through instances of the class.
# Usage: Useful for attributes that should vary between different instances.
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)  # Output: 3

another_dog = Dog("Max", 5)
print(another_dog.name)  # Output: Max
print(another_dog.age)  # Output: 5


# Instance Methods
# Definition: Instance methods are functions defined within a class that operate on instances of the class. They have self as their first parameter, which refers to the instance calling the method.
# Scope: They can access and modify instance attributes and call other instance methods using self.
# Usage: Useful for operations that require information about the specific instance.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def have_birthday(self):
        self.age += 1

my_dog = Dog("Buddy", 3)
my_dog.bark()           # Output: Buddy says Woof!
my_dog.have_birthday()
print(my_dog.age)       # Output: 4

