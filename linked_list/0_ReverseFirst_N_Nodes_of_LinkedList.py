# Change according to 206. Reverse Linked List
class Solution1:
    def reverseN(head: ListNode, n: int):
        if head is None or head.next is None:
            return head
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            n -= 1
        # 此时的 cur 是第 n + 1 个节点，head 是反转后的尾结点
        head.next = cur 
        # 此时的 pre 是反转后的头结点
        return pre

class Solution2:
    def __init__(self):
        # successor is an instance variable instead of a global variable
        self.successor = None

    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head

        # 以 head.next 为起点，反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last


# # 后驱节点
# successor = None

# # 反转以 head 为起点的 n 个节点，返回新的头结点
# def reverseN(head: ListNode, n: int):
#     global successor
#     if n == 1:
#         # 记录第 n + 1 个节点
#         successor = head.next
#         return head

#     # 以 head.next 为起点，需要反转前 n - 1 个节点
#     last = reverseN(head.next, n - 1)

#     head.next.next = head
#     # 让反转之后的 head 节点和后面的节点连起来
#     head.next = successor
#     return last 