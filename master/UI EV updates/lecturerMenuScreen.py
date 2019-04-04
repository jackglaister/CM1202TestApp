from tkinter import *
import csv
from dialogwindow import Dialog
from newTest import TestForm
from utils import TakeTest, MenuScreen, MarksDialog, QUESTION_COLUMNS, EXAM_COLUMNS


class LecturerWindow(MenuScreen):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.table = Frame(self.root)
        self.rows = 0;

        self.columns = ["Test Name","Test Type",""]
#        self.root.pack(padx=20, pady=50)
        self.table.grid(row=0, column=1, columnspan=2)

        self.elements = []
        self.display_table()


    def display_table(self):
        '''
        display the table of exams
        :return:
        '''

        for element in self.elements:
            element.grid_forget()

        self.elements.clear()

        frame = Frame()

        for i, parts in enumerate(self.exams):
            for j, (key, val) in enumerate(parts.items()):
                label = Label(self.table, text=val, bd=3)
                label.grid(row=i+1, column=j, padx=10)
                self.elements.append(label)

            button = Button(self.table, text="View Marks", command=lambda x=i: self.view_marks(x))
            button.grid(row=i+1, column=j+1, pady = 10, padx=20)
            self.elements.append(button)
            button = Button(self.table, text="Edit Test", command=lambda x=i: self.edit_test(x))
            button.grid(row=i+1, column=j+2)
            self.elements.append(button)

        self.rows = i + 1

        newTestButton = Button(self.root, text="Create a new test", command=self.new_test)
        newTestButton.grid(row=self.rows, column=2, pady=10, padx=25)

        self.elements.append(newTestButton)
        self.rows += 1

        logoutButton = Button(self.root, text="Log Out", command=frame.quit)
        logoutButton.grid(row=self.rows, column=1)
        self.elements.append(logoutButton)




    def view_marks(self, x):

        exam = self.exams[x]
        results = self.get_results(exam)
        marks = []

        for result in results:
            marks.append(result)

        di = MarksDialog(self.root, "Exam marks", exam, marks)

    def new_test(self):
        '''
        Create a new test
        :return:
        '''
        di = TestForm(self.root)
        if di.applied:
            self.read_exams()
            self.display_table()

    def edit_test(self, x):
        '''
        Edit test.

        At the moment the lecturer is only able to mark one of the answers as the correct answer.
        It's not possible at the omment to edit the question text or the answer text.

        once the lecturer clicks the ok buttong, we iterate through all the questions that were
        loaded at the time the object was initialized. (this is in the self.all_questions field.

        if any of the questions in all-questions have been edited, we set the 'Correct' field in that
        to the choice that the lecturer made by clicking the radio button.

        Then we write that back to the file. (all the equestions are written because with CSV you
        can't just write a part of the file

        '''

        self.root.title("Edit Test")

        exam = self.exams[x]
        questions = self.get_exam_questions(exam)

        edit = TakeTest(self.root, exam["TestName"], exam, questions, edit=True)

        if edit.applied:
            q = edit.questions

            with open("questions.csv", "w") as f:
                writer = csv.DictWriter(f, fieldnames=QUESTION_COLUMNS, delimiter=',', lineterminator='\n')
                for question in self.all_questions:
                    for edited_question in q:
                        if question['QuestionId'] == edited_question['QuestionId']:
                            try:
                                question['Correct'] = edited_question['Selected']
                                del question['Selected']
                                break
                            except KeyError:
                                pass

                    write_back = {k:v for k,v in question.items() if k in QUESTION_COLUMNS}
                    writer.writerow(write_back)

            exam["TestName"] = edit.questionvar.get()
            exam["TestType"] = edit.testType.get()
            self.write_exams()
            self.display_table()

def main():
    root = Tk()
    root.geometry("800x450")
    app = LecturerWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()