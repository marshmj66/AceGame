import turtle
import random
import time

class Board:
    def __init__(self,color):
        self.screen = turtle.Screen()
        self.screen.setup(750, 700)
        self.turts = []
        self.specturm = ['red','blue','green','yellow']

        self.leading = turtle.Turtle()
        self.leading.hideturtle()

        self.score_line = turtle.Turtle()
        self.score_line.hideturtle()

        self.width = turtle.screensize()[0]
        self.height = turtle.screensize()[1]
        self.draw_score_line()
        #self.player.left(90)

        print(self.width,self.height)

    def draw_score_line(self):
        self.score_line.penup()
        self.score_line.setx(-self.width + 40)
        self.score_line.sety(-self.height + 40)
        self.score_line.pendown()
        self.score_line.forward(self.height + self.height - 40)
        self.score_line.penup()
        self.score_line.setx(-self.width + 40)
        self.score_line.sety(-self.height + 40)
        self.score_line.left(90)
        self.score_line.pendown()
        self.score_line.forward(self.height + self.height - 40)
        self.score_line.write('Winner', font=('Arial', 18, 'italic'))

    def start_position(self):

        red = turtle.Turtle(shape='turtle')
        red.hideturtle()
        blue = turtle.Turtle(shape='turtle')
        blue.hideturtle()
        green = turtle.Turtle(shape='turtle')
        green.hideturtle()
        yellow = turtle.Turtle(shape='turtle')
        yellow.hideturtle()
        self.turts = [red,blue,green,yellow]
        count = 0
        place = 100
        for t in self.turts:
            t.color(self.specturm[count])
            t.hideturtle()
            count += 1
            t.penup()
            t.setx(-self.width+place)
            t.sety(-self.height)
            t.left(90)
            t.turtlesize(3,3)
            t.speed(1)
            t.showturtle()
            place += 150
    def display_lead(self,current):
        lead = ''
        count = 0
        for t in self.turts:
            if current.pos()[1] > t.pos()[1]:
                count += 1
        if count == 3:
            self.leading.clear()
            self.leading.penup()
            self.leading.setx(400)
            self.leading.sety(0)
            self.leading.write(current.color()[1])

    def move_turtles(self,*args):
        while True:
            player = random.randint(0, 3)
            move = random.randint(50, 100)
            if self.turts[player].pos()[1] >= 300.00:
                return self.turts[player]

            self.turts[player].forward(move)
            self.display_lead(self.turts[player])
            time.sleep(2)
    def close_window(self):
        self.screen.bye()

