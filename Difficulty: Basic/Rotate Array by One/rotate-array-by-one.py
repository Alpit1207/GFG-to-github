#User function Template for python3

class Solution:
    def rotate(self, arr):
        sup = arr[len(arr)-1]
        extra = arr[0]
        for i in range (1,len(arr)):
            next = arr[i]
            arr[i] = extra
            extra = next
            
        arr[0] = sup;
        return arr
    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1

# } Driver Code Ends