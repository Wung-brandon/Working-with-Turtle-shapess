#aliasing turtle as t
import turtle as t
import random

tim = t.Turtle()

num_sides = 5
#shape for a pentagon
""" for _ in range(num_sides):
    angle = 360/num_sides
    tim.forward(100)
    tim.right(angle) """

colors = ["red", "green", "blue", "yellow", "black", "orange", "purple", "cyan","dark gray", "pink"]
#function to draw multiple different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

#looping through 3 sided to 10 sided shapes   
for shape_side_num in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_num)
    
    