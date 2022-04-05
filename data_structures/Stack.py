#LIFO
class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not len(self.queue)
    
    def push(self, data):
        self.stack.append(data)
        return self.stack

    def pop(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.stack[-1]

my_stack= Stack()

my_stack.push(1) 
my_stack.push(13) 
my_stack.push(2) 
my_stack.push(4) 
my_stack.pop() #pop 4
print("peek:",my_stack.peek()) 