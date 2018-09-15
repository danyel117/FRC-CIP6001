import turtle

global robot
robot = turtle.Turtle('turtle',visible=False)
def mover(direccion,distancia):
    if direccion=="adelante":
        robot.forward(distancia)
    if direccion=="derecha":
        robot.right(distancia)
    if direccion=="izquierda":
        robot.left(distancia)
    if direccion=="atras":
        robot.back(distancia)


for i in range(180):
    mover("adelante",180)
    mover("derecha",30)
    mover("adelante",20)
    mover("izquierda",60)
    mover("adelante",50)
    mover("derecha",30)
    robot.penup()
    robot.setposition(0,0)
    robot.pendown()
    mover("derecha",2)
    


turtle.done()
