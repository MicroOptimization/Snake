from tail_link import Tail_Link

class Snek:
    
    def __init__(self, fruit, canvas):
        print("Making snek")
        self.x = 100
        self.y = 20
        self.dim = 20
        self.dir = "down"
        self.move_increment = 20
        self.count = 1
        self.fruit = fruit
        self.first_link = None
        self.last_link = None
        self.canvas = canvas
        self.is_dead = False
        
    def update(self):
        if self.x >= 400 and (self.dir != "up" and self.dir != "down"): 
            self.x = 0
        elif self.x <= 0 and (self.dir != "up" and self.dir != "down"):
            self.x = 400
        
        if self.y >= 400 and (self.dir != "left" and self.dir != "right"): 
            self.y = 0
        elif self.y <= 0 and (self.dir != "left" and self.dir != "right"):
            self.y = 400
        
        if self.first_link is not None:
            cur = self.last_link 
            
            while cur.prev is not None:
                if cur.x == self.x and cur.y == self.y:
                    self.die()    
                cur.x = cur.prev.x
                cur.y = cur.prev.y
                
                cur = cur.prev
            
            self.first_link.x = self.x
            self.first_link.y = self.y

        if self.fruit.x == self.x and self.fruit.y == self.y:
            self.fruit.spawn()
            self.count += 1
            print("fruit acquired \nCount: " , self.count)
            self.increase_size()
            print()
            
        if self.dir == "up":
            self.setY(self.y - self.move_increment)
        elif self.dir == "down":
            self.setY(self.y + self.move_increment)
        elif self.dir == "right":
            self.setX(self.x + self.move_increment)
        elif self.dir == "left":
            self.setX(self.x - self.move_increment)
        
    def increase_size(self):
        print("increasing size")
        next_x = self.x
        next_y = self.y
        
        if self.count == 2:
            new_link = Tail_Link(None, None, next_x, next_y)
            self.first_link = new_link
            self.last_link = new_link
            self.first_link.dir = self.dir
        else:
            new_link = Tail_Link(self.last_link, None, next_x, next_y)
            self.last_link.next = new_link
            
            self.last_link.next.dir = self.last_link.dir
            self.last_link = new_link
            
    def draw(self):
        x = self.x
        y = self.y
        dim = self.dim
        
        self.canvas.create_rectangle(x, y, x + dim, y + dim, fill='#8B7248')
        
        next_link = self.first_link
        while next_link is not None:
            x = next_link.x
            y = next_link.y
            self.canvas.create_rectangle(x, y, x + dim, y + dim, fill='#8B7248')
            next_link = next_link.next
            
    def die(self):
        self.is_dead = True
        
    def setX(self, newX):
        self.x = newX
        
    def setY(self, newY):
        self.y = newY
    
    def setDir(self, new_dir):
        self.dir = new_dir
        