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

        for i, mark in enumerate(marks):
            Label(self, text="Attempt {0}: ".format(i + 1)).grid(row=self.row, column=0)
            Label(self, text="{}".format(mark["Mark"])).grid(row=self.row, column=1)
            self.row +=1




class StudentWindow(MenuScreen):
    def __init__(self, root, user):
        super().__init__()
        self.root = root
        self.user = user

        self.columns = ["Test Name","Test Type","", "Marks", "Attempts"]

        self.results = []
        self.exams = []

        self.table = Frame(self.root)
        self.rows = 0;
        self.table.grid(row=0, column=1, columnspan=2)

        self.exams_file = "exams.csv"
        self.results_file = "results.csv"

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
                if line['StudentID'] == self.user:
                    self.results.append(line)

        with open(self.exams_file) as f:
            reader = csv.DictReader(f)
            for i, parts in enumerate(reader):

                for j, (key, val) in enumerate(parts.items()):
                    Label(self.table, text=val).grid(row=i+1, column=j, padx=1)

                button = Button(self.table, text="Take Test", command=lambda x=i: self.take_test(x))
                button.grid(row=i+1, column=j+1,  pady = 10, padx = 20)

                button = Button(self.table, text="View Marks", command=lambda x=i: self.view_marks(x))
                button.grid(row=i + 1, column=j + 2)

                self.exams.append(parts)

            self.rows = i + 1

    def take_test(self, x):
        '''

        :param x: The row number for the test
        :return:
        '''
        exam = self.exams[x]

        questions = self.get_exam_questions(exam)

        t = TakeTest(self.root, exam["TestName"], exam, questions)
        q = t.questions

        with open("test_answers.csv", "a") as f:
            fields = list(q[0].keys())
            fields.append("Student")
            fields.append("Markes")
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=',', lineterminator='\n')
            for question in q:
                question['Student'] = self.user
                #writer.writeheader()

                # the checking answer part comes here as described below
                writer.writerow(question)


        # to finish tis. we need to compare gainst the professors answers.
        # that's in the Correct field for each question in self.questions

        # so each question that's been attemped (for question in q) needs to be
        # compared against the corresponding entry in all_questions, we will then set a
        # marks fields in the question 1 for correct (matches lectureres choice) 1 for
        # incorrect - does not match the lecturers choice
    def view_marks(self, x):
        print("View marks for row", x)
        exam = self.exams[x]
        marks = []
        exam_name = exam['TestName'].lower()
        for result in self.results:
            if result['TestName'].lower() == exam_name:
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
