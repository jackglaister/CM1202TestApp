from tkinter import *
import csv
from dialogwindow import Dialog

class MenuScreen():

    def __init__(self):
        questions = []

        with open("questions.csv") as f:
            reader = csv.DictReader(f, ["TestName", "TestType", "QuestionType", "QuestionID", "Question", "Answer1", "Answer2", "Answer3", "Answer4", "Answer5"])
            for question in reader:
                questions.append(question)

        self.all_questions = questions

    def get_exam_questions(self, exam):
        questions = []
        exam_name = exam['TestName'].lower()
        for question in self.all_questions:
            print(question)
            q_test_name = question['TestName'].lower().strip()
            if q_test_name == exam_name:
                questions.append(question)

        return questions

class TakeTest(Dialog):
    """
    Dialog to display the test which needs to be taken by the student

    """
    def __init__(self, parent, title, exam, questions):
        self.exam = exam
        self.questions = questions
        self.answervar = [StringVar() for x in range(len(questions))]

        super().__init__(parent, title)

    def ok(self, event=None):
        '''
        Over ride the ok event to update the test
        :param event:
        :return:
        '''
        super().ok(event)

        for i in range(len(self.questions)):
            answer = self.answervar[i].get()
            self.questions[i]['Correct'] = answer

    def body(self, master):
        exam = self.exam
        questions = self.questions
        self.row = 0

        Label(self, text="Exam: ").grid(row=self.row, column=0, sticky=W)
        Label(self, text=exam['TestName']).grid(row=self.row, column=1, sticky=W)
        self.row += 1

        Label(self, text="Exam Type: ").grid(row=self.row, column=0, sticky=W)
        Label(self, text=exam['TestType']).grid(row=self.row, column=1, sticky=W)
        self.row += 1

        for i, question in enumerate(questions):
            Label(self, text=question["Question"]).grid(row=self.row, column=0, sticky=W)
            self.row += 1

            if question["QuestionType"] == "mcq":
                self.answervar[i].set(None)
                for ans in range(1, 5):
                    Radiobutton(self, variable=self.answervar[i],
                                text=question["Answer{}".format(ans)], value=ans).grid(row=self.row, column=0, sticky=W)

                    self.row += 1
            else:
                Entry(self, textvar=self.answervar[i]).grid(row=self.row, column=1, sticky=W+E+N+S)
                self.row += 1
