'''
Write a program to implement Stack using Arrays
'''

class Stack:

    def __init__(self, capacity):
        ''' Initialize stack with capacity '''
        self.stack    = []
        self.capacity = capacity

  
    def isEmpty(self):
        return len(self.stack) == 0
      
      
    def push(self, value):
        if len(self.stack) == self.capacity:
            print('Stack is full')
        else:
            self.stack.append(value)
            print('Stack updated...')


    def pop(self):
        return None if self.isEmpty() else self.stack.pop()


    def peek(self):
        return self.stack[-1]


    def __repr__(self):
        return str(self.stack)
    

    def __len__(self):
        return len(self.stack)


# Driver Code
if __name__ == '__main__':
    stack = Stack(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack)
    stack.pop()
    print(len(stack))
    print(stack.peek())

    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
