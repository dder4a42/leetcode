#ifndef UTILS_CPP_H
#define UTILS_CPP_H

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <functional>
#include <memory>
#include <algorithm>
#include <type_traits>

// ============== Data Structures ==============

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// ============== IO Conversion Functions ==============

namespace io {

// Parse "[1, 2, 3]" to vector<int>
inline std::vector<int> parseList(const std::string& s) {
    std::vector<int> result;
    if (s.empty() || s == "[]") return result;
    
    std::string content = s.substr(1, s.size() - 2);
    std::stringstream ss(content);
    std::string item;
    
    while (std::getline(ss, item, ',')) {
        item.erase(0, item.find_first_not_of(" \t\n\r"));
        item.erase(item.find_last_not_of(" \t\n\r") + 1);
        if (!item.empty()) {
            result.push_back(std::stoi(item));
        }
    }
    return result;
}

// Parse "[1, 2, 3]" to ListNode*
inline ListNode* parseListNode(const std::string& s) {
    std::vector<int> vals = parseList(s);
    if (vals.empty()) return nullptr;
    
    ListNode* head = new ListNode(vals[0]);
    ListNode* current = head;
    for (size_t i = 1; i < vals.size(); i++) {
        current->next = new ListNode(vals[i]);
        current = current->next;
    }
    return head;
}

inline std::string toString(const int v) {
    return std::to_string(v);
}

// Convert vector<int> to string "[1, 2, 3]" or "[1,2,3]"
inline std::string toString(const std::vector<int>& v, bool compact = false) {
    if (v.empty()) return "[]";
    
    std::string result = "[";
    for (size_t i = 0; i < v.size(); i++) {
        result += std::to_string(v[i]);
        if (i < v.size() - 1) {
            result += compact ? "," : ", ";
        }
    }
    result += "]";
    return result;
}

// Convert ListNode* to string "[1, 2, 3]" or "[1,2,3]"
inline std::string toString(ListNode* head, bool compact = false) {
    if (!head) return "[]";
    
    std::string result = "[";
    ListNode* current = head;
    while (current) {
        result += std::to_string(current->val);
        if (current->next) {
            result += compact ? "," : ", ";
        }
        current = current->next;
    }
    result += "]";
    return result;
}

// Convert vector<string> to string for multi-line inputs
inline std::string toString(const std::vector<std::string>& v) {
    std::string result;
    for (size_t i = 0; i < v.size(); i++) {
        result += v[i];
        if (i < v.size() - 1) result += "\n";
    }
    return result;
}

// Compare two lists
inline bool compareLists(ListNode* a, ListNode* b) {
    while (a && b) {
        if (a->val != b->val) return false;
        a = a->next;
        b = b->next;
    }
    return !a && !b;
}

// ============== Test Runner ==============

struct TestCase {
    std::vector<std::string> inputs;
    std::string expected;
};

inline std::string trim(const std::string& str) {
    size_t start = str.find_first_not_of(" \t\n\r");
    if (start == std::string::npos) return "";
    size_t end = str.find_last_not_of(" \t\n\r");
    return str.substr(start, end - start + 1);
}

inline std::vector<TestCase> parseTestCases(std::istream& in) {
    std::vector<TestCase> testCases;
    std::string line;
    std::vector<std::string> currentInputs;
    std::string currentExpected;
    bool expectingExpected = false;
    
    while (std::getline(in, line)) {
        std::string trimmed = trim(line);
        
        // Skip empty lines and comments
        if (trimmed.empty() || trimmed[0] == '#') continue;
        
        if (trimmed == "---") {
            expectingExpected = true;
        } else {
            if (expectingExpected) {
                currentExpected = trimmed;
                expectingExpected = false;
                
                // Save current test case
                if (!currentInputs.empty()) {
                    TestCase tc;
                    tc.inputs = currentInputs;
                    tc.expected = currentExpected;
                    testCases.push_back(tc);
                    currentInputs.clear();
                    currentExpected = "";
                }
            } else {
                currentInputs.push_back(trimmed);
            }
        }
    }
    
    // Handle last test case if no expected was given
    if (!currentInputs.empty()) {
        TestCase tc;
        tc.inputs = currentInputs;
        tc.expected = currentExpected;
        testCases.push_back(tc);
    }
    
    return testCases;
}

// Normalize string for comparison (remove spaces after commas and brackets)
inline std::string normalize(const std::string& s) {
    std::string result;
    for (size_t i = 0; i < s.size(); i++) {
        char c = s[i];
        // Skip spaces after commas and opening brackets
        if (c == ' ' && i > 0 && (s[i-1] == ',' || s[i-1] == '[')) {
            continue;
        }
        result += c;
    }
    return result;
}

// Generic test runner - solution returns a type that can be converted to string
template<typename Solution, typename RetType>
void runTests(
    Solution& sol,
    RetType (Solution::*solveMethod)(const std::vector<std::string>&),
    std::istream& in = std::cin
) {
    auto testCases = parseTestCases(in);
    
    if (testCases.empty()) {
        std::cout << "No test cases found." << std::endl;
        return;
    }
    
    int passed = 0, failed = 0;
    
    for (size_t i = 0; i < testCases.size(); i++) {
        auto& tc = testCases[i];
        
        std::cout << "Test Case " << (i + 1) << ":" << std::endl;
        std::cout << "  Input:    " << toString(tc.inputs) << std::endl;
        std::cout << "  Expected: " << tc.expected << std::endl;
        
        // Call solution method
        RetType result = (sol.*solveMethod)(tc.inputs);
        
        // Convert result to string - handle string return type directly
        std::string resultStr;
        if constexpr (std::is_same_v<RetType, std::string>) {
            resultStr = result;
        } else {
            resultStr = toString(result);
        }
        
        std::cout << "  Output:   " << resultStr << std::endl;
        
        // Normalize both for comparison
        std::string normalizedResult = normalize(resultStr);
        std::string normalizedExpected = normalize(tc.expected);
        
        if (normalizedResult == normalizedExpected) {
            std::cout << "  Status:   [PASS]" << std::endl;
            passed++;
        } else {
            std::cout << "  Status:   [FAIL]" << std::endl;
            failed++;
        }
        std::cout << std::endl;
    }
    
    std::cout << "========================================" << std::endl;
    std::cout << "Results: " << passed << " passed, " << failed << " failed out of " << testCases.size() << std::endl;
}

} // namespace io

#endif // UTILS_CPP_H
