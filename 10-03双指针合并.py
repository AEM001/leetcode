class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，简化操作
        dummy = ListNode(-1)
        curr = dummy
        
        # 分离双指针：分别遍历两个链表
        while list1 and list2:
            if list1.val <= list2.val:
                # 选择 list1 的当前节点
                curr.next = list1
                list1 = list1.next
            else:
                # 选择 list2 的当前节点
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # 处理剩余节点
        curr.next = list1 if list1 else list2
        
        return dummy.next