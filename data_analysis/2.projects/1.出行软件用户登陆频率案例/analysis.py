# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        傻瓜指针=head
        聪明指针=head
        for i in range(n):
            聪明指针=聪明指针.next
        if not 聪明指针:
            if 傻瓜指针.next is None:
                return None
            else:
                return 傻瓜指针.next
        while(聪明指针.next):
            聪明指针=聪明指针.next
            傻瓜指针=傻瓜指针.next
        傻瓜指针.next=傻瓜指针.next.next
        return  head