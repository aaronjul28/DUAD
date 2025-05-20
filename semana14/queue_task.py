
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head == None:
            return None
        val = self.head.value
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def pop_right(self):
        if self.tail == None:
            return None
        val = self.tail.value
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        else:
            self.head = None
        return val

    def print_queue(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next





my_queue=Queue()
my_queue.push_left('First left')
my_queue.push_left('Second left')
my_queue.push_right('First right')
my_queue.print_queue()
my_queue.pop_left()
print('after pop')
my_queue.print_queue()