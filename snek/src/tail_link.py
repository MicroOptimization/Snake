class Tail_Link:
    
    def __init__(self, prev, next, x, y):
        self.next = next
        self.prev = prev
        self.direction = None
        self.x = x
        self.y = y
        self.move_increment = 20
        self.dim = 20
        
    def draw(self, canvas):
        x = self.x
        y = self.y
        dim = self.dim
        
        canvas.create_rectangle(x, y, x + dim, y + dim, fill='#8B7248')
        
    def update(self):
        if self.x >= 400 and self.dir != "up": 
            self.x = 0
        elif self.x <= 0 and self.dir != "up":
            self.x = 400
        if self.y >= 400 and self.dir != "right": 
            self.y = 0
        elif self.y <= 0 and self.dir != "right":
            self.y = 400
            
    def setX(self, newX):
        self.x = newX
        
    def setY(self, newY):
        self.y = newY
    
    def setDir(self, new_dir):
        self.dir = new_dir