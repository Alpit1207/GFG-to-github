#User function Template for python3

class Solution:
    def isPrime (self, N):
        if N < 2:
            return 0
        else:    
            for i in range(2,int(N**0.5)+1):
                if N % i == 0:
                    return 0
        return 1  
            # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
        print("~")
# } Driver Code Ends