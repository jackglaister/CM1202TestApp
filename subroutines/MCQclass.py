class MultipleChoiceQuestion:
    def addQuestion(self, testID, questionID, questionType, questionText, answer, choices): 
    """ 
    >>> MultipleChoiceQuestion("000120","Q0001",bool(1),"In what year was python first released?","1990","1970","2002","1985","1990") 
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

    def __init__(self, questionID, questionType, questionText, answer, choices):
        self.__questionType = questionType
        self.__questionText = questionText 
        self.__answer = answer
        self.__choices = choices
