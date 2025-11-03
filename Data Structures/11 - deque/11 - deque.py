"""This script implements a simple queue data structure using deque from the collections module"""
from collections import deque

class Queue:
    def __init__(self):
        # Initialize an empty deque
        self.queue = deque()  

    def enqueue(self, item):
        # Add item to the end of the queue
        self.queue.append(item)  

    def dequeue(self):
        if not self.is_empty():
            # Remove and return the front item
            return self.queue.popleft()  
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0  

if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    print(my_queue.dequeue())  
    print(my_queue.dequeue())  
    print(my_queue.dequeue())  
