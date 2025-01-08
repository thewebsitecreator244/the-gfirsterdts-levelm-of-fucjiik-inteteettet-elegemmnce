import tkinter
print("to draw, hold down the left mouse button and move your mouse around")
print("to change your brush colours, click on one of your colours")
window = tkinter.Tk()
canvas =  tkinter.Canvas(window, width=750, height=500, bg="white")
canvas.pack
lastX, lastY = 0,0
colour = " black"
def store_positon(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
 def on_click(event):
     store_positon(event)
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width = 3)
store_positon()
canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)




def set_colour_red(event):
    global colour
    colour = ("red")
def set_colour_blue(event):
    global colour
    colour = "blue"
def set_colour_black(event):
    global colour
    colour = "black"
def set_colour_black(event):
    global colour
    colour  = ("black")
canvas.tag_bind()















