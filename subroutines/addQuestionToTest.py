#/bin/python3
def addQuestion(testID, questionType, questionText, answer, choices):
    """
    >>> addQuestion("000115",bool(1),"How many unique representations can 8 bits make","256",none)
    >>> import csv
    >>> f = open("000115.csv","r")
    >>> fr = csv.reader(f)
    >>> LastItem = []
    >>> for row in fr:
    >>>     LastItem = row
    >>> print((LastItem[0] == "Q0001" and LastItem[1] == "1" and LastItem[2] == "How many unique representations can 8 bits make" and LastItem[3] == "256"))
    True
    """
