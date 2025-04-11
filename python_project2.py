import pyautogui
from tkinter import*


def take_ss(): 
  add_data = entry.get()
  path = add_data+"\\test.png"
  print(path)
  ss = pyautogui.screenshot()
  ss.save(path)

win = Tk()

win.title("Kesar SS")
win.geometry("650x300")
win.config(bg = "green")
win.resizable(False,False)
  
  #gets the data from entry
entry = Entry(win, font=('Time New Roman',30))
entry.place(x=15, height=50, width=600, y=20)

button = Button(win,text="Done",font=('Time New Roman',50,"bold"), command=take_ss)
button.place(x=150, y=120, height=100, width= 200)



win.mainloop()
 