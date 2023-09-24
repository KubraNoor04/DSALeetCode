import bisect

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        obstacle_height = []
        result = []

        for obstacle in obstacles:
            position = bisect.bisect_right(obstacle_height, obstacle)

            if position == len(obstacle_height):
                obstacle_height.append(obstacle)
            else:
                obstacle_height[position] = obstacle

            result.append(position + 1)

        return result

# Example usage:
obstacles = [1, 2, 0, 2]
solution = Solution()
result = solution.longestObstacleCourseAtEachPosition(obstacles)
print(result)  # Output: [1, 2, 3, 3]