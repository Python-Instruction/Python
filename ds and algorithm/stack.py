

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, dataval):
# Use list append method to push element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use pop to look at the top of the stack
    def pop(self):     
	    return self.stack[-1]

St = Stack()
St.push(1)
St.push(2)
St.pop()


print(St.pop())
St.push(5)
St.push(6)
print(St.pop())