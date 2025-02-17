# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = 0
        max_length = 0
        hashmap = {0:-1}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            
            if prefix_sum - k in hashmap:
                sub_length = i - hashmap[prefix_sum - k]
                max_length = max(max_length , sub_length)
                
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i
                
        return max_length        
        # code here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends