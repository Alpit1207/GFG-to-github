#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    temp = n
	    rev = 0
	    while(temp>0):
	        digit = temp % 10
	        rev = rev *10 + digit
	        temp = temp //10
	    if rev == n:
	        return "Yes"
	    else:
	        return "No"
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends