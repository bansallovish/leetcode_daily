class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # print(people,type(people))
        people.sort()
        # print(people)
        res = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            res += 1
        
        return res




obj1=Solution()
print("1",obj1.numRescueBoats([1,2],3))
print("3",obj1.numRescueBoats([3,2,2,1],3))
print("4",obj1.numRescueBoats([3,5,3,4],5))
print("2",obj1.numRescueBoats([5,1,4,2],6))
# print("",obj1.numRescueBoats())