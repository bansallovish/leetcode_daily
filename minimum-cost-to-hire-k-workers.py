class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        res=0
        n=len(quality)
        unit=[]
        for i in range(0,n):
            unit.append(quality[i])



        return res

obj1=Solution()
print("",obj1.mincostToHireWorkers([10,20,5],[70,50,30],2))
print("",obj1.mincostToHireWorkers([3,1,10,10,1],[4,8,2,2,7],3))
# print("",obj1.mincostToHireWorkers(,,))
# print("",obj1.mincostToHireWorkers(,,))
# print("",obj1.mincostToHireWorkers(,,))