# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases: one or both is None
        if not (list1 and list2):
            if (not list1) and (not list2):
                return None
            
            if not list1:
                return list2
            
            if not list2:
                return list1

        # We want to do this in place, so we need to edit one of these
        #   linked lists directly. This means we will pick it to be the one
        #   that has the smaller starting value, meaning it's the one we start
        #   with
        # NOTE: Notice I use '<=' instead of '<', this is to keep it fully
        #   consistent with how we'll compare things in the actual loop,
        #   helping us avoid equality-related edge cases
        if list1.val <= list2.val:
            merge_head = list1
            merge_curr = list1
            feed_curr = list2
        else:
            merge_head = list2
            merge_curr = list2
            feed_curr = list1
        merge_prev = None

        # For the loop you can use curr and next (checking if next is null) or
        #   curr and prev (checking if curr is null), I prefer the latter
        #   because it's more intuitive to me, and we don't have to verify
        #   as much after the loop ("verification" of start/edge case of loop
        #   gets moved to expected behaviour at the beginning, avoiding error
        #   due to invariant from properties verified at the start)
        while merge_curr and feed_curr:
            if merge_curr.val <= feed_curr.val:
                # Merge curr is next in resulting list, simply increment the
                #   merge nodes (curr and prev) and move on
                merge_prev, merge_curr = merge_curr, merge_curr.next
            else:
                # Feed curr is smaller than merge curr, put it in merge curr's
                #   place, then increment merge prev and feed curr
                merge_prev.next = feed_curr
                merge_prev = feed_curr
                feed_curr, merge_prev.next = feed_curr.next, merge_curr
        
        # If the merge list ended first, then we need to add the rest of the
        #   feed list to the end
        if not merge_curr:
            merge_prev.next = feed_curr

        return merge_head