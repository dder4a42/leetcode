#include "../utils_cpp/utils.h"
#include <fstream>

using namespace std;

class Solution {
public:
    // Wrapper method for test runner
    string solve(const vector<string>& inputs) {
        ListNode* head = io::parseListNode(inputs[0]);
        ListNode* result = insertionSortList(head);
        return io::toString(result);
    }
    
    // Main solution method
    ListNode* insertionSortList(ListNode* head) {
        if(!head || !head->next) {
            return head;
        }

        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* current = head;
        
        while(current && current->next) {
            ListNode* tmp = current->next;
            ListNode* pre = dummy;
            ListNode* p = dummy->next;
            
            while(p && p->val < tmp->val) {
                pre = p;
                p = p->next;
            }
            
            if(pre->next != tmp) {
                // Insert tmp after pre
                current->next = tmp->next;
                tmp->next = p;
                pre->next = tmp;
            } else {
                // Already in correct position, advance
                current = current->next;
            }
        }
        
        return dummy->next;
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
