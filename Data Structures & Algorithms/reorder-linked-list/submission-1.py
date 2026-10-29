# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        #set two pointer at the first and at the end
        # and split the list in two

        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev , curr = None, slow.next
        #split the second list
        slow.next = None
         
        #reverse second list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        #merge two list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next =second
            second.next= tmp1

            first = tmp1
            second = tmp2

        