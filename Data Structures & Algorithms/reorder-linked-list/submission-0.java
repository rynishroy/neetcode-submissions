/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if(head ==null || head.next ==null) return;

        ListNode slow = head;
        ListNode fast = head;
    
        // Step 1: find the middle of the list (slow/fast pointers)
        while(fast !=null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        //reverse the second list
        ListNode second = reverse(slow.next);
        slow.next = null;

        //merge two list
        ListNode first = head;
        while(second !=null){
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second;
            second.next = temp1;

            first= temp1;
            second=temp2;
        }
        
    }
    private ListNode reverse(ListNode head){
        ListNode prev=null;
        ListNode curr = head;

        while(curr !=null){
            ListNode temp1= curr.next;
            curr.next = prev;
            prev=curr;
            curr= temp1;
        }
        return prev;
    }
}
