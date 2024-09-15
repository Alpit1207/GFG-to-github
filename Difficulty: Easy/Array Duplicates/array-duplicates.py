
from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        dictt = {}
        arrr = []
        
        for i in range(len(arr)):
            if arr[i] in dictt:  # Use arr[i] instead of i
                dictt[arr[i]] += 1
            else:
                dictt[arr[i]] = 1
        
        for key, value in dictt.items():
            if value > 1:
                arrr.append(key)
        
        arrr.sort()
        
        if not arrr:
            return [-1]
        
        return arrr

        # code here
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.duplicates(n, arr)

        IntArray().Print(res)

# } Driver Code Ends