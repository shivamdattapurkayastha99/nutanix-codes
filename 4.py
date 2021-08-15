class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = {}
        for i in range(numCourses):
            g[i] = []
        for pre in prerequisites:
            u, v = pre[1], pre[0]
            g[u].append(v)
        order = self.topo_sort(g, numCourses)
        return order
        
    def topo_sort(self, g, n):
        visiting, visited, st = set([]), set([]), []
        for i in range(n):
            if i not in visited:
                if self.dfs(g,i,st,visiting, visited):
                    return []
        st.reverse()
        return st
    
    def dfs(self, g, i, st, visiting, visited):
        visiting.add(i)
        for nbr in g[i]:
            if nbr in visiting:
                return True
            elif nbr not in visited:
                if self.dfs(g, nbr, st, visiting, visited):
                    return True
        visited.add(i)
        visiting.remove(i)
        st.append(i)
        return False
