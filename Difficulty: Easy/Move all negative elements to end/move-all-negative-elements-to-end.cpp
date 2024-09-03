//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    void segregateElements(vector<int>& arr) {
        // Your code goes here
        vector<int> arr1 ;
        vector<int> arr2 ;
     for(int i=0 ; i<arr.size() ; i++){
        if(arr[i]>=0){
            arr1.push_back(arr[i]);
        } else {
            arr2.push_back(arr[i]);
        }
     } 
     
     for(int i=0;i<arr1.size();i++){
         arr[i]=arr1[i];
     }
     for(int i=0;i<arr2.size();i++){
         arr[arr1.size()+i]=arr2[i];
     }
    }
};

//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);

    while (t--) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        vector<int> nums;
        int num;
        while (ss >> num) {
            nums.push_back(num);
        }
        Solution ob;
        ob.segregateElements(nums);

        for (int x : nums)
            cout << x << " ";
        cout << endl;
    }
}
// } Driver Code Ends