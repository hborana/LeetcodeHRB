class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        ListNode* dummy = new ListNode(0);  // Dummy node to simplify the new list construction
        ListNode* current = dummy;          // Pointer to construct the new list
        int sum_val = 0;                    // Variable to sum up values between zeros

        ListNode* node = head->next;        // Skip the first zero
        while (node != nullptr) {
            if (node->val == 0) {
                if (sum_val != 0) {
                    current->next = new ListNode(sum_val);
                    current = current->next;
                    sum_val = 0;
                }
            } else {
                sum_val += node->val;
            }
            node = node->next;
        }

        return dummy->next;
    }
};

// Helper function to print the linked list (for testing purposes)
void printLinkedList(ListNode* head) {
    while (head != nullptr) {
        std::cout << head->val << " -> ";
        head = head->next;
    }
    std::cout << "None" << std::endl;
}

