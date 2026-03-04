#include "../utils_cpp/utils.h"
#include <fstream>

using namespace std;

class Solution {
public:
    // Main solve method - modify signature and implementation as needed
    string solve(const vector<string>& inputs) {
        // Parse inputs
        auto nums = io::parseList(inputs[0]);
        
        // Call your actual solution method
        auto result = peak(nums);
        
        // Convert result to string
        return io::toString(result);
    }
    
    int peak(vector<int>& arr) {
        int lh=0, rh=arr.size()-1;
        while(lh < rh) {
            int mid = (lh + rh) / 2;
            if(arr[mid-1] < arr[mid]) {
                lh = mid;
            }else if(arr[mid+1] < arr[mid]) {
                rh = mid;
            }else {
                return mid;
            }
            if(rh - lh == 1) {
                return arr[lh] > arr[rh] ? lh : rh;
            }
        }
        return arr[lh];
    }
};

int main() {
    Solution sol;
    
    // Open test cases file
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    
    // Run tests using the io utilities
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    
    testFile.close();
    return 0;
}
