import turtle
import random
import math

turtle.setup(1000,1000)
turtle.title("Random Walk - PythonTurtle.Academy")
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()

a.color('red')
b.color('green')
c.color('blue')
d.color('orange')
e.color('black')

tlist = []
tlist.append(a)
tlist.append(b)
tlist.append(c)
tlist.append(d)
tlist.append(e)

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
sum = 0
count = 0
for j in range(100):  
    for i in range(10000):
        for t in tlist:
            t.seth(random.randrange(0,360,90))
            t.fd(10)
        turtle.update()
    for t in tlist:
        sum += math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2*math.sqrt(t.xcor()*t.xcor() + t.ycor()*t.ycor())/10*2/100
        count += 1
    for t in tlist:
        t.clear()
        t.up()
        t.goto(0,0)
        t.down()
    print(sum/count)

#20 Random Walkers with List:

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
walkers = list()
n = 20
for i in range(n):
    walkers.append(turtle.Turtle())
for i in range(n):
    walkers[i].color((random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)))
                  
def random_walk():
    for i in range(n):
        angle = random.randint(0,3)*90
        walkers[i].seth(angle)
        walkers[i].fd(10)
    screen.update()
    screen.ontimer(random_walk,1000//20)

random_walk()