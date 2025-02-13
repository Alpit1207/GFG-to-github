#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # return sorted(list(set(a+b)))
        i, j = 0, 0
        result = []

        while i < len(a) and j < len(b):
        # Add smaller element
            if a[i] < b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1
            else:
            # Equal elements - add once
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

    # Append remaining elements from arr1
        while i < len(a):
            if result[-1] != a[i] if result else True:
                result.append(a[i])
            i += 1

    # Append remaining elements from arr2
        while j < len(b):
            if result[-1] != b[j] if result else True:
                result.append(b[j])
            j += 1

        return result        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends