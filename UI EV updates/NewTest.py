from tkinter import *
from dialogwindow import Dialog


class NumAttemptsDialog(Dialog):
    '''
    Dialog to ask the number of attempts
    '''
    def body(self, master):
        self.row = 0
        self.attempts_var = StringVar()
        self.attempts_entry = Entry(self, textvariable=self.attempts_var)
        self.attempts_label = Label(self, text="The number of attempts allowed")

        self.attempts_label.grid(row=self.row , column=0)
        self.attempts_entry.grid(row=self.row , column=1)


class TextAnswerDialog(Dialog):
    '''
    Dialog fo the text-answer questions
    '''
    def body(self, master):
        self.row = 0
        self.row += 1

        self.question = StringVar()
        self.answer = StringVar()
        self.correct_answer = StringVar()


        self.question_entry = Entry(self, textvariable=self.question).grid(row=self.row, column=1)
        self.question_label = Label(self, text="Question:").grid(row=self.row, column=0)
        self.row += 1


        self.answer_entry = Entry(self, textvariable=self.answer).grid(row=self.row, column=1)
        self.answer_label = Label(self, text="Answer").grid(row=self.row, column=0)
        self.row += 1


        self.correct_answer_entry = Entry(self, textvariable=self.correct_answer).grid(row=self.row, column=1)
        self.correct_answer_label = Label(self, text="Correct answer").grid(row=self.row, column=0)
        self.row += 1


class NewMCQ(Dialog):
    '''
    Dialog fo the multiple-choice answer questions
    '''

    def body(self, master):
        self.vars = [StringVar(), StringVar(), StringVar(), StringVar()]
        self.labels = ["1", "2","3", "4"]
        self.question = StringVar()
        self.answer = StringVar()

        Label(self, text="The question").grid(row=self.row, column=0)
        Entry(self,  textvariable=self.question).grid(row=self.row, column=1)

        self.row += 1
        for i in range(len(self.labels)):
            Label(self, text=self.labels[i]).grid(row=self.row, column=0)
            Entry(self, textvariable=self.vars[i]).grid(row=self.row, column=1)

            self.row += 1

        Label(self, text="Correct answer").grid(row=self.row, column=0)
        Entry(self, textvariable=self.answer).grid(row=self.row, column=1)


class TestForm():
    def __init__(self, root):
        self.root = root
        root.wm_title("Create New Test")
        self.title = StringVar()
        self.dueDate = StringVar()
        self.releaseDate = StringVar()
        self.testType = StringVar()

        self.testType.set(None)
        frame = Frame(self.root)
        self.frame = frame

        row = 0
        Label(root, text="Title").grid(row=row, column=0)
        Entry(root, textvariable=self.title).grid(row=row, column=1)

        row +=1
        Radiobutton(root, text="Formative", command=self.on_checked, value="f",
                    variable=self.testType).grid(row=row, column=0)
        Radiobutton(root, text="Summative", command=self.on_checked, value="s",
                    variable=self.testType).grid(row=row, column=1)

        row += 1
        Label(root, text="Due Date").grid(row=row, column=0)
        Entry(root, textvariable=self.dueDate).grid(row=row, column=1)

        row += 1
        Label(root, text="Release Date").grid(row=row, column=0)
        Entry(root, textvariable=self.releaseDate).grid(row=row, column=1)

        row += 1
        Button(root, text="New multiple choice", command=self.multiple_choice).grid(row=row, column=0)
        Button(root, text="New text answer", command=self.text_answer).grid(row=row, column=1)

        row += 1
        self.submit = Button(root, text="Submit")
        self.submit.grid(row=row, column=0)


    def multiple_choice(self):
        print("Multiple")
        mcq = NewMCQ(self.root)
        print("MCQ dialog closed", mcq.question.get())
        # typically the code to save to a database or file would be here.
        for i in range(len(mcq.labels)):
            print("Choice ", i + 1, mcq.vars[i].get())

        print("correect answer is", mcq.answer.get())

    def text_answer(self):
        print("Text question")
        taq = TextAnswerDialog(self.root)
        print("TextAnswerDialog closed", taq.question.get())

        print("Space for the answer:", taq.answer.get())

        # pop up a dialog for a text answer

    def on_checked(self):
        self.num_attempts = 1
        if(self.testType.get() == 'f'):
            d = NumAttemptsDialog(self.root)
            try :
                self.num_attempts = int(d.attempts_var.get())
            except ValueError:
                print("The user did not enter a value for number of attempts")




def main():

    root = Tk()
    root.geometry("500x500")
    app = TestForm(root)

    root.mainloop()


if __name__ == '__main__':
    main()
