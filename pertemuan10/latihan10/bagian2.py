class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        if self.top == None:
            return self.size == 0

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return "Stack kosong"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.top.url

    def size(self):
        return self.count

myStack = StackLinkedList()

myStack.push("https://instagram.com/njw_khairunnisa")
myStack.push("https://instagram.com/kirun_9876")
myStack.push("https://instagram.com/wwww.id")

print("LinkedList:")
print("Peek:", myStack.peek())
print("Pop:", myStack.pop())
print("LinkedList after Pop:")
print("isEmpty:", myStack.isEmpty())
print("Size:", myStack.size())