class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        n1 = len(v1)
        v2 = version2.split('.')
        n2 = len(v2)
        i=0
        # print(v1,n1,v2,n2)

        while( i<n1 and i<n2 ):
            # print(int(v1[i]) , int(v2[i]))
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
            i+=1
        # print("here")
        if n1 > n2:
            for i in range(n2 , n1):
                # print("for int ",i,int(v1[i]))
                if int(v1[i]) > 0:
                    return 1
        if n2 > n1:
            for i in range(n1 , n2):
                if int(v2[i]) > 0:
                    return -1
        return 0
        

obj1=Solution()
print("0",obj1.compareVersion("1.01","1.001"))
print("0",obj1.compareVersion("1.0","1.0.0"))
print("-1",obj1.compareVersion("0.1","1.1"))
print("1",obj1.compareVersion("1.0.1","1"))
print("1",obj1.compareVersion("1.0.1.0","1"))