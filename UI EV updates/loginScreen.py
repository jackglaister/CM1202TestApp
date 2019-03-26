from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Log in Screen")
        self.pack(fill=NONE, expand=True)

        loginButton = Button(self, text="Log In", command=self.screen2)
        loginButton.grid(row=3, column=1)

        # loginButton.place(x =/'; 10, y = 10)

        Label(self, text="Username").grid(row=0)
        usernameEntry = Entry(self)
        usernameEntry.grid(row=0, column=1)
        usernameEntry.config(background="lightblue")

        Label(self, text="Password").grid(row=1)
        passwordEntry = Entry(self, show="*")
        passwordEntry.grid(row=1, column=1)

        passwordEntry.config(background="lightblue")
    def screen2(self):
        screen2 = Tk()
        self.master.title("screen2")


if __name__ == '__main__':
    root = Tk()
    height = 300
    width = 400
    ww = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    root.geometry("{0}x{1}+{2}+{3}".format(width, height,
                                           (ww-width)//2, (wh - height)//2))
    app = Window(root)

    root.mainloop()