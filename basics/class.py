class Person:
    species = "Homo sapiens"  # Class attribute shared by all instances

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


if __name__ == "__main__":

    # creating an object
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    person1.display()
    print(f"{person1.name}'s specie is {person1.species}") 
    print(f"{person2.name}'s specie is {person2.species}")

    Person.species = "Neanderthal"

    print(f"{person1.name}'s specie is {person1.species}")  # Output: Neanderthal