class StackArray:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("-Cannot pop from empty stack-")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("-Cannot peek from empty stack-")
        
    def size(self):
        return len(self.items)
    
# Example usage
stack_array=StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)
print(stack_array.pop()) # Output is 3
print(stack_array.peek()) # Output is 2
print(stack_array.size()) # Output is 2
    
    