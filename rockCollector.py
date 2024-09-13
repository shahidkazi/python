'''
You are an avid rock collector who lives in southern California. Some rare and desirable rocks just became available in New York, so you are planning a cross-country road trip. There are several other rare rocks that you could pick up along the way. You have been given a grid filled with numbers, representing the number of rare rocks available in various cities across the country. Your objective is to find the optimal path from So_Cal to New_York that would allow you to accumulate the most rocks along the way.

Note: You can only travel either north (up) or east (right).
b) Consider adding some additional tests in doTestsPass().
c) Implement optimalPath() correctly.
d) Here is an example:

              {{0, 0, 0, 0, 5}, New_York (finish)
               {0, 1, 1, 1, 0},
So_Cal (start) {2, 0, 0, 0, 0}} 

The total for this example would be 10 (2+0+1+1+1+0+5).
'''

def optimalPath(arrRoute):
    rows = len(arrRoute)
    cols = len(arrRoute[0])

    dt        = [[0] * cols for _ in range(rows)]
    dt[-1][0] = arrRoute[-1][0]

    # Fill the first column
    for i in range(rows-2, -1, -1):
        dt[i][0] = arrRoute[i][0] + dt[i-1][0]

    # Fill the last row
    for i in range(1, cols):
        dt[-1][i] = arrRoute[-1][i] + dt[-1][i-1]

    # Fill the rest of the cells
    for i in range(rows-2, -1, -1):
        for j in range(1, cols):
            dt[i][j] = arrRoute[i][j] + max(dt[i+1][j], dt[i][j-1])
  
    return dt[0][-1]


# Driver Code
if __name__ == '__main__':
    path = [[0, 0, 0, 0, 5],
            [0, 1, 1, 1, 0],
            [2, 0, 0, 0, 0]]

    print(optimalPath(path))
