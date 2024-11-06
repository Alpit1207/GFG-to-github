#User function Template for python3

class Solution:
	def binary_to_decimal(self, b):
	    num = 0
	    i = 0
	    while(b):
	        digit = int(b)%10
	        num += (digit * (2**i))
	        b = int(b)//10
	        i+=1
	    return num 
	        
	        
	        
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.binary_to_decimal(str)
        print(ans)
        print("~")

# } Driver Code Ends