# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Dummy node to simplify insertion
        dummy = ListNode(0)
        dummy.next = None
        current = head

        while current:
            # Store the next node to process
            next_node = current.next

            # Find the position to insert the current node in the sorted list
            prev, pointer = dummy, dummy.next
            while pointer and pointer.val < current.val:
                prev = pointer
                pointer = pointer.next

            # Insert the current node into the sorted list
            current.next = pointer
            prev.next = current

            # Move to the next node in the original list
            current = next_node

        return dummy.next