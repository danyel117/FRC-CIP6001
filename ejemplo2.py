import turtle
from turtle import Screen, Turtle


global screen
global robot
global square4
screen = Screen()
robot = Turtle('turtle',visible=False)
robot = Turtle('turtle',visible=False)
robot.turtlesize(2,2,1)
robot.color('dark green', 'green')
robot.penup()
robot.goto(-900,300)
#robot.goto(0,-400)
robot.showturtle()
square4 = Turtle('square', visible=False)

def inicial():
    
    screen.setup (width=2000, height=800, startx=0, starty=0)

    square = Turtle('square', visible=False)
    square.turtlesize(20,1,1)
    square.color('grey', 'grey')
    square.penup()
    square.goto(-700, 150)
    
    square3 = Turtle('square', visible=False)
    square3.turtlesize(20,1,1)
    square3.color('grey', 'grey')
    square3.penup()
    square3.goto(0,-150)
    
    square2 = Turtle('square', visible=False)
    square2.turtlesize(20,1,1)
    square2.color('grey', 'grey')
    square2.penup()
    square2.goto(700,150)
    
   
    square4.shapesize(5,5)
    square4.color('blue', 'white')
    square4.penup()
    square4.goto(850, 300)
    
    square.showturtle()
    square2.showturtle()
    square3.showturtle()
    square4.showturtle()

def sensarPared():

    for turt in screen.turtles():
        distancia=40
        tp=turt.position()
        rp=robot.position()
        rh=robot.heading()
        sup=tp[1]+200
        inf=tp[1]-200
        if (turt is not robot and turt is not square4 and tp!=(0,0)) and ((abs(tp[0]-rp[0])<distancia and ((rh==0 and tp[0]>=rp[0]) or (rh==180 and tp[0]<=rp[0])) and (rp[1]<=sup and rp[1]>=inf))):
            #robot.back(1)
            robot.color('red')
            robot.write('        Oh no, nos chocamos!! Haz clic para salir.',move=False,align="left",font=("Arial",10,"bold"))
            screen.exitonclick()
            #return("gris")
        if turt is square4 and abs(rp[0]-tp[0])<distancia+10 and abs(rp[1]-tp[1])<distancia+10:
            robot.write('Excelente, lograste el objetivo! Haz clic para salir.',move=False,align="left",font=("Arial",10,"bold"))
            screen.exitonclick()

def mover(direccion,distancia):
    if direccion=="adelante":
        for i in range (0,distancia):
            robot.forward(1)
            sensarPared()
    if direccion=="derecha":
        robot.right(distancia)
    if direccion=="izquierda":
        robot.left(distancia)
    if direccion=="atras":
        for i in range (0,distancia):
            robot.back(1)
            sensarPared()

inicial()

#Escribir aquí el código---------------------------------------------->
mover("adelante",150)
mover("derecha",90)
mover("adelante",380)
mover("izquierda",90)
mover("adelante",150)
mover("izquierda",90)
mover("adelante",200)
mover("derecha",90)
mover("adelante",1000)
mover("derecha",90)
mover("adelante",300)
mover("izquierda",90)
mover("adelante",450)
mover("izquierda",90)
mover("adelante",500)
#<---------------------------------------------------------------------

turtle.done()