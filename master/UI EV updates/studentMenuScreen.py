from tkinter import *
import csv
from dialogwindow import Dialog
from utils import MenuScreen, TakeTest


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
            for i, mark in enumerate(marks):
                Label(self, text="Attempt {0}: ".format(i + 1)).grid(row=self.row, column=0)
                Label(self, text="{}".format(mark["Mark"])).grid(row=self.row, column=1)
                self.row +=1
        else:
            Label(self,text="Not Atempted").grid(row=self.row, column=0, columnspan=2)



class StudentWindow(MenuScreen):
    def __init__(self, root, user):
        super().__init__()
        self.root = root
        self.user = user

        self.columns = ["Test Name", "Test Type", "Test Due", "Results Released"]

        self.table = Frame(self.root)
        self.rows = 0;
        self.table.grid(row=0, column=1, columnspan=2)

        frame = Frame(bg="lightblue")

        self.load_student_data()
        logoutButton = Button(self.root, text="Log Out", command=frame.quit)
        logoutButton.grid(row=1, column=0)

    def load_student_data(self):
        '''
        Reads the results and the exams

        Only the exams taken by this student is considered when reading the result.
        The results and the exams can be joined using the TestName field which is
        there in both the dataset
        :return:
        '''
        for i, column in enumerate(self.columns):
            lb = Label(self.table, text=column)
            lb.grid(row=0, column=i, sticky=W)

        with open(self.results_file) as f:
            reader = csv.DictReader(f)
            for line in reader:
                if line['StudentId'] == self.user:
                    self.results.append(line)

        for i, parts in enumerate(self.exams):

            for j, (key, val) in enumerate(parts.items()):
                Label(self.table, text=val).grid(row=i+1, column=j, padx=1)

            button = Button(self.table, text="Take Test", command=lambda x=i: self.take_test(x))
            button.grid(row=i+1, column=j+1,  pady = 10, padx = 20)

            if parts["ResultsRelease"]:
                state = "normal"
            else:
                state = DISABLED

            button = Button(self.table, text="View Marks", state=state,
                            command=lambda x=i: self.view_marks(x))
            button.grid(row=i + 1, column=j + 2)



        self.rows = i + 1

    def take_test(self, x):
        '''

        :param x: The row number for the test
        :return:
        '''
        exam = self.exams[x]

        questions = self.get_exam_questions(exam)
        q = questions[:]
        t = TakeTest(self.root, exam["TestName"], exam, q)

        marks = 0

        with open("test_answers.csv", "a") as f:
            fields = ["StudentId","QuestionId","Answer","Correct"]
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=',', lineterminator='\n')
            #writer.writeheader()
            for i, question in enumerate(q):
                answer = t.answervar[i].get()
                correct = answer.strip().lower() == question["Correct"].strip().lower()
                result = {"StudentId":  self.user, "QuestionId": question["QuestionId"],
                          "Answer": answer, "Correct": correct}

                if correct:
                    marks += 1

                # the checking answer part comes here as described below
                writer.writerow(result)

        # write the summary to the results.csv file at the end of the file
        summary = [self.user, exam["TestName"], marks]
        with open("results.csv", "a") as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(summary)

    def view_marks(self, x):
        '''
        view the marks for an exam

        :param x:
        :return:
        '''
        exam = self.exams[x]
        results = self.get_results(exam, self.user)
        marks = []

        for result in results:
            marks.append(result)

        di = MarksDialog(self.root, "Exam marks", exam, marks)


    def init_window(self):
        self.root.title("Main Menu")
        #self.pack(fill=NONE, expand=True)



def main(user):

    root = Tk()
    root.geometry("600x300")
    app = StudentWindow(root, user)
    root.mainloop()

if __name__ == '__main__':
    main(user="c10002")
