def mergeTrees(self,t1,t2):
    if t1 and t2:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left,t2.left)
        t1.right = mergeTrees(t1.right,t2.right)
        return t1
    else:
        return t1 or t2