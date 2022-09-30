import turtle

class Artist:

    def __init__(self, t):
        self.t = t

    def square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def circle(self, size = 100):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size/100)
            
    def star(self, size = 100):
        for i in range(5):
            self.t.forward(size)
            self.t.right(144)

    def polygon(self, size = 100, sides = 4):
        for i in range (sides):
            self.t.right(360/sides)
            self.t.forward(size)

    def unknow(self,size = 50,angle = 60):
        for i in range(6):
            self.t.forward(200)
            self.t.right(angle)
            
    def idk(self,size = 50):
         for i in range(14):
            self.t.forward(150)
            self.t.right(130)


    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("white")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0.5)
    art = Artist(t)
    art.triangle()
    art.move(100, 200)
    art.star()
    art.move(-200, 200)
    art.circle()
    art.move(-200, 100)
    art.square()
    art.move(200,100)
    art.polygon(50,20)
    art.move(125,125)
    art.unknow()
    art.move(-100,-100)
    art.idk()
    
    


if __name__ == "__main__":
    main()
