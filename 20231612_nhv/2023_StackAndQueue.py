"""
Stack, list of elements that:
• Data can be inserted only at the end of a stack. [push]
• Data can be deleted only from the end of a stack. [pop]
• Only the last element of a stack can be read [peek]
last ele/ end of stack is the top of stack (LIFO)
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)
    

"""
Example: linter
"""

"""
Queue:
 queues are arrays with three restrictions (it’s just a different set
of restrictions):
• Data can be inserted only at the end of a queue. (This is identical behavior
to the stack.) [enqueue]
• Data can be deleted only from the front of a queue. (This is the opposite
behavior of the stack.) [dequeue]
• Only the element at the front of a queue can be read. (This, too, is the
opposite of behavior of the stack.) [peek]
"""

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)