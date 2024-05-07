
def traverse_linked_list(head):
    current = head
    while current is not None:
        print(current.val),
        current = current.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        str1 = ''
        cur = head
        while cur is not None:
            str1 = str1 + str(cur.val)
            cur = cur.next

        str1 = str(2*int(str1))
        cur = head
        # traverse_linked_list(head)
        # print(str1)

        for i in range(0,len(str1)):
            print(i,str1[i],cur.val)
            cur.val = int(str1[i])
            if cur.next is None and i != len(str1) -1:
                cur.next = ListNode(0)
                # print(cur.val , cur.next.val)
                cur = cur.next
                # print(str1[i],cur.val)
                # exit()
            else:
                cur = cur.next
                # exit()

        return head


obj1 = ListNode(7)
obj2 = ListNode(8)
obj3 = ListNode(9)

obj1.next = obj2
obj2.next = obj3

test1=Solution()
# print("",test1.doubleIt(obj1))
print("",test1.doubleIt(obj1),traverse_linked_list(obj1))