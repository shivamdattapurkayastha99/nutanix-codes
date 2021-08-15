# course schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [set() for i in range(numCourses)]
        for i, j in prerequisites:
            
            adj_list[j].add(i)

        
        state = [0] * numCourses
        
        finished = False

        def dfs(ls, u):
        
            nonlocal finished

            
            if finished:
                return

            
            state[u] = 1

            
            for e in ls[u]:
                
                if state[e] == 0:
                    dfs(ls, e)
                
                elif state[e] == 1:
                    finished = True

                
                if finished:
                    return

            
            state[u] = 2


        for i in range(numCourses):
            if state[i] == 0 and not finished:
                dfs(adj_list, i)

        return not finished