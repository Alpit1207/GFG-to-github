#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        num = n
        summ = 0
        while(num != 0):
            digit = num % 10
            num = num //10
            summ = summ + digit ** 3
            
        if summ == n  :
            return "true"
        else:
            return "false"
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends