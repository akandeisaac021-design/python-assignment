class CustomStack:

    def __init__(self):
        self.my_stack = []

    def length(self):
        count =0

        for _ in self.my_stack:
            count +=1

        length =count

        return length;        

    def is_empty(self):

        return self.length() ==0

    def push(self, value):
    
        self.my_stack.append(value)

    def peek(self):
        if self.is_empty():
            raise AttributeError("Stack is empty")
        return self.my_stack[-1]

    def pop(self):
        
        if not self.is_empty():
            return self.my_stack.pop()

        raise AttributeError("Stack is empty")


