class Person:
    def __init__(self, name, age):
        # TODO: Make 'name' and 'age' private
        self.__name = name
        self.__age = age

    # TODO: Create setter methods for 'name' and 'age'
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
        

    # TODO: Create getter methods for 'name' and 'age'
    def get_name(self):
        return self.__name
        
    def get_age(self):
        return self.__age

    
        
person = Person("Alice", 30)

# TODO: Change the 'name' and 'age' attributes using the setter methods instead
person.set_name('Bob')
person.set_age(25)
person.name = "Bob"
person.age = 25

# TODO: Print the 'name' and 'age' attributes using the getter methods instead
print("Name:", person.get_name(), ", Age:", person.get_age())