def swapPairs(self,head):
    # To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, 
    # we need to change those three references. 
    # Instead of thinking about in what order I change them, 
    # I just change all three at once
    pre, pre.next = self,head
    while pre.next and pre.next.next:
        currNode = pre.next
        nextNode = currNode.next
        pre.next, nextNode.next, currNode.next = nextNode, currNode, nextNode.next
        pre = currNode
    return self.next


    # Solution2
    if head and head.next:
        head, head.next, head.next.next = \
            head.next, head, self.swapPairs(head.next.next)
    return head
