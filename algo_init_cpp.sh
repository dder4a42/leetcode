#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"Problem Title\" [type]"
    echo ""
    echo "Types:"
    echo "  listnode   - Linked list problem (e.g., insertion sort)"
    echo "  treenode   - Binary tree problem"
    echo "  vector     - Array problem (default)"
    echo "  int        - Single integer"
    echo "  string     - String problem"
    echo "  matrix     - 2D matrix problem"
    echo ""
    echo "Examples:"
    echo "  $0 'Insertion Sort List' listnode"
    echo "  $0 'Two Sum' vector"
    echo "  $0 'Binary Tree Inorder' treenode"
    exit 1
fi

TITLE="$1"
TYPE="${2:-vector}"
DIR_NAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd 'a-z0-9_')
mkdir -p "$DIR_NAME"

# Generate test_cases.txt based on problem type
case $TYPE in
    listnode)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
[4, 2, 1, 3]
---
[1, 2, 3, 4]

[2, 1]
---
[1, 2]

[1, 2, 3]
---
[1, 2, 3]

[5, 4, 3, 2, 1]
---
[1, 2, 3, 4, 5]
TESTEND
        ;;
    treenode)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
[1, 2, null, null, 3]
---
[1, null, 2, null, null, null, 3]
TESTEND
        ;;
    int)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
123
---
321

456
---
654

100
---
1
TESTEND
        ;;
    string)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
hello
---
olleh

world
---
dlrow

a
---
a
TESTEND
        ;;
    matrix)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
[[1,2,3],[4,5,6],[7,8,9]]
---
[1,2,3,4,5,6,7,8,9]
TESTEND
        ;;
    vector|*)
        # Default: Two Sum style (2 inputs)
        cat > "$DIR_NAME/test_cases.txt" << 'TESTEND'
[2,7,11,15]
9
---
[0,1]

[3,2,4]
6
---
[1,2]

[3,3]
6
---
[0,1]
TESTEND
        ;;
esac

# Generate solution.cpp based on problem type
case $TYPE in
    listnode)
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // Parse inputs
        ListNode* head = parseListNode(inputs[0]);
        
        // Call your actual solution method
        ListNode* result = insertionSortList(head);
        
        // Convert result to string
        return toString(result);
    }
    
    // TODO: Implement your solution here
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !head->next) return head;
        
        // Your implementation...
        
        return head;
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;

    treenode)
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

// Note: Tree parsing needs custom implementation based on your format
// Common formats: level-order [1,2,3,null,null,4] or pre-order

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // TODO: Implement tree parsing based on your format
        // TreeNode* root = parseTreeLevel(inputs[0]);
        
        TreeNode* result = invertTree(nullptr);
        
        // TODO: Implement tree to string conversion
        return "[]";
    }
    
    // TODO: Implement your solution here
    TreeNode* invertTree(TreeNode* root) {
        return root;
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;

    int)
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // Parse inputs
        int n = stoi(inputs[0]);
        
        // Call your actual solution method
        int result = myFunction(n);
        
        // Convert result to string
        return to_string(result);
    }
    
    // TODO: Implement your solution here
    int myFunction(int n) {
        return n;
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;

    string)
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // Parse inputs
        string s = inputs[0];
        
        // Call your actual solution method
        string result = reverseString(s);
        
        // Result is already a string
        return result;
    }
    
    // TODO: Implement your solution here
    string reverseString(string s) {
        reverse(s.begin(), s.end());
        return s;
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;

    matrix)
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // Parse inputs - TODO: implement matrix parsing
        // vector<vector<int>> matrix = parseMatrix(inputs[0]);
        
        // Call your actual solution method
        auto result = spiralOrder({});
        
        return toString(result);
    }
    
    // TODO: Implement your solution here
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        return {};
    }
    
    // TODO: Implement matrix parsing
    vector<vector<int>> parseMatrix(const string& s) {
        return {};
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;

    vector|*)
        # Default: vector type
        cat > "$DIR_NAME/solution.cpp" << 'CPPCODE'
#include "utils_cpp/utils.h"
#include <fstream>

using namespace io;
using namespace std;

class Solution {
public:
    string solve(const vector<string>& inputs) {
        // Parse inputs
        auto nums = parseList(inputs[0]);
        int target = stoi(inputs[1]);
        
        // Call your actual solution method
        auto result = twoSum(nums, target);
        
        // Convert result to string
        return toString(result);
    }
    
    // Example: Two Sum problem
    vector<int> twoSum(vector<int>& nums, int target) {
        // TODO: Implement your solution here
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            if (seen.count(target - nums[i])) {
                return {seen[target - nums[i]], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    Solution sol;
    ifstream testFile("test_cases.txt");
    if (!testFile.is_open()) {
        cerr << "Error: Could not open test_cases.txt" << endl;
        return 1;
    }
    io::runTests<Solution, string>(sol, &Solution::solve, testFile);
    testFile.close();
    return 0;
}
CPPCODE
        ;;
esac

# Create Makefile
cat > "$DIR_NAME/Makefile" << 'END'
CC=g++
CFLAGS=-std=c++17 -Wall -Wextra -g -I..
TARGET=solution
SRC=solution.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all run clean
END

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create symlink to utils if not exists
if [ ! -e "$DIR_NAME/utils_cpp" ]; then
    ln -s "$SCRIPT_DIR/utils_cpp" "$DIR_NAME/utils_cpp"
fi
if [ ! -e "$DIR_NAME/utils_cpp" ]; then
    ln -s ../utils_cpp "$DIR_NAME/utils_cpp"
fi

# Print instructions
echo "✓ LeetCode C++ environment created: $DIR_NAME/"
echo ""
echo "Problem type: $TYPE"
echo ""
echo "Files created:"
echo "  ├── $DIR_NAME/test_cases.txt"
echo "  ├── $DIR_NAME/solution.cpp"
echo "  ├── $DIR_NAME/Makefile"
echo "  └── $DIR_NAME/utils_cpp ->"
echo ""
echo "To get started:"
echo "  cd $DIR_NAME"
echo "  make"
echo "  ./solution"
echo ""
echo "Or run tests from file:"
echo "  ./solution < test_cases.txt"
