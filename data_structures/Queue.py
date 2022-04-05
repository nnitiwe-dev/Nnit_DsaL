#FIFO
class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not len(self.queue)
    
    def enqueue(self, data):
        self.queue.append(data)
        return self.queue

    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue[0]
    

my_queue = Queue()

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")
print(f"Queue first data: {my_queue.peek()}")
# Queue first data: a
    
print(f"The data '{my_queue.dequeue()}' removed from the Queue")
# The data 'a' removed from the Queue
