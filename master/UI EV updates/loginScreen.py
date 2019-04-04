from tkinter import *
import lecturerMenuScreen, studentMenuScreen

class Login():
    def __init__(self):
        self.users = []

        with open("users.csv") as f:
            for line in f:
                data = line.split(",")
                self.users.append(data)

        login_screen = Tk()
        self.login_screen = login_screen

        height = 300
        width = 400
        ww = login_screen.winfo_screenwidth()
        wh = login_screen.winfo_screenheight()

        login_screen.geometry("{0}x{1}+{2}+{3}".format(width, height,
                                               (ww - width) // 2, (wh - height) // 2))

        login_screen.title("Account Login")

        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(login_screen, text="Username * ").pack()
        self.username_login_entry = Entry(login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        Label(self.login_screen, text="").pack()
        Label(self.login_screen, text="Password * ").pack()

        self.password_login_entry = Entry(login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()


    def login_verify(self):
        username = self.username_verify.get()
        password = self.password_verify.get()
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        for user in self.users:
            if username == user[0]:
                if password == user[1]:
                    self.login_success(user)
                    return

        self.user_not_found()

    def login_success(self, user):

        self.login_screen.withdraw()
        self.login_screen.destroy()
        if user[2] == 'lecturer':
            lecturerMenuScreen.main()
        else:
            studentMenuScreen.main(user[0])

    def user_not_found(self):

        user_not_found_screen = Toplevel(self.login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found. Try again").pack()
        Button(user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

        self.user_not_found_screen = user_not_found_screen

    def delete_login_success(self):
        self.login_success_screen.destroy()

    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()


if __name__ == '__main__':
    login = Login()
    login.login_screen.mainloop()  # start the GUI
