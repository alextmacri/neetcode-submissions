# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Naive approach would be to keep a set of visited nodes and finish
        #   when either the traversal completes (no loop), or a previously
        #   visited node is reached (there is a loop). This would take O(n)
        #   space, is there a way to do this without building another data
        #   structure, but using the same intuition of either completing or
        #   detecting a loop?

        # If we make one traversal/pointer go 1 at a time (normal speed), and
        #   another traversal/pointer go 2 at a time (fast), then we can say
        #   that if one of them completes the traversal (we'll say the fast
        #   one, since it's faster), then there is no loop, but if the
        #   pointers ever meet, then there is a loop. we can say this because
        #   WHEN THE TRAVERSALS ENTER A LOOP OF LENGTH L, THEY ENTER A SYSTEM
        #   OF MOD L. This means that, since the traversals move at a speed
        #   with a difference of 1, then their modular distance decreases by 1
        #   each time, meaning it will take at most L "ticks" to have the
        #   traversals meet (and L < n, meaning it will be O(n) "ticks" total)

        # Edge cases: No head, next, or next next
        if not (head and head.next and head.next.next):
            return False
        
        # Instantiate traversals, start them both at the beginning since the
        #   "step" will happen at the beginning of the loop, before equality
        #   is checked
        trav_slow = head
        trav_fast = head

        # Condition needs to check for fast and fast's next for None (since it
        #   goes "2 at a time", meaning it's possible for the fast's next node
        #   to be None and try to skip over it). Don't need to check for
        #   slow's status since it has "already been checked" by fast
        while trav_fast and trav_fast.next:
            # Increment
            trav_slow = trav_slow.next
            trav_fast = trav_fast.next.next

            # Check
            if trav_slow == trav_fast:
                return True
        
        # List has been fully traversed through, so there is no loop
        return False