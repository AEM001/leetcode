class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        before=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=before
            before=cur
            cur=temp
            
        return before