from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def hasCycle(node, parent):
            queue = deque([node])

            while queue:
                cur = queue.popleft()
                visited.add(cur)

                for i in neighbor_list[cur]:
                    if i not in visited:
                        queue.append(i)
                        parent_list[i] = cur
                    elif i != parent_list[cur]:
                        return True

            return False
        
        neighbor_list = self.buildNeighbor(n, edges)
        visited = set()
        parent_list = [-1] * n
        if hasCycle(0, -1):
            return False
        
        return len(visited) == n
    
    
    
    def buildNeighbor(self, n, edges):
        neighbor_list = [[] for _ in range(n)]
        for v1, v2 in edges:
            neighbor_list[v1].append(v2)
            neighbor_list[v2].append(v1)
        
        return neighbor_list
    
    
    