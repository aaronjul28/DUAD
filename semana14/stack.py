class Node:
    data : str
    
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def stack_push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
        print(f'Adding new node {new_node.data}')
        return data

    def stack_pop(self):
        if self.top is not None:
            popped_node=self.top
            self.top=self.top.next
            print(f'Removing node {popped_node.data}')
        else:
            print('Current node is already None')

    def show_stack(self):
        print('List of current nodes:')
        top=self.top
        while top:
            print(top.data)
            top=top.next

node_push=Stack()
node_push.stack_push('NODE1')
node_push.stack_push('NODE2')
node_push.show_stack()
node_push.stack_pop()
node_push.show_stack()
node_push.stack_pop()
node_push.stack_pop()
node_push.stack_pop()


