class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def findFromEnd(head: ListNode, k:int) -> ListNode:
    p1 = head
    
    # p1 moves k steps ahead
    for _ in range(k):
        p1 = p1.next

    p2 = head
    # p1 and p2 move n-k steps at the same time
    while p1:
        p1 = p1.next
        p2 = p2.next
        
    # p2 now points to the n-k+1 th node, which is the k-th node from the end
    return p2

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2
    kth_node = FindFromEnd(head, k)
    print(f"The {k}-th node from the end has the value: {kth_node.val}")  # Output: 4