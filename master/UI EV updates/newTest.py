import random
import csv
from tkinter import *
from dialogwindow import Dialog
from utils import QUESTION_COLUMNS, EXAM_COLUMNS

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
        self.correct_answer = StringVar()


        self.question_entry = Entry(self, textvariable=self.question).grid(row=self.row, column=1)
        self.question_label = Label(self, text="Question:").grid(row=self.row, column=0)
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


class TestForm(Dialog):
    def __init__(self, root):
        self.root = root
        self.questions = []
        self.exam = StringVar()
        self.dueDate = StringVar()
        self.releaseDate = StringVar()
        self.testType = StringVar()

        super().__init__(self.root, "Create new test")

    def body(self, master):

        self.testType.set(None)
        frame = Frame(self.root)
        self.frame = frame

        row = self.row
        Label(self, text="Title").grid(row=row, column=0)
        Entry(self, textvariable=self.exam).grid(row=row, column=1)

        row +=1
        Radiobutton(self, text="Formative", command=self.on_checked, value="formative",
                    variable=self.testType).grid(row=row, column=0)
        Radiobutton(self, text="Summative", command=self.on_checked, value="summative",
                    variable=self.testType).grid(row=row, column=1)

        row += 1
        Label(self, text="Due Date").grid(row=row, column=0)
        Entry(self, textvariable=self.dueDate).grid(row=row, column=1)

        row += 1
        Label(self, text="Release Date").grid(row=row, column=0)
        Entry(self, textvariable=self.releaseDate).grid(row=row, column=1)

        row += 1
        Button(self, text="New multiple choice", command=self.multiple_choice).grid(row=row, column=0)
        Button(self, text="New text answer", command=self.text_answer).grid(row=row, column=1)

        row += 1

        self.row = row


    def multiple_choice(self):
        '''
        Creates a new multiple choice question for the current exam.
        :return:
        '''
        mcq = NewMCQ(self.root)
        try:
            question = {"Answer{0}".format(i + 1):mcq.vars[i].get() for i in range(4)}
            question["Correct"] = int(mcq.answer.get())
            question["QuestionId"] = "q{0}".format(random.randint(1, 1000000))
            question["Question"] = mcq.question.get()
            question["QuestionType"] = "mcq"

            self.questions.append(question)
        except ValueError:
            print("MCQ question is not valid")


    def text_answer(self):
        '''
        Creates a new question with a simple text answer
        '''

        taq = TextAnswerDialog(self.root)
        if taq.applied:
            answer = taq.correct_answer.get()
            question = {"Question": taq.question.get(),
                        "Answer1": answer,
                        "QuestionType": "tax",
                        "Correct": answer }

            question["QuestionId"] = "q{0}".format(random.randint(1, 1000000))

            self.questions.append(question)

    def on_checked(self):
        self.num_attempts = 1
        if(self.testType.get() == 'f'):
            d = NumAttemptsDialog(self.root)
            try :
                self.num_attempts = int(d.attempts_var.get())
            except ValueError:
                print("The user did not enter a value for number of attempts")


    def ok(self, event=None):
        '''
        Over ride the ok event to update the test
        :param event:
        :return:
        '''
        super().ok(event)
        with open("questions.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=QUESTION_COLUMNS, delimiter=',', lineterminator='\n')
            for question in self.questions:
                question["TestType"] = self.testType.get()
                question["TestName"] = self.exam.get()
                writer.writerow(question)

        with open("exams.csv","a") as f:
            writer = csv.DictWriter(f, fieldnames=EXAM_COLUMNS, delimiter=',', lineterminator='\n')
            writer.writerow({"TestName": self.exam.get(), "TestType" : self.testType.get(),
                             "DueDate": self.dueDate.get(), "ResultsRelease": self.releaseDate.get()})

def main():

    root = Tk()
    root.geometry("500x500")
    app = TestForm(root)

    root.mainloop()


if __name__ == '__main__':
    main()
