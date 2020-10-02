#Importing turtle package
import turtle
#Creating a turtle object (pen)
pen = turtle.Turtle()
#Defining a function to draw a curve
def curve():
    for i in range (200):
        #Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
#Defining method to draw a full heart 
def heart():
    #Set the fill color to red
    pen.fillcolor('red')
    #Start filling the color
    pen.begin_fill()
    #Draw left line
    pen.left(140)
    pen.forward(113)
    #Draw left curve
    curve()
    pen.left(120)
    #Draw right curve
    curve()
    #Draw right line
    pen.forward(112)
    #Ending the filling of the color
    pen.end_fill()
    #Defining function to write text in it 
def txt():
    #Move turtle to the air
    pen.up()
    #Move turtle to a given position
    pen.setpos(-68, 95)
    #Move turtle to the ground
    pen.down()
    #Set the text color to black
    pen.color('black')
    #Write specified text you want to show
    #Specify the font style and size
    pen.write("It's just me and you ", font=("Verdana",12, "bold"))

#Draw a heart    
heart()
#Write text
txt()
#To hide turtle
pen.ht()



