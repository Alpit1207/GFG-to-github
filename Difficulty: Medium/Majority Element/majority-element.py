#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
                
        for j in freq :
            if freq[j] > len(arr)//2:
                return j
        return -1
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))
        print("~")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends