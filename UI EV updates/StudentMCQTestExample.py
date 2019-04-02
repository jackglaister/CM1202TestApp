from tkinter import *

class Questionnaire(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        createMultipleChoiceQuiz(self)
        self.grid()



def createMultipleChoiceQuiz(self):
    lblTeamExp = Label(self, text="Questions:", font=('MS', 14,'bold'))
    lblTeamExp.grid(row=4, column=0, columnspan=2, sticky=NE)
    lblExp1 = Label(self, text="1. In what year was python first released?                            A: 1999  B: 2000   C: 2001  D: 2002  ", font=('MS', 14))
    lblExp1.grid(row=5, column=0, columnspan=4, sticky=W)
    lblExp2 = Label(self, text="2. How many unique representations can 8 bits make?       A: 150   B: 256     C: 8      D: 1250.   ", font=('MS', 14))
    lblExp2.grid(row=6, column=0, columnspan=4, sticky=W)
    lblExp3 = Label(self, text="3. In what year was java released?                                        A: 1990   B: 2009   C: 1959  D: 1972.   ", font=('MS', 14))
    lblExp3.grid(row=7, column=0, columnspan=4, sticky=W)
    lblExp3 = Label(self, text="4. Are we going to pass DQS ?                                             A: Yes   B: No   C: Maybe  D: Please.   ", font=('MS', 14))
    lblExp3.grid(row=8, column=0, columnspan=4, sticky=W)
    self.varQ1 = IntVar()
    self.varQ2 = IntVar()
    self.varQ3 = IntVar()
    self.varQ4 = IntVar()

    lblStrAgr = Label(self, text = 'A', font=('MS', 10,'bold'))
    lblStrAgr.grid(row=3, column= 4, rowspan=2)
    R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
    R1Q1.grid(row=5, column=4)
    R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
    R1Q2.grid(row=6, column=4)
    R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
    R1Q3.grid(row=7, column=4)
    R1Q4 = Radiobutton(self, variable=self.varQ4, value=4)
    R1Q4.grid(row=8, column=4)

    lblStrAgr = Label(self, text = 'B', font=('MS', 10,'bold'))
    lblStrAgr.grid(row=3, column= 5, rowspan=2)
    R2Q1 = Radiobutton(self, variable=self.varQ1, value=3)
    R2Q1.grid(row=5, column=5)
    R2Q2 = Radiobutton(self, variable=self.varQ2, value=3)
    R2Q2.grid(row=6, column=5)
    R2Q3 = Radiobutton(self, variable=self.varQ3, value=3)
    R2Q3.grid(row=7, column=5)
    R2Q4 = Radiobutton(self, variable=self.varQ4, value=3)
    R2Q4.grid(row=8, column=5)

    lblStrAgr = Label(self, text = 'C', font=('MS', 10,'bold'))
    lblStrAgr.grid(row=3, column= 6, rowspan=2)
    R3Q1 = Radiobutton(self, variable=self.varQ1, value=2)
    R3Q1.grid(row=5, column=6)
    R3Q2 = Radiobutton(self, variable=self.varQ2, value=2)
    R3Q2.grid(row=6, column=6)
    R3Q3 = Radiobutton(self, variable=self.varQ3, value=2)
    R3Q3.grid(row=7, column=6)
    R3Q4 = Radiobutton(self, variable=self.varQ4, value=2)
    R3Q4.grid(row=8, column=6)

    lblStrAgr = Label(self, text = 'D', font=('MS', 10,'bold'))
    lblStrAgr.grid(row=3, column= 7, rowspan=2)
    R4Q1 = Radiobutton(self, variable=self.varQ1, value=1)
    R4Q1.grid(row=5, column=7)
    R4Q2 = Radiobutton(self, variable=self.varQ2, value=1)
    R4Q2.grid(row=6, column=7)
    R4Q3 = Radiobutton(self, variable=self.varQ3, value=1)
    R4Q3.grid(row=7, column=7)
    R4Q4 = Radiobutton(self, variable=self.varQ4, value=1)
    R4Q4.grid(row=8, column=7)
    

    Button(root, text='Submit Test', command=root.quit).grid(row=9, column=9, sticky=W, pady=4)


root = Tk()
root.geometry("1080x600+150+150")
root.title("MULTIPLE CHOICE QUESTION QUIZ")
app = Questionnaire(root)
root.mainloop()
