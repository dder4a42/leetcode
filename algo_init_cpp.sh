#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"Problem Title\""
    exit 1
fi

TITLE="$1"
DIR_NAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd 'a-z0-9_')
mkdir -p "$DIR_NAME"

# Create test_cases.txt
cat > "$DIR_NAME/test_cases.txt" << 'END'
# Test Cases Format:
# - Input lines (one or more)
# - "---" separator line
# - Expected Answer (e.g., [0,1], 9, [1,2,3])
# - Blank line separator between test cases
#
# Each input line becomes an argument to solve() method.

[2,7,11,15]
9
---
[0,1]

END

# Create solution.cpp
cat > "$DIR_NAME/solution.cpp" << 'END'
#include "../utils_cpp/utils.h"
#include <fstream>

using namespace std;

class Solution {
public:
    // Main solve method - modify signature and implementation as needed
    string solve(const vector<string>& inputs) {
        // Parse inputs
        auto nums = io::parseList(inputs[0]);
        int target = stoi(inputs[1]);
        
        // Call your actual solution method
        auto result = twoSum(nums, target);
        
        // Convert result to string
        return io::toString(result);
    }
    
    // Example: Two Sum problem
    vector<int> twoSum(vector<int>& nums, int target) {
        // TODO: Implement your solution here
        return {0, 1};
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
END

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

# Print instructions
echo "✓ LeetCode C++ environment created: $DIR_NAME/"
echo ""
echo "Files created:"
echo "  ├── $DIR_NAME/test_cases.txt"
echo "  ├── $DIR_NAME/solution.cpp"
echo "  └── $DIR_NAME/Makefile"
echo ""
echo "To get started:"
echo "  cd $DIR_NAME"
echo "  make"
echo "  ./solution"