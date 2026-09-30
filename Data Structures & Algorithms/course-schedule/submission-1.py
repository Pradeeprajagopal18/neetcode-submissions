class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1
            for new_course in graph[course]:
                indegree[new_course] -= 1
                if indegree[new_course] == 0:
                        queue.append(new_course)

        return finished == numCourses




        