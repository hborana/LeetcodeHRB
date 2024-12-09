# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 

        #lets initialize 2-pointer approach 
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_h = prev

        first_h, second_h = head, second_h
        while second_h:
            temp1, temp2 = first_h.next, second_h.next
            first_h.next = second_h
            second_h.next = temp1
            first_h, second_h = temp1, temp2
        