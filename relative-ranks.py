class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        descls = sorted(score, reverse=True)
        n = len(score)
        res = [0]*n
        # print(len(res))
        for i in range(0,n):
            index = descls.index(score[i])
            if index ==0:
                res[i]="Gold Medal"
            elif index == 1:
                res[i]="Silver Medal"
            elif index == 2:
                res[i]="Bronze Medal"
            else:
                res[i] = str(index+1)
        
        # print(res)
        return res

obj1=Solution()
print("",obj1.findRelativeRanks([5,4,3,2,1]))
print("",obj1.findRelativeRanks([10,3,8,9,4]))
# print("",obj1.findRelativeRanks([5,4,3,2,1]))
# print("",obj1.findRelativeRanks([5,4,3,2,1]))
# print("",obj1.findRelativeRanks([5,4,3,2,1]))