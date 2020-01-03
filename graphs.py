from tkinter import *
import sys
import os


columns = int(sys.argv[1])	#x
rows = int(sys.argv[2]) 	#y
b = rows
print("line equation is y= ",-rows/columns, "x + ", b) 
print("point({}:0)".format(columns))
print("point(0:{})".format(rows))


print("row = {}\ncolumn = {}".format(rows,columns))

root = Tk()

w = 0
h = 0

#------------------------------------------------------------------------
def redraw(event):
#	print(event.width, " ", event.height)
	canvas.delete('all')	

	w = event.width/columns
	h = event.height/rows

	#create columns
	for i in range(1,columns):
		canvas.create_line(	
			w * i,  0,
			w * i, event.height, 
			fill="white", width = 2
				)

	#create rows
	for i in range(1,rows):
		canvas.create_line(
			0, h*i,
			event.width, h*i,
			fill="white", width=2
				)
	canvas.create_line(0,0,event.width,event.height,fill="white",width=2)
#------------------------------------------------------------------------

canvas = Canvas(root, width = 400, height = 400, background='grey')
canvas.pack(fill = BOTH,expand=1)
#canvas.update()

canvas.bind("<Configure>",redraw)





mainloop()
