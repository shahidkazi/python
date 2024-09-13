'''
Write a program to calculate the Fibonacci of a given number
Fibonacci - 1 1 2 3 5 8 ...
'''
def fibonacciGenerator(seq):
    ''' Function to return generator for the sequence '''
    a = 0
    yield a
    b = 1
  
    for i in range(seq - 1):
        yield b
        a, b = b, a+b

# Driver Code
if __name__ == '__main__':
    seq = 6
    for i in fibonacciGenerator(seq):
        print(i, end= ' ')
