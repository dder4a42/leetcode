# C++ LeetCode Setup Guide

## Overview
The C++ setup now includes IO parser and test case support similar to the Python version.

## Files Modified

### 1. utils_cpp/utils.h
Enhanced with:
- **IO Parsing Functions**:
  - `parseList(string)` - Parse `[1,2,3]` to `vector<int>`
  - `parseListNode(string)` - Parse `[1,2,3]` to `ListNode*`
  
- **String Conversion**:
  - `toString(vector<int>)` - Convert to `[1, 2, 3]`
  - `toString(ListNode*)` - Convert to `[1, 2, 3]`
  - `toString(vector<string>)` - Multi-line format
  
- **Test Runner**:
  - `parseTestCases(istream)` - Parse test_cases.txt format
  - `runTests<Solution, RetType>()` - Generic test runner with normalized comparison
  - `normalize(string)` - Normalize strings for comparison (handles spacing differences)

### 2. algo_init_cpp.sh
Updated template to:
- Include `#include "../utils_cpp/utils.h"`
- Use `ifstream` to read test_cases.txt
- Provide a `solve(vector<string>&)` wrapper method
- Use `io::runTests()` for automatic test execution
- Updated Makefile with `-I..` flag and `run` target

### 3. insertionlist_cpp/
Migrated to use new utilities:
- Simplified solution.cpp from ~140 lines to ~55 lines
- Uses centralized IO parsing and test running
- Updated test_cases.txt to standard format

## Test Case Format

```
# Comments start with #
# Format:
# - Input lines (one or more)
# - "---" separator
# - Expected output
# - Blank line between test cases

[2,7,11,15]
9
---
[0,1]

[3,2,4]
6
---
[1,2]
```

## Usage

### Create New Problem
```bash
bash algo_init_cpp.sh "Two Sum"
cd two_sum
```

### Write Solution
```cpp
class Solution {
public:
    // Wrapper for test runner
    string solve(const vector<string>& inputs) {
        auto nums = io::parseList(inputs[0]);
        int target = stoi(inputs[1]);
        auto result = twoSum(nums, target);
        return io::toString(result);
    }
    
    // Your actual solution
    vector<int> twoSum(vector<int>& nums, int target) {
        // Implementation here
    }
};
```

### Build and Run
```bash
make        # Compile
./solution  # Run tests
make run    # Compile and run
make clean  # Clean build files
```

## Features

1. **Automatic Test Parsing**: Reads test_cases.txt and parses inputs/expected outputs
2. **Flexible Format**: Handles both `[1,2,3]` and `[1, 2, 3]` formats
3. **Clear Output**: Shows input, expected, output, and pass/fail status
4. **Type Safety**: Template-based test runner supports any return type
5. **Standard C++17**: Uses modern C++ features

## Example Output

```
Test Case 1:
  Input:    [4, 2, 1, 3]
  Expected: [1, 2, 3, 4]
  Output:   [1, 2, 3, 4]
  Status:   [PASS]

========================================
Results: 4 passed, 0 failed out of 4
```
