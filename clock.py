
from tkinter import * 
import time 

canvas = Tk()
canvas.title("Digital clock")
canvas.geometry("300x200")
canvas.resizable(1,1)
label = Label(canvas, font=("Courier", 30 ,'bold'), bg = "blue" , fg = "white" ,bd = 30)
label.grid(row = 0, column = 1)

def clock():
	current_time = time.strftime("%H:%M:%S")
	label.config(text = current_time)
	label.after(200, clock)

clock()
canvas.mainloop()





#print(current_time) works fine. 
#print(current_time)






