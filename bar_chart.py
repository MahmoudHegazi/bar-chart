import turtle

t = turtle.Turtle()
sales_5_years_precentage = [10, 100, 30, 50, 10]


def word():    
    x = turtle.Turtle()
    x.speed(0)
    x.penup()
    x.forward(80)
    x.right(90)
    x.forward(100)
    x.left(90)
    x.pendown()
    x.left(90)
    x.color("lightblue")
    x.width(5)
    x.right(40)
    x.penup()
    x.back(10)
    x.pendown()
    x.back(10)
    x.forward(10)
    x.left(40)
    x.forward(7)
    x.back(7)
    x.right(40)
    x.back(10)
    x.back(5)
    x.right(20)
    x.back(5)
    x.back(10)
    x.color("white")
    x.forward(5)
    x.color("black")
    x.penup()
    x.left(70)
    x.right(10)
    x.forward(30)
    x.color("lightblue")
    x.back(5)
    x.forward(5)
    x.pendown()
    x.back(10)
    x.right(90)
    x.back(10)
    x.left(90)
    x.forward(10)
    x.back(10)
    x.right(90)
    x.back(10)
    x.left(90)
    x.forward(10)
    x.back(10)
    x.right(90)
    x.back(20)
    x.right(90)
    x.back(5)
    x.left(90)
    x.back(10)
    x.left(90)
    x.back(20)
    x.back(5)
    x.forward(22)
    x.right(90)
    x.left(90)
    x.back(2)
    x.right(90)
    x.forward(5)
    x.color("white")
    x.back(5)
    x.color("lightblue")
    x.right(90)
    x.forward(10)
    x.back(2)
    x.left(90)
    x.right(90)
    x.back(2)
    x.right(90)
    x.back(10)
    x.right(90)
    x.forward(7)
    x.color("black")
    x.left(90)
    x.penup()
    x.forward(50)
    x.right(90)
    x.color("lightgreen")
    x.forward(10)
    x.pendown()
    x.back(10)
    x.right(90)
    x.back(30)
    x.forward(10)
    x.left(90)
    x.forward(10)
    x.penup()
    x.back(30)
    x.forward(10)
    x.width(10)
    x.forward(1)
    x.back(3)
    x.width(20)
    x.forward(2)
    x.pendown()
    x.width(10)
    x.forward(1)
    x.back(2)
    x.right(90)
    x.penup()
    x.back(7)
    x.pendown()
    x.back(2)
    x.color("white")
    x.forward(2)
    x.penup()
    x.back(8)
    x.color("lightgreen")
    x.forward(2)
    x.pendown()
    x.forward(2)
    x.penup()
    x.forward(32)
    x.pendown()
    x.back(2)
    x.penup()
    x.back(30)
    x.left(90)
    x.forward(12)
    x.right(90)
    x.pendown()
    x.forward(5)
    x.color("white")
    x.back(5)
    x.color("lightgreen")
    x.width(5)
    x.forward(30)
    x.back(40)
    x.left(90)
    x.forward(30)
    x.back(30)
    x.right(90)
    x.penup()
    x.back(14)
    x.left(90)
    x.forward(10)
    x.pendown()
    x.back(10)
    x.right(90)
    x.back(20)
    x.left(90)
    x.forward(10)
    x.penup()
    x.back(10)
    x.right(30)
    x.pendown()
    x.back(4)
    x.back(2)
    x.right(5)
    x.back(2)
    x.right(5)
    x.back(4)
    x.right(20)
    x.back(4)
    x.right(5)
    x.back(5)
    x.right(10)
    x.back(4)
    x.right(10)
    x.back(4)
    x.right(10)
    x.back(4)
    x.right(10)
    x.back(2)
    x.right(20)
    x.back(4)
    x.right(10)
    x.back(2)
    x.right(20)
    x.back(2)
    x.right(30)
    x.left(10)
    x.back(12)
    x.penup()
    x.forward(30)
    x.right(10)
    x.left(92)
    x.back(10)
    x.width(10)
    x.pendown()
    x.forward(2)
    x.penup()
    x.forward(17)
    x.pendown()
    x.forward(2)
    x.penup()
    x.left(90)
    x.forward(50)
    x.right(90)
    x.forward(35)
    x.pendown()
    x.forward(2)
    x.penup()
    x.home()
    x.pendown()
    x.ht()


def bot():
    word()
    t.speed(0)
    t.penup()
    t.back(50)
    t.pendown()
    t.width(10)
    t.color("green")
    t.left(90)
    t.forward(200)
    t.width(5)
    t.color("black")
    t.right(40)
    t.back(10)
    t.forward(10)
    t.left(80)
    t.back(10)
    t.forward(10)
    t.right(40)
    t.back(200)
    t.right(90)
    t.width(10)
    t.color("green")
    t.forward(300)
    t.penup()
    t.home()
    t.back(50)
    t.width(7)
    t.pendown()
    t.color("gold")
    t.penup()
    t.forward(50)
    t.pendown()
    for side in sales_5_years_precentage:
        t.left(90)
        t.forward(side)             
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(side)             
        t.left(90)
        t.penup()
        t.forward(30)
        t.pendown()
    t.width(5)
    t.color("black")
    t.right(40)
    t.back(10)
    t.forward(10)
    t.left(40)
    t.left(40)
    t.back(10)
    t.forward(10)
    t.right(40)
    t.back(300)
    t.ht()
    x = input("Do You Want Close App(Y/N)")
    if x == "y":
        return "Thanks"
    else:
        y.home()
        bot()
bot()
