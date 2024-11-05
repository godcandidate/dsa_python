# TODO: Declare a class called Person
class Person:

    # TODO: Implement a constructor that initializes 'name' and 'age'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # TODO: Implement a 'display' method that prints 'name' and 'age'
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":
    # TODO: Create a Person object with name "Alice" and age 30
    person1 = Person("Alice", 30)

    # TODO: Call the 'display' method on this object to print the details
    person1.display()