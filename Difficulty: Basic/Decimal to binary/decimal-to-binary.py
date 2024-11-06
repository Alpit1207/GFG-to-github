#User function Template for python3
def toBinary(n):
    binary = ""
    while(n):
        rem = n % 2
        binary = str(rem) + binary
        n = n//2
    print(binary)  



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    for _ in range(int(input())):
        n=int(input())
        toBinary(n)

    
# } Driver Code Ends