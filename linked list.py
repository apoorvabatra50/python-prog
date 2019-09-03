class node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval= None



class SlinkedList:
    def __init__(self):
        self.HeadVal= None


    def ListPrint(self):
        printVal= self.HeadVal
        while printVal is not None:
            print(printVal.dataval)
            printVal=printVal.nextval



list1= SlinkedList()
list1.HeadVal= node("mon")
El2= node("tue")
El3= node("wed")
El4= node("thu")
El5= node("fri")

list1.HeadVal.nextval=El2
El2.nextval=El3
El3.nextval=El4
El4.nextval=El5


list1.ListPrint()