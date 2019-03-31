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
    def addQuestion(testID, questionID, questionType, questionText, answer, choices): 
    """ 
    >>> addMultipleChoiceQuestion("000120","Q0001",bool(1),"In what year was python first released?","1990","1970","2002","1985","1990") 
    >>> import csv 
    >>> f = open("000115.csv","r") 
    >>> fr = csv.reader(f)
    >>> LastItem = [] 
    >>> for row in fr: 
    ...     LastItem = row 
    >>> print(LastItem[0] == "Q0001") 
    True 
    >>> print(LastItem[1] == "1") 
    True 
    >>> print(LastItem[2] == "In what year was python first released?") 
    True 
    >>> print(LastItem[3] == "1990") 
    True 
    >>> print(LastItem[4] == "["1970","2002","1985","1990"])
   
    """ 
    f = open(str(testID)+".csv","a") 
    f.write(str(questionID)+","+str(int(questionType))+","+str(questionText)+","+str(answer)+","+str(choices)+"\n") 
    f.close() 
    def __init__(self, text, answer, questionNumber, choices)
        self._text = text
        self._answer = answer
        self.questionNumber = questionNumber
        self._choices = choices
    def editQuestion(self, text, answer, choices):
        self._text = text
        self._answer = answer
        self._choices = choices
    

class Question:
    __init__(self, text, answer, questionNumber):
        self._text = text
        self._answer = answer 
        self.questionNumber = questionNumber
