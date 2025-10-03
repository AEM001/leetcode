def findNthFromEnd(head, n):
    slow = fast = head
    
    # 快指针先走 n 步
    for _ in range(n):
        fast = fast.next
    
    # 两个指针同时移动
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # 慢指针指向倒数第 n 个节点