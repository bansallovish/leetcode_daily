class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            temp = max (happiness[i]-i,0)
            print(i , temp)
            res+=temp
        
        return res
        
obj1=Solution()
print("4",obj1.maximumHappinessSum([1,2,3],2),"\n")
print("1",obj1.maximumHappinessSum([1,1,1,1],2),"\n")
print("5",obj1.maximumHappinessSum([2,3,4,5],1),"\n")
# print("",obj1.maximumHappinessSum([1,2,3],2))
# print("",obj1.maximumHappinessSum([1,2,3],2))