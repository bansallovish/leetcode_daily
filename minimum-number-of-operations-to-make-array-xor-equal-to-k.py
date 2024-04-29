class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        n=len(nums)
        xor = self.xorOfArray(nums,n)
        # print(k , xor , type(xor))

        if xor == k:
            return cnt
        else:
            xor_b = str(self.decimalToBinary(xor))
            k_b = str(self.decimalToBinary(k))
            # print(xor,xor_b,k_b)
            if len(xor_b) > len(k_b):
                for i in range(0,len(xor_b)-len(k_b)):
                    k_b = '0'+k_b
                for i in range(0,len(xor_b)):
                    if xor_b[i] != k_b[i]:
                        cnt+=1

            elif len(xor_b) < len(k_b):
                for i in range(0,len(k_b)-len(xor_b)):
                    xor_b = '0'+xor_b
                for i in range(0,len(xor_b)):
                    if xor_b[i] != k_b[i]:
                        cnt+=1

            else:
                for i in range(0,len(xor_b)):
                    if xor_b[i] != k_b[i]:
                        cnt+=1

        return cnt
    
    def xorOfArray(self , arr, n):
    
        xor_arr = 0
        for i in range(n):
            xor_arr = xor_arr ^ arr[i]

        return xor_arr

    def decimalToBinary(self ,n): 
        return bin(n).replace("0b", "") 

obj1=Solution()
print("2",obj1.minOperations([2,1,3,4],1))
print("0",obj1.minOperations([2,0,2,0],0))
# print("2",obj1.minOperations([2,1,3,4],1))
# print("2",obj1.minOperations([2,1,3,4],1))
# print("2",obj1.minOperations([2,1,3,4],1))
# print("2",obj1.minOperations([2,1,3,4],1))