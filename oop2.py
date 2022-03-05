# PascleNotation
class Robot():

    def __init__(self, name, manufacturer, myear):
        self.name = name
        self.manufacturer = manufacturer
        self.myear = myear

    # task/method
    def add(self, x, y):
        print(x+y)

    def greet(self):
        print("Hi there!! I am " + self.name)

    def even_or_odd(self, number):
        if number%2 == 0:
            print("Given number is even")
        else: 
            print("Given number is odd")

robo_22b = Robot('alexa', 'amazon', '2014')
robo_562 = Robot('Siri', 'Apple', '2008')

robo_22b.greet()
robo_22b.even_or_odd(10)
robo_22b.add(10, 908)

