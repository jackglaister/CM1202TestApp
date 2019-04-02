from tkinter import *



class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master=None)


        self.table = Frame(self)
        self.master = master
        self.init_window()
        self.rows = 0;
        self.table.grid(row=0, column=1, columnspan=2)

        frame = Frame(bg="lightblue")

        with open("Test File Example.csv") as f:
            self.columns = next(f, None).split(",")

            for i, column in enumerate(self.columns):
                lb = Label(self.table, text=column)
                lb.grid(row=0, column=i, sticky=W)



            for i, line in enumerate(f):
                parts = line.split(",")
                for j, val in enumerate(parts):
                    Label(self.table, text=val).grid(row=i+1, column=j, padx=1)

                button = Button(self.table, text="Take Test", command=lambda x=i: self.take_test(x))
                button.grid(row=i+1, column=j+1,  pady = 10, padx = 20)

                button = Button(self.table, text="View Marks", command=lambda x=i: self.view_marks(x))
                button.grid(row=i + 1, column=j + 2)

            self.rows = i + 1

        logoutButton = Button(self, text="Log Out", command=frame.quit)
        logoutButton.grid(row=1, column=0)





    def take_test(self, x):
        print("Take the test for row ", x)

    def view_marks(self, x):
        print("View marks for row", x)


    def init_window(self):
        self.master.title("Main Menu")
        self.pack(fill=NONE, expand=True)



def main():

    root = Tk()
    root.geometry("800x450")
    app = Window(root)
    root.mainloop()



if __name__ == '__main__':
    main()
