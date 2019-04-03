from tkinter import *
import csv
from utils import MenuScreen

class testEditor():
    def __init__(self, exam):
        """
           Test should be passed to the form as a list composed of [title, dueDate, releaseDate, testTyep and questions<list>]
        """
        Test = exam
        root = Tk()
        root.title("Edit Test")
        self.title = StringVar().set(Test[0])
        self.dueDate = StringVar().set(Test[1])
        self.releaseDate = StringVar().set(Test[2])
        self.testType = StringVar().set(Test[3])

        self.frame = Frame(root)
        row = 0
        Label(root, text="Title").grid(row=row, column=0)
        Entry(root, textvariable=self.title).grid(row=row, column=1)
        row = 1
        Label(root, text="dueDate").grid(row=row, column=0)
        Entry(root, textvariable=self.dueDate).grid(row=row, column=1)
        row = 2
        Label(root, text="releaseDate").grid(row=row, column=0)
        Entry(root, textvariable=self.releaseDate).grid(row=row, column=1)
        row = 3
        Radiobutton(root, text="Formative", command=self.on_checked, value="f", variable=self.testType).grid(row=row, column=0)
        Radiobutton(root, text="Summative", command=self.on_checked, value="s", variable=self.testType).grid(row=row, column=1)
        row += 1
        self.submit = Button(root, text="Submit")
        self.submit.grid(row=row, column=0)
        questions=MenuScreen().get_exam_questions(exam[0])
        for i, question in enumerate(questions):
            Label(self, text=question["Question"]).grid(row=self.row, column=0, sticky=W)
            row += 1
            if question["QuestionType"] == "mcq":
                self.answervar[i].set(None)
                for ans in range(1, 5):
                    Radiobutton(root, variable=self.answervar[i],
                                text=question["Answer{}".format(ans)], value=ans).grid(row=row, column=0, sticky=W)
            else:
                Entry(root, textvar=self.answervar[i]).grid(row=row, column=1, sticky=W+E+N+S)
            Button(root, text="edit this", command=self.editQuestion(i, question))
        root.mainloop()

    def on_checked(self):
        self.num_attempts = 1
        if(self.testType.get() == 'f'):
            d = NumAttemptsDialog(self.root)
            try :
                self.num_attempts = int(d.attempts_var.get())
            except ValueError:
                print("The user did not enter a value for number of attempts")


if __name__ == "__main__":
    exams = []
    with open("exams.csv") as f:
        reader = csv.DictReader(f)
        for i, parts in enumerate(reader):
            for j, (key, val) in enumerate(parts.items()):
                exams.append(parts)
    testEditor(MenuScreen().get_exam_questions(exams[0]))
