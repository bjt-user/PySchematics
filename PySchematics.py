from tkinter import *

ACTIVE = "active"  # tag name for the *active* item

root = Tk()

my_canvas = Canvas(root, width = 500, height = 500, bg = "white")
my_canvas.grid(row = 0, column = 0)

my_canvas.create_line(0, 0, 100, 100, fill = "black")
my_canvas.create_line(200, 200, 220, 150, fill = "blue")

my_object = my_canvas.create_rectangle(50, 150, 250, 50, fill = "red", tag=ACTIVE)  #make it *active*


def left(event):
  my_canvas.move(ACTIVE, -10, 0)
  
def right(event):
  my_canvas.move(ACTIVE, 10, 0)
  
def up(event):
  my_canvas.move(ACTIVE, 0, -10)
  
def down(event):
  my_canvas.move(ACTIVE, 0, 10)
  
def opamp(event):
  my_canvas.dtag(ACTIVE, ACTIVE)  # clear current active tag
  my_canvas.create_rectangle(100, 200, 250, 50, fill = "black", tag = ACTIVE)  #make it *active*
  my_label = Label(root, text = "your mouse is at " + str(event.x) + " " + str(event.y))
  my_label.grid(row = 1, column = 1)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<o>", opamp)

root.mainloop()
