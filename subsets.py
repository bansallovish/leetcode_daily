class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        print(n , nums)
        if n > 0:
            res = [[],[nums[0]]]
        else:
            return [[]]
        print("res ",res)

        def abc(ls1,a):
            for j in range(0,len(ls1)):
                ls1[j].append(a)
            return ls1

        for i in range(1,n):
            temp = abc(res,nums[i])

            print("res ",res ,"temp ", temp)
            res.extend(temp)
            print("res ",res)



        return res
    
obj1=Solution()
print(obj1.subsets([1,2,3]))