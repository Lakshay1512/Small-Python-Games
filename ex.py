from turtle import Turtle,Screen
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width = 600, height = 600)
my_screen.title("Revision")
my_screen.bgcolor("black")
tim = Turtle('turtle')
tim.color("red")

tim2 = Turtle()

tim2.color('white')
tim2.hideturtle()
tim2.penup()
tim2.goto(0,265)

tim2.write(f"score : {0000000}", align='center',font=('Arial',24,'normal'))
my_screen.update()

my_screen.exitonclick()
