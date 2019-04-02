from tkinter import *


def login():
    global login_screen
    login_screen = Tk()
    height = 300
    width = 400
    ww = login_screen.winfo_screenwidth()
    wh = login_screen.winfo_screenheight()

    login_screen.geometry("{0}x{1}+{2}+{3}".format(width, height,
                                           (ww - width) // 2, (wh - height) // 2))

    login_screen.title("Account Login")

    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

    login_screen.mainloop()  # start the GUI


def login_verify():
    username = username_verify.get()
    password = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    with open("users.csv") as f:
        data = f.readlines()

        uname = data[0].strip()
        pword = data[1].strip()

        if username == uname and password == pword:
            login_sucess()
        else:
            user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)

    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found. Try again").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

login()