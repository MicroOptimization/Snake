import random

class Fruit:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 50
        self.y = 50
        self.dim = 20
        
    def spawn(self):
        self.x = 20 * random.randrange(1, 20)
        self.y = 20 * random.randrange(1, 20)

        print("New fruit spawned at ({}, {})".format(self.x, self.y))
    
    def draw(self):
        x = self.x
        y = self.y
        dim = self.dim
        
        self.canvas.create_rectangle(x, y, x + dim, y + dim, fill='#7C0907')
        