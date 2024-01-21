class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)
print(stack_linked_list.pop())  # Output is 3
print(stack_linked_list.peek())  # Output is 2
print(stack_linked_list.size())  # Output is 2
