'''
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 104
'''

# Math based implementation
def findFactorialTrailingZeroes(n):
    count = 0
    i     = 5

    while (n//i >= 1):
        count += n//i
        i *= 5

    return count


# Brute Force Implementation
def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n-1)


def bruteMethod(n):
    fact  = str(factorial(n))
    count = 0

    for i in range(len(fact)-1, -1, -1):
        if fact[i] == '0':
            count += 1
        else:
            break

    return count


# Driver code
if __name__ == '__main__':
    print('Math Method :', findFactorialTrailingZeroes(100))
    print('Brute Method:', bruteMethod(100))
