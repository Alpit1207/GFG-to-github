#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1
        while(low<=high):
            if s[low] != s[high]:
                return False
            low +=1
            high -=1
        return True    
                
		# code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends