class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # if k == len(num):
        #     return "0"
        # el
        # if len(num) == k+1:
        #     min = int(num)
        #     for i in num:
        #         temp = int(i)
        #         if min > temp:
        #             min = temp
        #     return str(min)
        # else:
        min = []
        for i in num:
            while (k>0 and len(min) > 0 and int(i) < int(min[len(min)-1]) ):
                k = k-1
                min.pop()
            if (len(min) == 0 and i == '0'):
                continue
            min.append(i)
        while (k>0 and len(min) > 0):
            k = k-1
            min.pop() 

        my_string = ''.join(min)
        if len(my_string) == 0:
            return "0"
        return my_string
            


obj1 = Solution()
print("1432219", 3,obj1.removeKdigits("1432219", 3))
print("10200", 1,obj1.removeKdigits("10200", 1))
print("10", 2,obj1.removeKdigits("10", 2))
print("5334", 2,obj1.removeKdigits("5334", 2))
print("43214321", 4,obj1.removeKdigits("43214321", 4))
print("100", 1,obj1.removeKdigits("100", 1))

'''
            f_min = int(num)
            for i in range(0,int(round(2*k/3,0))+1):
            # for i in range(0,k):
                min = self.get_min(num[i:] , k-i)
                if f_min > min:
                    f_min = min
                print( i , k , k-i,f_min)
            return str(f_min)
    
    def get_min(self,num , k):
        min = int(num)
        for i in range(0,len(num)-k+1):
            temp = int(num[0:i] + num[i+k:] )
            if min > temp :
                min = temp
        return min
        
'''