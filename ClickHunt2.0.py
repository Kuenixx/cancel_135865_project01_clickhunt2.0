

# Press Shift+F10 to execute it
from graphics import *
import random
import time

# Este program se trata de dar "click" a los cuadrados verdes intentando evitar los cuadrados rojos y anaranjados.
# Los cuadrados verdes te otorgan un punto, los cuadrados rojos te quitan un punto y los cuadrados anaranjados terminan el juego antes del tiempo.
# El tiempo total es de 60 segundos mientras no se haga "click" a los anaranjados.

# OJO: Este programa es basado en el código de DJeanM en su juego "ClickHunt", por este motivo le puse "ClickHunt2.0".

# Mejoras: El programa fuente se basaba en "click" cuadros verdes por 60 segundos.
# El mayor problema es que podías "click" en cualquier esquina de la pantalla y contaba como punto.
# Otro problema era la falta de aleatoriedad en el desplazamiento de los cuadros(siempre los cuadros aparecian muy cerca del centro).

win = GraphWin("Click Hunt", 600, 600)
win.setBackground("Black")


def main():
    menu()

    # Background Text
    clickSquares = Text(Point(300, 50), "Click the Green Squares!")
    clickSquares.setFill("Green")
    clickSquares.draw(win)
    # Gameplay
    Gameplay()
    # Undraws the background text to showcase Final Score
    clickSquares.undraw()

    win.getMouse()
    win.close()

#Start Menu
def menu():

    startLine = Text(Point(300, 300), "Click Hunt 2.0\nClick to Start!")
    startLine.setFill("Green")
    startLine.draw(win)
    win.getMouse()
    startLine.undraw()


# Gameplay
def Gameplay():
    # Variable to count the amount of squares clicked
    Sum = 0
    # Sets the timer
    Timer = 60
    TimerEnd = time.time() + Timer
    BackTime = Text(Point(300, 100), f"You have {Timer} seconds")
    BackTime.setFill("Green")
    BackTime.draw(win)


    #Starts 60 second loop
    while time.time() < TimerEnd:
        Timer = int(TimerEnd - time.time())
        BackTime.undraw()
        BackTime = Text(Point(300, 100), f"You have {Timer} seconds")
        BackTime.setFill("Green")
        BackTime.draw(win)

        # Draw orange box
        MpositionX = random.randint(50, 550)
        MpositionY = random.randint(100, 550)
        # Check clickable size
        while MpositionX == MpositionY:
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
        Oposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
        OX = Oposition.getP1()
        OY = Oposition.getP2()
        Oposition.setFill(color_rgb(180, 90, 20))
        Oposition.draw(win)

        #Draw red box
        MpositionX = random.randint(50, 550)
        MpositionY = random.randint(100, 550)
        #Check clickable size
        while MpositionX == MpositionY:
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
        Rposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
        RX = Rposition.getP1()
        RY = Rposition.getP2()
        Rposition.setFill(color_rgb(120, 0, 0))
        Rposition.draw(win)



        #Draw green box
        MpositionX = random.randint(50, 550)
        MpositionY = random.randint(100, 550)
        # Check clickable size
        while MpositionX == MpositionY:
            MpositionX = random.randint(50, 550)
            MpositionY = random.randint(100, 550)
        Mposition = Rectangle(Point(MpositionX, MpositionY), Point(MpositionY, MpositionX))
        MX = Mposition.getP1()
        MY = Mposition.getP2()
        Mposition.setFill(color_rgb(0, 120, 0))
        Mposition.draw(win)


        # Green box location
        check = win.getMouse()
        CHECKX1 = check.getX() >= MX.getX()
        CHECKX2 = check.getX() <= MY.getX()
        CHECKY1 = check.getY() >= MX.getY()
        CHECKY2 = check.getY() <= MY.getY()
        CHECKX = CHECKX1 == CHECKX2
        CHECKY = CHECKY1 == CHECKY2

        #Red Box Location
        CHECKRX1 = check.getX() >= RX.getX()
        CHECKRX2 = check.getX() <= RY.getX()
        CHECKRY1 = check.getY() >= RX.getY()
        CHECKRY2 = check.getY() <= RY.getY()
        CHECKRX = CHECKRX1 == CHECKRX2
        CHECKRY = CHECKRY1 == CHECKRY2

        #Orange Box Location
        CHECKOX1 = check.getX() >= OX.getX()
        CHECKOX2 = check.getX() <= OY.getX()
        CHECKOY1 = check.getY() >= OX.getY()
        CHECKOY2 = check.getY() <= OY.getY()
        CHECKOX = CHECKOX1 == CHECKOX2
        CHECKOY = CHECKOY1 == CHECKOY2

        #Variables to loop getMouse
        Sum1 = Sum + 1
        Sum2 = Sum - 1
        # Square Spawner
        while Sum1 != Sum or Sum2 != Sum:

            if (CHECKX == True and CHECKY == True):
                #Score Point
                Sum = Sum + 1
                break
            elif (CHECKRX == True and CHECKRY == True):
                #Score -1 Point
                Sum = Sum - 1
                break
            elif (CHECKOX == True and CHECKOY == True):
                #Gameover
                TimerEnd=0
                break
            else:
                check = win.getMouse()
                #Check Green box location
                CHECKX1 = check.getX() >= MX.getX()
                CHECKX2 = check.getX() <= MY.getX()
                CHECKY1 = check.getY() >= MX.getY()
                CHECKY2 = check.getY() <= MY.getY()
                CHECKX = CHECKX1 == CHECKX2
                CHECKY = CHECKY1 == CHECKY2
                # Check Red box location
                CHECKRX1 = check.getX() >= RX.getX()
                CHECKRX2 = check.getX() <= RY.getX()
                CHECKRY1 = check.getY() >= RX.getY()
                CHECKRY2 = check.getY() <= RY.getY()
                CHECKRX = CHECKRX1 == CHECKRX2
                CHECKRY = CHECKRY1 == CHECKRY2
                # Check Orange box location
                CHECKOX1 = check.getX() >= OX.getX()
                CHECKOX2 = check.getX() <= OY.getX()
                CHECKOY1 = check.getY() >= OX.getY()
                CHECKOY2 = check.getY() <= OY.getY()
                CHECKOX = CHECKOX1 == CHECKOX2
                CHECKOY = CHECKOY1 == CHECKOY2

        # Eliminates the squares
        Mposition.undraw()
        Rposition.undraw()
        Oposition.undraw()

    # Deletes the Text in the Background
    BackTime.undraw()

    # Shows Final Score:
    End = Text(Point(300, 300), f"Final Score:{Sum}")
    End.setFill("Green")
    End.draw(win)


main()

