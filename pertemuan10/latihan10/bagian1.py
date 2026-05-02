class StackList:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, url):
        self.stack.append(url)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
myStack = StackList()

myStack.push("https://instagram.com/njw_khairunnisa")
myStack.push("https://instagram.com/kirun_9876")
myStack.push("https://instagram.com/wwww.id")

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())
