from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master = None)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Main Menu")
        self.pack(fill=BOTH, expand = 1)

        logoutButton = Button(self, text = "Log Out")
        logoutButton.place(x = 740, y = 10)

        


root = Tk()
root.geometry("800x450")
app = Window(root)
root.mainloop()