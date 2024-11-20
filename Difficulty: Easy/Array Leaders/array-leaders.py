class Solution:
    def leaders(self, arr):
        nums = []
        max_from_right = float('-inf')
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>= max_from_right:
                nums.append(arr[i])
                max_from_right = arr[i]
                    
        return nums[::-1]            
        # code here


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends