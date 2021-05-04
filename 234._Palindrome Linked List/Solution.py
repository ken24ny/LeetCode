# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list = []
        reverselist = []
        while head is not None:
            list.append(head.val)
            head = head.next

        index = len(list) - 1
        for i in range(0,len(list)):
            print(index)
            reverselist.append(list[index])
            index = index - 1
        
        print(list)
        print(reverselist)
        if list == reverselist:
            return True
        else:
            return False

        
node1 = ListNode(1,None)
node2 = ListNode(2,node1)      
node3 = ListNode(2,node2)      
node4 = ListNode(1,node3)

sol = Solution()
print(sol.isPalindrome(node4))
