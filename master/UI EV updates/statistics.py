from tkinter import *
from dialogwindow import Dialog
from utils import MenuScreen
import csv

def showStats(testID):
    filename = str("statistics")+".csv"
    highestMark = -1
    numberOfWrongAnswers = 0
    numberOfCorrectAnswers = 0
    numberOfAllCorrectSubmissions = 0
    highestMarkUser = ""
    with open(filename) as file:
        reader = csv.reader(file,delimiter=",")
        for row in reader:
            score = calculateScore(row[2:])
            wrongs = calculateWrongs(row[2:])
            corrects = caculateCorrects(row[2:])

            userID = row[0]
            testID = row[1]

            if score > highestMark:
                highestMark = score
                highestMarkUser = userID

            numberOfWrongAnswers += wrongs
            numberOfCorrectAnswers += corrects

            if wrongs == 0:
                numberOfAllCorrectSubmissions += 1

        return (highestMark, highestMarkUser, numberOfWrongAnswers, numberOfCorrectAnswers, numberOfAllCorrectSubmissions)
"""    print("Highest mark ever scored in a test: " + str(highestMark))
       print("User ID with the highest mark: " + highestMarkUser)
       print("Number of wrong answers recorded: " + str(numberOfWrongAnswers))
       print("Number of correct answers recorded: " + str(numberOfCorrectAnswers))
       print("Number of perfect scores recorded: " + str(numberOfAllCorrectSubmissions))
"""
class ViewStatistics(MenuScreen):
    def __init__(self):
        root = Tk()
        root.title("Show Statistics")
        super().__init__()
        self.root = root
        self.table = Frame(self.root)
        self.rows = 0;
        mainfr = Frame(root)
        mainfr.grid(column=0,row=0, sticky=(N,W,E,S))
        mainfr.columnconfigure(0, weight=1)
        mainfr.rowconfigure(0, weight=1)
        mainfr.pack(pady = 100, padx = 400)
        tkvar = StringVar(root)
        choices = {}
        for row in csv.reader(open("exams.csv","r")):
            choices[row[0]] = row[0]
        tkvar.set('none')
        popupMenu = OptionMenu(mainfr, tkvar, *choices)
        Label(mainfr, text="Choose a test").grid(row = 1, column = 1)
        Label1 = Label(mainfr, text="Please select a test:")
        popupMenu.grid(row = 2, column =1)
        def change_dropdown(*args):
            print("dropdown changed")
            stats = showStats(tkvar.get())
            print(stats)
            Label1 = Label(mainfr, text="The heighest mark achieved: "+str(stats[0]))
            Label2 = Label(mainfr, text="The user id of the user with the highest mark: "+str(stats[1]))
            Label3 = Label(mainfr, text="Number of wrong answers: "+str(stats[2]))
            Label4 = Label(mainfr, text="Number of Correct Answers: "+str(stats[3]))
            Label5 = Label(mainfr, text="Number of students to get 100%: "+str(stats[4]))
            root.update()
        tkvar.trace('w', change_dropdown)
        root.mainloop()

def calculateScore(row):
    score = 0
    for each in row:
        if each == "1":
            score += 1
    return score


def calculateWrongs(row):
    wrongs = 0
    for each in row:
        if each == "0":
            wrongs += 1
    return wrongs

def caculateCorrects(row):
    corrects = 0
    for each in row:
        if each == "1":
            corrects += 1
    return corrects


if __name__ == '__main__':
    ViewStatistics()
