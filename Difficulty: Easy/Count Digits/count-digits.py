#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        x = N
        count = 0
        while (x>0):
            digit = x%10
            if digit > 0:
                if N%digit == 0:
                    count += 1
            x = x//10
        return count
            # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends