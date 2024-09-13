'''
Write a program to calculate the Fatorial of a given number
'''

def factorial(n):
    ''' Recursive method to generate the factorial of a number '''
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1) 


# Driver Code
if __name__ == '__main__':
    num = 5
    print('Factorial of', num, 'is', factorial(num))
