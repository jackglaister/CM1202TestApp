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
        self.row = 0

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

class TakeTest(Dialog):
    """
    Dialog to display the test which needs to be taken by the student

    """
    def __init__(self, parent, title, exam, marks):
        self.exam = exam
        self.marks = marks
        super().__init__(parent, title)

    def body(self, master):
        exam = self.exam
        marks = self.marks
        self.row = 0

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
class StudentWindow():
    def __init__(self, root, user):
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

        self.read_questions()
        logoutButton = Button(self.root, text="Log Out", command=frame.quit)
        logoutButton.grid(row=1, column=0)

    def read_questions(self):
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
        print("Take the test for row ", x)

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
    root.geometry("800x450")
    app = StudentWindow(root, user)
    root.mainloop()

if __name__ == '__main__':
    main(user="c10002")
