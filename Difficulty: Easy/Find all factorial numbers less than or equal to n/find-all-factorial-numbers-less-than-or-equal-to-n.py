#User function Template for python3

class Solution:
    
    def factorialNumbers(self, n):
        num = []
        def fact(n):
            if n == 1:
                return 1
            else:
                return n * fact(n-1)
        for i in range(1,n+1):
            fact_num = fact(i)
            if fact_num<=n:
                num.append(fact_num)
            else:
                break
        return num    
    	#code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends