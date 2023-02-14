"""Ben Berube, Sara Vanaki, Giacomo Raedelli
12.7.2021
COMP305 - Ahn Nuzen
Final Project Prototype Code """

#Import desired packages and libraries
import math
from abc import ABC, abstractmethod
from turtle import Turtle, Screen
import matplotlib
from matplotlib.colors import is_color_like
import turtle
import random


#Definition and implementation of abstract base class
class Fractal(ABC):
    #Constructor: sets abstract object attributes
    def __init__(self, name, color, size, screen, turt):
        self.turt = turt
        self.screen = screen
        self.name = name
        self.color = color
        self.size = size

        # Screen setup
        self.screen.setup(500, 500)
        self.screen.title(self.name + " - Fractal with Italians' Turtle Graphics")

        # Allow added clarity of image given user-specified color
        if (self.color.lower() == "yellow" or self.color.lower() == "orange" or self.color.lower() == "white"):
            self.screen.bgcolor("gray")
        else:
        #Leave background light
            self.screen.bgcolor("white")

        #Set turtle speed to 150 and hide cursor from user view
        self.turt.hideturtle()
        self.turt.speed(150)


    @abstractmethod
    def draw_fractal(self):
        pass


class Star(Fractal):
    #Inherit constructor from parent class
    def __init__(self, name, color, size, screen, turt):
        super().__init__(name, color, size, screen, turt)


    #Star implementation of abstract method draw_fractal
    def draw_fractal(self):

        #Specify image color to user's liking
        self.turt.pencolor(self.color)
        turt.goto(-self.size/2, 0)

        self.star(self.turt, self.size)

        self.screen.exitonclick()

    #Definition of helper function for draw_fractal
    def star(self, turt, size):
        if size <= 10:
            return
        else:
            for i in range(5):  # pylint: disable=unused-variable
                # moving turtle forward
                self.turt.forward(size)
                self.star(turt, size / 3)
                # moving turtle left
                self.turt.left(216)


class Tree(Fractal):
    #Inherit constructor from parent class
    def __init__(self, name, color, age, screen, turt):
        super().__init__(name, color, age, screen, turt)

    def draw_fractal(self):

        #Specify image color to user's liking
        self.turt.pencolor(self.color)
        self.turt.left(90)

        #Call helper function to draw image
        self.tree(self.turt, self.age)

        self.screen.exitonclick()

    #Definition of helper function for draw_fractal
    def tree(self, turt, age):
        #Return when size falls below 10
        if age <= 10:
            return

        else:
            #Implement movement of turtle to generate tree image
            self.turt.forward(age)
            self.turt.left(30)
            self.tree(turt, 3 * age/4)
            self.turt.right(60)
            self.tree(turt, 3 * age/4)
            self.turt.left(30)
            self.turt.backward(age)


class Snowflake(Fractal):
    #Inherit constructor from parent class
    def __init__(self, name, color, size, screen, turt):
        super().__init__(name, color, size, screen, turt)

    def draw_fractal(self):
        self.turt.pencolor(self.color)

        #Call helper function for creating snowflake
        self.snowflake(self.turt, self.size)

        self.screen.exitonclick()

    #Definition of helper function for draw_fractal
    def snowflake(self, turt, size):
        # move the pen into starting position
        self.turt.penup()
        self.turt.forward(10*size)
        self.turt.left(45)
        self.turt.pendown()

        #Draw branch 8 times to make a snowflake
        for i in range(8):  
            for j in range(3):  
                for k in range(3):  
                    self.turt.forward(10.0*size/3)
                    self.turt.backward(10.0*size/3)
                    self.turt.right(45)
                self.turt.left(90)
                self.turt.backward(10.0*size/3)
                self.turt.left(45)
            self.turt.right(90)
            self.turt.forward(10.0*size)
            self.turt.left(45)


class RandomWalk(Fractal):
    # Inherit constructor method from Fractal class
    def __init__(self, name, color, age, screen, turt):
        super().__init__(name, color, age,  screen, turt)

    def draw_fractal(self):
        # Set color of fractal  drawing
        self.turt.pencolor(self.color)

        # Generate multiple Turtle objects to add complexity to drawing
        a = turtle.Turtle()
        b = turtle.Turtle()
        c = turtle.Turtle()
        d = turtle.Turtle()

        #Set the color of all turtle objects to the user specified color
        a.pencolor(self.color)
        b.pencolor(self.color)
        c.pencolor(self.color)
        d.pencolor(self.color)

        # Create list of all turtle objects
        turtList = []
        turtList.append(self.turt)
        turtList.append(a)
        turtList.append(b)
        turtList.append(c)
        turtList.append(d)

        # Increase default speed of each turtle object
        for i in range(len(turtList)):
            turtList[i].speed(150)
            turtList[i].hideturtle()

        # Call fractal helper method

        self.randomWalk(turtList, self.age)

        self.screen.exitonclick()

    # Definition of helper function specific to random walk
    def randomWalk(self, turtList, age):
        for i in range(age):
            #Implement actual movement of each turtle object in the list
            for turt in range(len(turtList)):
                angle = random.randint(0, 3) * 90
                turtList[turt].seth(angle)
                turtList[turt].fd(10)

#User interface
if __name__ == "__main__":
    #Initialize variables to allow the program to be rerun 
    run = True
    while run:
        print("Welcome to the Fractal Drawing Simulator!")
        print("-----------------------------------------------------------------------------------------------")
    
        #Collect user-specified fractal image, desired color and size
        fractal = input('Please enter which fractal you would like to create (Star, Snowflake, Tree, Walk): ')
        fractal = fractal.upper()
        fractals = ["Star", "SNOWFLAKE", "TREE", "WALK"]
        #Ensure user enters a fractal type which exists in the program
        while fractal not in fractals:
            print("Not a valid fractal! Please try again.")
            fractal = input("Please enter which fractal you would like to create (Star, Snowflake, Tree, Walk): ")
            fractal = fractal.upper()

        color = input('Please enter the color you would like to use for your fractal: ')
        #Ensure user enters a color which is recognized in the Turtle class library
        while not is_color_like(color):
            print('Not a valid color!! Please try again.')
            color = input('Please enter the color you would like to use for your fractal: ')
        
        #Case statements that will run particular fractal code according to user preference
        if fractal == 'STAR':
            #Wrap inputs in try/except statements to prevent crashing from ValueError
            retry = True
            while retry:
                try:
                    size = int(input('Please enter an integer (between 100-250) for the size of your fractal: '))
                    #Ensure user enters a valid integer for size (between 100-250)
                    while size<100 or size>250:
                        print('Please choose an integer within the interval. Try again!')
                        size = int(input('Please enter an integer (between 100-250) for the size of your fractal: '))
                    retry=False
                except ValueError:
                    print('You have made a terrible mistake. Please input a VALID integer.')

            turt = turtle.Turtle()
            screen = turtle.Screen()
            #Create star object and call its overridden draw_fractal() method
            star = Star(fractal, color, size, screen, turt)
            star.draw_fractal()

        elif fractal == 'SNOWFLAKE':
            #Wrap inputs in try/except statements to prevent crashing from ValueError
            retry = True
            while retry:
                try:
                    size = int(input('Please enter an integer (between 1-20) for the size of your fractal: '))
                    #Ensure user enters a valid integer for size (between 1 and 20)
                    while size<1 or size>20:
                        print('Please choose an integer within the interval. Try again!')
                        size = int(input('Please enter an integer (between 1-20) for the size of your fractal: '))
                    retry=False
                except ValueError:
                    print('You have made a terrible mistake. Please input a VALID integer.')

            turt = turtle.Turtle()
            screen = turtle.Screen()
            #Create snowflake object and call its overriden draw_fractal() method
            snowflake = Snowflake(fractal, color, size, screen, turt)
            snowflake.draw_fractal()

        elif fractal == 'TREE':
            #Wrap inputs in try/except statements to prevent crashing from ValueError
            retry = True
            while retry:
                try:
                    age = int(input('Please enter an integer (between 25-75) for the age of your fractal: '))
                    #Ensure user enters a valid integer for size (between 25-75)
                    while age<25 or age>75:
                        print('Please choose an integer within the interval. Try again!')
                        age = int(input('Please enter an integer (between 25-75) for the age of your fractal: '))
                    retry=False
                except ValueError:
                    print('You have made a terrible mistake. Please input a VALID integer.')

            turt = turtle.Turtle()
            screen = turtle.Screen()
            #Create tree object and call its overridden draw_fractal() method
            tree = Tree(fractal, color, age, screen, turt)
            tree.draw_fractal()

        elif fractal == "WALK":
        #Wrap inputs in try/except statements to prevent crashing from ValueError
            retry = True
            while retry:
                try:
                    age = int(input('Please enter an integer (between 100 - 300) for the age of your fractal: '))
                    #Ensure user enters a valid integer for size (between 100-300)
                    while age<100 or age>300:
                        print('Please choose an integer within the interval. Try again!')
                        age = int(input('Please enter an integer (between 100 - 300) for the age of your fractal: '))
                    retry=False
                except ValueError:
                    print('You have made a terrible mistake. Please input a VALID integer.')
            
            turt = turtle.Turtle()
            screen = turtle.Screen()
            #Create randomWalk object and call its overriden draw_fractal() method
            walk = RandomWalk(fractal, color, age, screen, turt)
            walk.draw_fractal()
        
        turtle.TurtleScreen._RUNNING = True
        
        rerun = input("Would you like to rerun the program (Enter Y for Yes and N for No)?" )
        if rerun.upper() == 'Y':
            pass
        else:
            run = False
            print("------------------------------")
            print("Thanks for using our program!")