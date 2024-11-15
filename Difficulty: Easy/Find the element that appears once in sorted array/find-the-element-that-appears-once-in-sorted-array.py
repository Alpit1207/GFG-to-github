#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        for key in freq:
            if freq[key] ==1:
                return key
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
        print("~")
# } Driver Code Ends