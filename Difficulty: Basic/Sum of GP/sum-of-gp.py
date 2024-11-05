#User function Template for python3

class Solution:
	def sum_of_gp(self, n, a, r):
	    if r<1:
	        return int(a*(1-(r**n))/(1-r))
	    elif r>1 :
	        return int(a*((r**n)-1)/(r-1))
	    else:
	        return int(n*a)
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, r = input().split()
		n = int(n)
		a = int(a)
		r = int(r)
		ob = Solution();
		ans = ob.sum_of_gp(n, a, r)
		print(ans)
# } Driver Code Ends