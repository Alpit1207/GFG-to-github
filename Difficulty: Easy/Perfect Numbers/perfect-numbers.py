#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        add = 1
        if N <=1:
            return 0
        else:
            for i in range(2,int(N**0.5)+1):
                if N % i == 0 :
                    add += i
                    other_num = N / i 
                    if N % other_num == 0 :
                        add+= other_num
        if add == N:
            return 1
            
        return 0    
                
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
        print("~")
# } Driver Code Ends