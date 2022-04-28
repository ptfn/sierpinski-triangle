from PIL import Image, ImageColor
from PIL import ImageDraw
import random
import time


class Point():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def paint(self, draw):
        draw.point((self.x, self.y), fill=ImageColor.getrgb(self.color))


class Triangle():
    def __init__(self):
        self.width = 3000
        self.height = 3000
        self.image = Image.new("RGB", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
  
    def rendering(self):
        a = Point(random.randrange(0, self.height), random.randrange(0, self.width), "green")
        a.paint(self.draw)
        
        b = Point(random.randrange(0, self.height), random.randrange(0, self.width), "green")
        b.paint(self.draw)
        
        c = Point(random.randrange(0, self.height), random.randrange(0, self.width), "green")
        c.paint(self.draw)

        first = Point(random.randrange(50, self.height), random.randrange(50, self.width), "red")
        first.paint(self.draw)

        def calcPoint(p1:Point, p2:Point):
            x = (p1.x + p2.x) / 2
            y = (p1.y + p2.y) / 2
            
            return Point(x,y,"blue")

        i = 0
        num = 1000000

        while i < num:
            random_dot = random.randrange(0,3000)
          
            if random_dot >= 0 and random_dot < 1000:
                newp = calcPoint(p1 = a, p2 = first)
                first = newp
            
            elif random_dot >= 1000 and random_dot < 2000:
                newp = calcPoint(p1 = b, p2 = first)
                first = newp
            
            elif random_dot >= 2000 and random_dot <= 3000:
                newp = calcPoint(p1 = c, p2 = first)
                first = newp
            
            newp.paint(self.draw)
            first = newp
            i += 1
            time.sleep(0.00001)

        self.image.save("save.png", "PNG")


def main():
    start = Triangle()
    start.rendering()
 
if __name__ == '__main__':
    main()