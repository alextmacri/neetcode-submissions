# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case 1: no head
        if not head:
            return None
        
        # Edge case 2: just head
        if not head.next:
            return head
        
        # We can traverse the linked list and just reverse the pointers as we
        #   go to make the solution in-place as long as we are careful with
        #   our pointers and when we choose to replace things (i.e. we need to
        #   get the current and next before we switch current's next. After
        #   covering the first two edge cases, we know that there must be a
        #   head node and next node, from there we can arbitrarily continue
        #   to traverse until there's no next next node
        prev_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            prev_node, curr_node.next = curr_node, prev_node
            curr_node = next_node
        
        # Don't forget to set the final node to be the new head
        head = prev_node

        return head
            