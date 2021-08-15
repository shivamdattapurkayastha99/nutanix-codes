# populating next right pointers in each node 
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        k=1
        q=deque()
        q.append(root)
        while q:
            for i in range(k):
                if i<(k-1): q[i].next = q[i+1]
                if q[i].left: q.append(q[i].left)
                if q[i].right: q.append(q[i].right)
            for i in range(k): q.popleft()
            k<<=1