#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        temp = N
        count = 0
        while(temp>0):
            digit = temp%10
            if digit != 0:
                if N % digit == 0:
                    count += 1
            temp = temp //10        
         
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
        print("~")
# } Driver Code Ends