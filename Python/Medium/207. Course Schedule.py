class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisites_num, prerequisites_list = self.get_prerequisite(numCourses, prerequisites)
        start_course = [i for i in range(numCourses) if prerequisites_num[i] == 0]
        order = []

        queue = collections.deque(start_course)
        while queue:
            p = queue.pop()
            order.append(p)

            for next_course in prerequisites_list[p]:
                prerequisites_num[next_course] -= 1
                if prerequisites_num[next_course] == 0:
                    queue.append(next_course)
                    
        if len(order) == numCourses:
            return True
        return False
                
    
    
    def get_prerequisite(self, numCourses, prerequisites):
        prerequisites_list = dict(zip(list(range(numCourses)), [ [] for _ in range(numCourses)]))
        prerequisites_num = dict(zip(list(range(numCourses)), [0] * numCourses))   
        
        for p in prerequisites:
            prerequisites_num[p[0]] = prerequisites_num.get(p[0]) + 1
            if p[1] not in prerequisites_list:
                prerequisites_list[p[1]] = [p[0]]
            else:
                prerequisites_list[p[1]].append(p[0])
        
        return prerequisites_num, prerequisites_list
        