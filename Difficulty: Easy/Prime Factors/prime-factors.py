#User function Template for python3

class Solution:
    def prime(self,n):
        if n <2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
                
	def AllPrimeFactors(self, N):
	    
	    prime_factors = []
	    if N < 2:
	        return prime_factors
	    else:
	        for i in range(2,N+1):
	            if N % i == 0 and self.prime(i):
	               # prime_candidate = self.prime(i)
	               # if prime_candidate:
	               #     prime_factors.append(prime_candidate)
	               prime_factors.append(i)
	    return prime_factors            
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends