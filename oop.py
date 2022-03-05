# Object Oriented Programming

# attribute: height, weight, gender, hairColor
# eat, walk, talk, write | task

class Human():

    def __init__(self, height, weight, gender, hairColor):
        self.height = height
        self.weight = weight
        self.gender = gender
        self.hairColor = hairColor

    def eat(self):
        print('Eating...')

    def walk(self):
        print('Walking...')

    def talk(self):
        print('talking...')

    def write(self):
        print('Writing...')


person1 = Human(6, 75, "Male", 'Black')
print(person1.weight)
person1.walk()
person1.write()
person2 = Human(5.9, 72, "Trans", "Blonde")



