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
# Test Cases
[2,7,11,15]
9
---
[0,1]
END

# Create solution.cpp
cat > "$DIR_NAME/solution.cpp" << 'END'
#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int solve(vector<int>& nums) {
        return 0;
    }
};

int main() {
    cout << "Solution compiled!" << endl;
    return 0;
}
END

# Create Makefile
cat > "$DIR_NAME/Makefile" << 'END'
CC=g++
CFLAGS=-std=c++17 -Wall -Wextra -O2
TARGET=solution
SRC=solution.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)
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
EOF