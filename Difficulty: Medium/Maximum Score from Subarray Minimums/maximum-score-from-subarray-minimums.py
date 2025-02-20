#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        summ = 0
        max_sum = 0
        
        for i in range(len(arr)-1):
            summ = (arr[i] + arr[i+1])
            max_sum = max(max_sum , summ)
        return max_sum    
            # Your code goes here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends