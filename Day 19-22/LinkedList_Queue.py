class QueueNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_node = None
        self.rear = None

    def is_empty(self):
        return self.front_node is None

    def enqueue(self, item):
        new_node = QueueNode(item)
        if self.is_empty():
            self.front_node = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.front_node.data
            self.front_node = self.front_node.next
            if self.front_node is None:
                self.rear = None
            return dequeued_item
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.front_node.data
        else:
            raise IndexError("front from empty queue")

    def size(self):
        current = self.front_node
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)
print(queue_linked_list.dequeue())  # Output is 1
print(queue_linked_list.front())    # Output is 2
print(queue_linked_list.size())     # Output is 2
