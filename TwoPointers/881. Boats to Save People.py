class Solution(object):
    def numRescueBoats(self, people, limit):
      people.sort()
      right = len(people)-1
      left =0
      boats = 0
      while left <= right:
        if people[left] + people[right] <= limit:
          left += 1
        right -= 1
        boats +=1
      return boats  


solution = Solution()
people = [1,2]
limit = 3 
result =solution.numRescueBoats(people, limit)      
print(result)