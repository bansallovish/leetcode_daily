class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        rs_ls = [0,1,1]
        for i in range(0,n-2):
            rs_ls.append(rs_ls[i]+rs_ls[i+1]+rs_ls[i+2])
            
        return rs_ls[n]

obj1 = Solution()
print("4",obj1.tribonacci(4))