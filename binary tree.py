class Node:
    def __init__(self,Data):
        self.left= None
        self.right=None
        self.data=Data


    def Insert(self,ata):
        if self.data is not None:
            if  ata< self.data:
                if self.left is None:
                    self.left=Node(ata)
                else:
                    self.left.Insert(ata)
            elif ata> self.data:
                if self.right is None:
                    self.right=Node(ata)
                else:
                    self.right.Insert(ata)
        else:
            self.data=ata



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

Root=Node(20)
Root.Insert(30)
Root.Insert(30)
Root.Insert(40)
Root.Insert(50)
Root.Insert(60)
Root.Insert(10)
Root.Insert(0)
Root.Insert(14)
Root.Insert(17)
Root.Insert(80)
Root.Insert(90)
Root.Insert(100)
Root.Insert(105)
Root.Insert(int(input("enter a no.   ")))

Root.PrintTree()
