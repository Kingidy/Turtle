import turtle    #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400, 400)

polygon = turtle.Turtle()  #defined variable
#variable
polygon.penup()
polygon.goto(0, 100)
num_sides = int(input("Enter the number of sides:"))
side_length = 70
angle = 360.0 / num_sides
polygon.shape('turtle')
polygon.pendown()
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

polygon.hideturtle()
turtle.done()