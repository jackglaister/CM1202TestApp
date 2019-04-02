from tkinter import *


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master=None)

        self.table = Frame(self)
        self.master = master

        self.rows = 0;
        self.pack(padx=20, pady=50)
        self.table.grid(row=0, column=1, columnspan=2)
        frame = Frame()

        with open("Test File.csv") as f:
            self.columns = next(f, None).split(",")

            for i, column in enumerate(self.columns):
                lb = Label(self.table, text=column)
                lb.grid(row=0, column=i, sticky=W)

            for i, line in enumerate(f):
                parts = line.split(",")
                for j, val in enumerate(parts):
                    Label(self.table, text=val, bd=3).grid(row=i+1, column=j, padx=10)

                button = Button(self.table, text="View Marks", command=lambda x=i: self.view_marks(x))
                button.grid(row=i+1, column=j+1, pady = 10, padx = 20)

                button = Button(self.table, text="Edit Test", command=lambda x=i: self.edit_test(x))
                button.grid(row=i + 1, column=j + 2)

            self.rows = i + 1


        logoutButton = Button(self, text="Log Out", command=frame.quit)
        logoutButton.grid(row=1, column=0)

        newTestButton = Button(self, text="Create a new test")
        newTestButton.grid(row=1, column=3, pady=10, padx=25)

    def view_marks(self, x):
        print("take the tet for row ", x)

    def view_test(self, x):
        print("View test", x)


    def edit_test(self, x):
        self.master.title("Main Menu")
        self.pack(fill=NONE, expand=True)


def main():
    root = Tk()
    root.geometry("800x450")
    app = Window(root)

    root.mainloop()

if __name__ == '__main__':
    main()