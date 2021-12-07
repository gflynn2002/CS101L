import turtle
import time
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    
    def draw_action(self):
        #Draws a box
        turtle.color(self.color)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class Box_filled(Box):
    def __init__(self, x1, y1, width, height, color, fill_color):
        super().__init__(x1,y1,width,height,color)
        self.fill_color = fill_color
    
    def draw_action(self):
        #Draws a box then fills it in
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    
    def draw_action(self):
        #Draws a circle
        turtle.color(self.color)
        turtle.circle(self.radius)

class Circle_filled(Circle):
    def __init__(self, x1, y1, radius, color, fill_color):
        super().__init__(x1, y1, radius, color)
        self.fill_color = fill_color
    
    def draw_action(self):
        #Draws a circle then fills it in
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


p = Point(-100,100,'blue')
p.draw()

time.sleep(1)


b = Box(100,110,50,40,'red')
b.draw_action()

time.sleep(1)


b = Box_filled(1, 2, 100, 200, "red", "Blue")
b.draw_action()

time.sleep(1)


c = Circle(1,2,100,'red')
c.draw_action()

time.sleep(1)


c = Circle_filled(1,2,50,'blue','red')
c.draw_action()

time.sleep(1)


turtle.mainloop()