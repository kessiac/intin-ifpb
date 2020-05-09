import tkinter as tk
from two_date import *

name_app = "THE DATE"

class One_date(tk.Tk):
        
        def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                self.img = tk.PhotoImage(file="the date.png")
                self.img = self.img.subsample(4, 4)

                self.background = tk.Label(image=self.img, bd=0)
                self.background.place(x=0, y=0)
                self.background.image = self.img

                self.segundo = Two_date(self)
                self.segundo.place(x=95, y=250)

if __name__ == '__main__':
        prime = One_date()
        prime.title(f"{name_app}")
        prime.resizable(0, 0)
        prime.geometry("397x562")
        prime.iconbitmap("logo.ico")
        prime.mainloop()
