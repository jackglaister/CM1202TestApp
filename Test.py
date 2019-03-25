from datetime import datetime
class Test:
    """
        >>> import csv
        >>> newTest = Test("Practice test","05/12/19","05/12/20","000115")
        >>> f = open("Tests.csv","r")
        >>> fcsv = csv.reader(f)
        >>> for line in fcsv:
        ...     lastline = line
        >>> print(lastline == ["05/12/19","Practice test","05/12/20","000115"])
        True
    """
    def __init__(self, title, releaseDate, deadline, testID, questions):
        self.__releaseDate = datetime.strptime(releaseDate, "%d/%m/%y").date()
        self.title = title
        self.__deadline = datetime.strptime(releaseDate, "%d/%m/%y").date()
        self.__testID = testID
        self.__questions = questions
        f = open("Tests.csv","a")
        f.write(str(releaseDate)+","+title+","+deadline+","+testID+"\n")

    def addQuestionToTest(self, Token, type):
        if type:
            self.__questions = multipleChoiceQuestion()
        else:
            self.__questions = question()

class multipleChoiceQuestion(Question):
    

class Question:
    __init__(self, text, answer, questionNumber):
        self._text = text
        self._answer = answer 
        self.questionNumber = questionNumber

