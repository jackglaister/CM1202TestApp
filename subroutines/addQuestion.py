#/bin/python3
def addQuestion(testID, questionID, questionType, questionText, answer, choices):
    """
    >>> addQuestion("000115","Q0001",bool(1),"How many unique representations can 8 bits make","256","none")
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
    >>> print(LastItem[2] == "How many unique representations can 8 bits make")
    True
    >>> print(LastItem[3] == "256")
    True
    """
    f = open(str(testID)+".csv","a")
    f.write(str(questionID)+","+str(int(questionType))+","+str(questionText)+","+str(answer)+","+str("choices")+"\n")
    f.close()
