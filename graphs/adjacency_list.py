from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Step 1: Create the adjacency list using defaultdict
        prerequisite_dict = defaultdict(list)
        # or use the regular dictionary
        # prerequisite_dict = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prerequisite_dict[prereq].append(course)

        # Step 2: Initialize a set to keep track of nodes in the current path (for cycle detection)
        path_set = set()

        # Step 3: Define DFS function with a set for visited nodes
        def dfs(course):
            if course in path_set:  # Cycle detected
                return False
            if course not in prerequisite_dict:  # No dependencies, this node is safe
                return True

            # Mark the course as visiting
            path_set.add(course)

            # Visit all the courses that depend on this one
            for next_course in prerequisite_dict[course]:
                if not dfs(next_course):
                    return False

            # Remove the course from the current path and mark as fully processed
            path_set.remove(course)
            del prerequisite_dict[course]

            return True

        # Step 4: Check each course for cycles
        for course in range(numCourses):
            if course in prerequisite_dict and not dfs(course):
                return False

        # O(n) space complexity

        return True
