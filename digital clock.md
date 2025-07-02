import tkinter as tk                #tkinter used to make graphical interface 
from time import strftime           #time modeule : helps to fetch information from time (current time , current day) 
                                    #strftime: function used to forward time as per our wish

root = tk.Tk()                      # window used to display elements(made by tkinter)
root.title("Digital Clock")         # root title : title of window

def time():
    string = strftime('%H:%M:%S %p \n %D')      
    label.config(text=string)                 #method to convert tect into string
    label.after(1000,time)                    #update every second and displa currebt time

label =tk.Label(root , font=('calibri', 50 , 'bold'), background='yellow' , foreground= 'black')  #design of the window

label.pack(anchor='center')                  #method to store the object at the center

time()

root.mainloop()                              # method of tkintercad which keeps the window in a loop