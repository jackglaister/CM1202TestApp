from tkinter import *
import csv
from dialogwindow import Dialog
from utils import TakeTest, MenuScreen


class LecturerWindow(MenuScreen):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.table = Frame(self.root)
        self.rows = 0;

        self.columns = ["Test Name","Test Type",""]
#        self.root.pack(padx=20, pady=50)
        self.table.grid(row=0, column=1, columnspan=2)

        frame = Frame()

        with open("exams.csv") as f:
            reader = csv.DictReader(f)
            for i, parts in enumerate(reader):
                self.exams.append(parts)
                for j, (key, val) in enumerate(parts.items()):
                    Label(self.table, text=val, bd=3).grid(row=i+1, column=j, padx=10)

                button = Button(self.table, text="View Marks", command=lambda x=i: self.view_marks(x))
                button.grid(row=i+1, column=j+1, pady = 10, padx=20)

                button = Button(self.table, text="Edit Test", command=lambda x=i: self.edit_test(x))
                button.grid(row=i+1, column=j+2)

            self.rows = i + 1

        logoutButton = Button(self.root, text="Log Out", command=frame.quit)
        logoutButton.grid(row=1, column=1)

        newTestButton = Button(self.root, text="Create a new test")
        newTestButton.grid(row=1, column=2, pady=10, padx=25)

        statsButton = Button(self.root, text="See statistics for tests")
        statsButton.grid(row=1, column=3, pady=10, padx=25)

    def view_marks(self, x):
        print("take the tet for row ", x)

        exam = self.exams[x]
        questions = self.get_exam_questions(exam)

    def view_test(self, x):
        print("View test", x)


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

        edit = TakeTest(self.root, exam["TestName"], exam, questions)
        q = edit.questions

        with open("questions.csv", "w") as f:
            fields = list(q[0].keys())
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=',', lineterminator='\n')
            writer.writeheader()
            for question in self.all_questions:
                for edited_question in q:
                    if question['QuestionId'] == edited_question['QuestionId']:
                        try:
                            question['Correct'] = edited_question['Selected']
                            del question['Selected']
                            break
                        except KeyError:
                            pass
                writer.writerow(question)
def main():
    root = Tk()
    root.geometry("800x450")
    app = LecturerWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()