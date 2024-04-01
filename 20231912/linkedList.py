#Linked List

"""
The data from linked lists can be scattered across
different cells throughout the computer’s memory.

Connected data that is dispersed throughout memory are known as nodes.
In a linked list, each node represents one item in the list. The big question,
then, is: if the nodes are not next to each other in memory, how does the
computer know which nodes are part of the same linked list?

This is the key to the linked list: each node also comes with a little extra
information, namely, the memory address of the next node in the list.
This extra piece of data—this pointer to the next node’s mem:

|data|link(address of next node)|
|"a"|1652|     |"b"|1983|       |"c"|2001|      |"d"|null|
 1000-1001      1652-1653       1983-1984       2001-2002
        ..........     ..........       .......... (linked)

A linked list’s first node can also be referred to as its head, 
and its final node as its tail

The fact that a linked list’s data can be spread throughout the computer’s
memory is a potential advantage it has over the array. 
An array, by contrast, needs to find an entire block of 
contiguous cells to store its data, which can get increasingly difficult 
as the array size grows
"""

# Build a Node

class Node:
    def __init__(self, data) -> None:
       self.data = data
       self.next = Node

# Build a Linkedlist
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data): #O(N)
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data): #O(N)
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def delete_at_index(self, index): #O(N)
        if self.is_empty():
            return

        if index == 0:
            self.head = self.head.next

        current = self.head
        current_index = 0

        while current_index < index - 1:
            current = current.next
            current_index += 1
        
        current.next = current.next.next

    def search(self, data): #(N)
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def read(self, index): #O(N)
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1
        return current.data if current else current
    
    def insert(self, data, index): #O(K) -> O(N)
        current = self.head
        current_index = 0
        if index == 0:
            self.prepend(data) #O(1)
        new_node = Node(data)
        while current_index < index - 1:
            current = current.next
            current_index += 1
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

"""
No matter whether the list is an array or a linked list, we need to comb through
the entire list one element at a time to inspect each email address. This,
naturally, takes N steps. However, let’s examine what happens when we
actually delete each email address.

With an array, each time we delete an email address, we need another O(N)
steps to shift the remaining data to the left to close the gap. All this shifting
will happen before we can even inspect the next email address.

Let’s assume that 1 in 10 email addresses are invalid. If we had a list of 1,000
email addresses, we’d have about 100 invalid ones. Our algorithm, then,
would take 1,000 steps to read all 1,000 email addresses. On top of that,
though, it might take up to an additional 100,000 steps for deletion, as for
each of the 100 deleted addresses, we might shift up to 1,000 other elements.

With a linked list, however, as we comb through the list, each deletion takes
just one step, as we can simply change a node’s link to point to the appropriate
node and move on. For our 1,000 emails, then, our algorithm would take just
1,100 steps, as there are 1,000 reading steps, and 100 deletion steps.

It turns out, then, that linked lists are an amazing data structure for moving
through an entire list while making insertions or deletions, as we never have
to worry about shifting other data as we make an insertion or deletion.
"""

#Doubly Linked List
"""
A doubly linked list is like a linked list except that each node has two
links—one that points to the next node, and another that points to the previous
node. In addition, the doubly linked list always keeps track of both the first
and last nodes, instead of just the first node.
"""
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, data) -> None:
        self.data = data
        self.head = None
        self.tail = self.head
    
    def is_empty(self):
        return self.head is None
    
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail = new_node
    
    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
        if index == -1:
            self.append(data)

        new_node = Node(data)
        current_index = 0
        current = self.head
        while current_index < index:
            current = current.next
            current_index += 1

        current.next.prev = new_node
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
    
    def delete_by_index(self, index):
        if self.is_empty():
            return

        if index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        if index == -1:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        current = self.head
        current_index = 0

        while current_index < index - 1:
            current = current.next
            current_index += 1
        
        current.next = current.next.next
        current.next.prev = current.next.prev.prev
            

#Queue as Doubly Linked List
"""
Because doubly linked lists have immediate access to both the front and end
of the list, they can insert data on either side at O(1) as well as delete data
on either side at O(1).
Because doubly linked lists can insert data at the end in O(1) time and delete
data from the front in O(1) time, they make the perfect underlying data structure
for a queue.

By implementing our queue with a doubly linked list, we can now both insert
and delete from the queue at a speedy O(1). And that’s doubly awesome.
"""

"""
Add a method to the classic LinkedList class that
reverses the list. That is, if the original list is A -> B -> C, all of the list’s
links should change so that C -> B -> A.
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, data) -> None:
        self.data = data
        self.head = None
    
    def reverse(self):
        prev_node = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node

"""
Let’s say you have access to a node from somewhere in the middle of a 
classic linked list, but not the linked list itself. 
That is, you have a variable that points to an instance
of Node, but you don’t have access to the LinkedList instance. 
In this situation, if you follow this node’s link, you can find all the items from this middle
node until the end, but you have no way to find the nodes that precede
this node in the list.
Write code that will effectively delete this node from the list. The entire
remaining list should remain complete, with only this node removed.
"""

def delete_node(mid: Node):
    mid.data = mid.next.data
    mid.next = mid.next.next

    

