#User function Template for python3
class Solution:
    def is_prime(self,n):
        if n<2:
            return False
        elif n == 2 :  
            return True
        else:
            for i in range(2,int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True        
    def isSumOfTwo (self, N):
        if N % 2 != 0:
            second_num = N - 2
            if self.is_prime(second_num) is True:
                return "Yes"
            else:
                return "No"
        else:
            for i in range(2,int(N/2)+1):
                if self.is_prime(i) is True:
                    second_num = N - i
                    if self.is_prime(second_num) is True:
                        return "Yes"
            return "No"
                        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.isSumOfTwo(N))
        print("~")
# } Driver Code Ends