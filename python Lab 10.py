##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# 70pt:roof and house                               100pt: red house
rectangle = drawpad.create_rectangle(200,600,600,200, fill='red')
line = drawpad.create_line(200,200,400,100)
line = drawpad.create_line(600,200,400,100)
#80pt: windows and door
rectangle = drawpad.create_rectangle(250,300,300,250)
rectangle = drawpad.create_rectangle(550,300,500,250)
rectangle = drawpad.create_rectangle(250,500,300,550)
rectangle = drawpad.create_rectangle(550,500,500,550)
rectangle = drawpad.create_rectangle(350,600,450,500)

#90pt: handle and chimney
oval = drawpad.create_oval(425,575,450,550)
line = drawpad.create_line(200,200,200,100)
line = drawpad.create_line(200,100,250,100)
line = drawpad.create_line(250,100,250,180)

#100pt: green grass
rectangle = drawpad.create_rectangle(200,500,0,600, fill ='green')
rectangle = drawpad.create_rectangle(600,500,800,600, fill ='green')
root.mainloop()

