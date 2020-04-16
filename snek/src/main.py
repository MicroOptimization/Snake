import tkinter as tk
from tkinter import Canvas, BOTH, W
from snek import Snek
import time
from fruit import Fruit
import random

class Application(tk.Frame):
    
    def __init__(self, snake, fruit, canvas, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = canvas
        self.snek = snake
        self.fruit = fruit

        
        self.pack()
        self.create_drawings()
        
    def create_drawings(self):
        print("Creating drawings...")
        
        self.canvas.bind("<Key>", self.key_listener)
        self.canvas.bind("<Button-1>", self.focuser)
        
        self.canvas.configure(background='#ECECED')
        self.canvas.pack(fill=BOTH, expand=1)
        
    def key_listener(self, event):
        kp = repr(event.char)
        
        if kp == "'w'" and (self.snek.dir != "down" or self.snek.first_link is None):
            self.snek.setDir("up")    
        elif kp == "'s'" and (self.snek.dir != "up" or self.snek.first_link is None):
            self.snek.setDir("down")    
        elif kp == "'a'" and (self.snek.dir != "right" or self.snek.first_link is None):
            self.snek.setDir("left")    
        elif kp == "'d'" and (self.snek.dir != "left" or self.snek.first_link is None):
            self.snek.setDir("right")    
        
    def focuser(self, event):
        self.canvas.focus_set()

root = tk.Tk()

canvas = Canvas(root, width=400, height=400)

fruit = Fruit(canvas)
fruit.spawn()
snake = Snek(fruit, canvas)

app = Application(snake, fruit, canvas, master=root)

def draw_all():
    canvas.delete("all")
    snake.draw()
    fruit.draw()
    cur = snake.first_link 
    while cur is not None:
        cur.draw(canvas)
        cur = cur.next
        
def update_all():
    snake.update()
    
death_messages = ["Happens to the best of us", "Atleast you tried", "Give it another shot", "Whoops", "Try again"]
death_message = death_messages[random.randrange(0, len(death_messages) - 1)]

def finish_game():
    canvas.delete("all")
    canvas.create_text(50, 50, anchor=W, font="Purisa",
                text="You lose! ({})".format(death_message))
    canvas.create_text(50, 100, anchor=W, font="Purisa",
                text="Score: {}".format((snake.count - 1) * 100))
    
    root.update_idletasks()
    root.update()

print()

    
continuing_game = True
while continuing_game:
    root.update_idletasks()
    root.update()
    if snake.is_dead:
        finish_game()
    else:
        update_all()
        draw_all()
        time.sleep(0.1)

 




