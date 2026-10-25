# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node to seamlessly manage head changes
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # Step 2: Locate the k-th node of the current group
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # If there aren't enough nodes left, leave them as-is
                
            # Track the start of the next group
            groupNext = kth.next
            
            # Step 3: Reverse the current group of k nodes
            # 'prev' starts at groupNext because the first node of this reversed group 
            # will need to point directly to the beginning of the next group.
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Step 4: Fix the surrounding connections
            # Save the node that will become the new tail of this reversed group
            tmp = groupPrev.next
            # Connect the previous group's tail to the new head of this reversed group
            groupPrev.next = kth
            # Move groupPrev forward to the tail of our newly reversed group
            groupPrev = tmp
            
        return dummy.next
        
    def getKth(self, curr, k):
        # Helper function to advance k steps forward in the list
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

            
        