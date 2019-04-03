from tkinter import *
import csv
from dialogwindow import Dialog


class MarksDialog(Dialog):
    '''
    Dialog to display the marks of a test
    '''

    def __init__(self, parent, title, exam, marks):
        self.exam = exam
        self.marks = marks
        super().__init__(parent, title)

    def body(self, master):
        exam = self.exam
        marks = self.marks

        Label(self, text="Exam: ").grid(row=self.row, column=0)
        Label(self, text=exam['TestName']).grid(row=self.row, column=1)
        self.row += 1

        Label(self, text="Exam Type: ").grid(row=self.row, column=0)
        Label(self, text=exam['TestType']).grid(row=self.row, column=1)
        self.row += 1

        if marks:
            scores = [int(mark["Mark"]) for mark in marks]
            highest = max(scores)
            lowest = min(scores)

            if len(marks[0]) == 3:
                Label(self, text="Student Id").grid(row=self.row, column=0)
            else:
                Label(self, text="Attempt").grid(row=self.row, column=0)

            Label(self, text="Marks").grid(row=self.row, column=1)

            self.row += 1
            for i, mark in enumerate(marks):
                if mark.get("StudentId"):
                    Label(self, text="{}".format(mark["StudentId"])).grid(row=self.row, column=0)
                else:
                    Label(self, text="Attempt {0}: ".format(i + 1)).grid(row=self.row, column=0)

                Label(self, text="{}".format(mark["Mark"])).grid(row=self.row, column=1)
                self.row += 1

            if mark.get("StudentId"):
                Label(self, text="Highest score").grid(row=self.row, column=0)
                Label(self, text=str(highest)).grid(row=self.row, column=1)
                self.row += 1
                Label(self, text="Lowest score").grid(row=self.row, column=0)
                Label(self, text=str(lowest)).grid(row=self.row, column=1)


        else:
            Label(self,text="Not Atempted").grid(row=self.row, column=0, columnspan=2)


class MenuScreen():

    def __init__(self):
        questions = []
        self.results = []
        self.exams = []

        self.exams_file = "exams.csv"
        self.results_file = "results.csv"

        # read the questions file
        with open("questions.csv") as f:
            reader = csv.DictReader(f, ["TestName", "TestType", "QuestionType", "QuestionID", "Question", "Answer1", "Answer2", "Answer3", "Answer4", "Answer5"])
            for question in reader:
                questions.append(question)

        self.all_questions = questions

        # read the exame file

        with open(self.exams_file) as f:
            reader = csv.DictReader(f)
            for exam in reader:
                self.exams.append(exam)

        # read the results file.
        with open(self.results_file) as f:
            reader = csv.DictReader(f)
            for result in reader:
                self.results.append(result)

    def get_exam_questions(self, exam):
        questions = []
        exam_name = exam['TestName'].lower()
        for question in self.all_questions:
            q_test_name = question['TestName'].lower().strip()
            if q_test_name == exam_name:
                questions.append(question)

        return questions


    def get_results(self, exam=None, student=None):
        if exam == None and student == None:
            return self.results

        if exam:
            # filtr by exam
            results = []
            exam = exam["TestName"].strip().lower()

            for result in self.results:
                result_for = result["TestName"].strip().lower()
                if result_for == exam:
                    if student:
                        # situation where we want to filter by both the student and the
                        # exam
                        student = student.strip().lower()
                        if result["StudentId"] == student:
                            results.append(result)
                    else:
                        results.append(result)
        else:
            # filter by student
            results = []
            student = student.strip().lower()
            for result in self.results:
                if result["StudentId"] == student:
                    results.append(result)

        return results


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
            self.questions[i]['Selected'] = answer

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
