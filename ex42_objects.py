## Animal is-a object 
class Animal(object):
    pass

## dog inherit from Animal 
class Dog(Animal):

    def __init__(self, name):
        #Dog has-a attribute named (name)
        self.name = name


#cat inherit from Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has-a attribute named (name)
        self.name = name

#Person is a object
class Person (object):
    def __init__(self, name):
    ## Person has a attribute named (name)
        self.name = name
    #Person may have a pet, if value not false or none 
        self.pet = False


# Employee inherit from Person object
class Employee(Person):
    def __init__(self, name, salary):
        ##  Employee has two attributes that sakes name and salry
        super (Employee, self).__init__(name)
        self.salary = salary

#fish is a object
class Fish(object):
    pass

# Salmon inherit from fish and is a type of fish 
class Salmon(Fish):
    pass

#class Halibut inherit from fish and is a type of fish
class Halibut(Fish): 
    pass

#rover is a dog
rover = Dog("Rover")

#satan is a cat
satan = Cat ("Satan")

#mary is a person
mary = Person("Mary")

#marys pet is satan
mary.pet = satan

#fraks is a empoyee and makes 120000
frank = Employee("Frank", 120000)

#franks pet is rover
frank.pet = rover

#flipper is a fish
flipper = Fish()
#crouse is the name os the type salmon fish 
crouse = Salmon()
#harry is a halibut
harry = Halibut ()