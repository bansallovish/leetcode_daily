class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        arr.sort()
        n=len(arr)
        dt = {}
        for i in range(0,n):
            for j in range(i+1,n):
                temp = round(arr[i] / arr[j],5)
                dt[temp] = [arr[i] , arr[j]]
                res.append(temp)
        
        res.sort()
        print(dt,res)
        return dt[res[k-1]]


        
obj1=Solution()
print("[2,5]",obj1.kthSmallestPrimeFraction([1,2,3,5],3))
print("[1,7]",obj1.kthSmallestPrimeFraction([1,7],1))
# print("",obj1.kthSmallestPrimeFraction())
# print("",obj1.kthSmallestPrimeFraction())
# print("",obj1.kthSmallestPrimeFraction())