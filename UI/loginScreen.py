from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master = None)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Log in Screen")
        self.pack(fill=BOTH, expand = 1)
        
        loginButton = Button(self, text = "Log In", command = self.screen2)
        loginButton.grid(row = 3, column = 1)
        #loginButton.place(x = 10, y = 10)

        Label(self, text = "Username").grid(row = 0)
        usernameEntry = Entry(self)
        usernameEntry.grid(row = 0, column = 1)

        Label(self, text = "Password").grid(row = 1)
        passwordEntry = Entry(self, show = "*")
        passwordEntry.grid(row = 1, column = 1)

    def screen2(self):
        screen2 = Tk()
        self.master.title("screen2")

root = Tk()
root.geometry("800x450")
app = Window(root)
root.mainloop()