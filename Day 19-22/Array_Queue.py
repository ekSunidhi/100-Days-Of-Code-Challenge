class QueueArray:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("-Cannot dequeue from empty queue-")
        
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("-Cannot front from empty queue-")
        
    def size(self):
        return len(self.items)
    
# Example usage
queue_array=QueueArray()
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)
print(queue_array.dequeue()) # Output is 1
print(queue_array.front()) # Output is 2
print(queue_array.size()) # Output is 2        