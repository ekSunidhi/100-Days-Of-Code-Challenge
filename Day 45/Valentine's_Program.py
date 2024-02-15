import turtle

def draw_heart():
    turtle.speed(2)
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    
    turtle.end_fill()
    turtle.hideturtle()

def write_message():
    turtle.penup()
    turtle.goto(0, -180)
    turtle.color("black")
    turtle.write("Happy Valentine's Day!", align="center", font=("Arial", 16, "normal"))

if __name__ == "__main__":
    turtle.title("Valentine's Day")
    turtle.bgcolor("lightpink")
    
    draw_heart()
    write_message()

    turtle.done()
