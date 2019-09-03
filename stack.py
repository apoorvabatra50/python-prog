class stack:
    def __init__(self):
        self.stack= []

    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False


    def peek(self):
        return self.stack[-1]


    def remove(self):
        if len(self.stack)<= 0:
            return("no elements in the stack")
        else:
            return self.stack.pop()

.
Newstack= stack()
Newstack.add("apoorva")
Newstack.add("rudraksh")
Newstack.add("mommy")
Newstack.add("papa")
print(Newstack.peek())
Newstack.add("Sakshu")
print(Newstack.peek())
Newstack.remove()
print(Newstack.peek())