class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        dict={}
        for i in nums:
            if i in dict:
                continue
            else:
                dict[i]=1
                if -1*i in dict:
                    if abs(i) > max:
                        max = abs(i)
        
        if max ==0:
            return -1
        return max
        

obj1=Solution()
print("3",obj1.findMaxK([-1,2,-3,3]))
print("7",obj1.findMaxK([-1,10,6,7,-7,1]))
print("-1",obj1.findMaxK([-10,8,6,7,-2,-3]))
print("-1",obj1.findMaxK([-9,-43,24,-23,-16,-30,-38,-30]))
# print("",obj1.findMaxK())