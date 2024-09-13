'''
Trapping Rain Water in Python
We are given with n non-negative integers representing an elevation map where the width of each bar is 1, 
we need to compute how much water it is able to trap after raining.

Example :
Input : arr = [2,0,3,0,2,0,4]
Output : 9

Explanation : We can trap “2 units” of water between 2 and 3, “7 units” between 3 and 4 
(“3 units” between 3 and 2, “1 unit” on top of bar 2 and “3 units” between 2 and 4.
'''

def trapRainWater(arrHeights):
    ''' Method to calculate rainwater trapped in the given heights '''
    left, right       = 0, len(arrHeights) - 1 
    leftMax, rightMax = -1, -1
    water             = 0

    while left < right:
        leftMax  = max(leftMax, arrHeights[left])
        rightMax = max(rightMax, arrHeights[right])

        if leftMax < rightMax:
            water += leftMax - arrHeights[left]
            left  += 1
        else:
            water += rightMax - arrHeights[right]
            right -= 1

    return water


''' Driver Code '''
if __name__ == '__main__':
    arrWaterHeights = [2,0,3,0,2,0,4]
    print(trapRainWater(arrWaterHeights))
            
