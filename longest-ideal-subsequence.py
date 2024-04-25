class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ls = [0]*26
        ls[ord(s[n-1])-ord('a')] = 1
        for i in range(n-2 , -1 , -1):
            st = max(0 , ord(s[i])-ord('a')-k)
            ed = min(25 , ord(s[i])-ord('a')+k)
            # print("ss",st,ed)
            ans = 0
            for j in range(st,ed+1):
                ans = max(ans , ls[j])
            ls[ord(s[i])-ord('a')] = ans+1
        ans = 0
        for i in range(0,len(ls)):
            ans = max(ans , ls[i])
        
        return ans

        
obj1 = Solution()
print(4,obj1.longestIdealString('acfgbd',2))
print(4,obj1.longestIdealString('abcd',3))
print(5,obj1.longestIdealString('eduktdb',15))
print(2,obj1.longestIdealString('pvjcci',4))
# print(2,obj1.longestIdealString('pvjcci',4))

'''
                for i in range(j+1,len(s)):
                    # print("--"+lng_str[len(lng_str)-1] + " "+s[i])
                    if k-2*k-1 < ord(lng_str[len(lng_str)-1]) - ord(s[i])  and ord(lng_str[len(lng_str)-1]) - ord(s[i])  < k+1 :
                        # print(ord(lng_str[len(lng_str)-1]) , ord(s[i]))
                        lng_str = lng_str+s[i]

                                max = 0
        
        for j in range(0,len(s)):
            lng_str = 1
            if max > len(s)-j:
                break
            else:
                k_n =abs( k + (ord('a')-ord(s[j])-1))
                ls = []
                # print("j",j ," k_n",k_n)
                for i in range(j+1,len(s)):
                    ls.append(abs( ord(s[j])-ord(s[i]) ))
                    # print(  j , i , len(ls))
                    if  abs( ord(s[j])-ord(s[i]) ) < k and lng_str!= 2:
                        lng_str = 2
                        continue
                    elif lng_str > 1 and abs(abs(ord(s[j])-ord(s[i])) - ls[len(ls)-2]) < k_n:
                        # print(i-j-1)
                        # print(abs(abs(ord(s[j])-ord(s[i]))) , ls[i-j-1] , k_n)
                        lng_str+=1
                    else:
                        continue
                # print("max",max ,"lng_str",lng_str)
                if lng_str > max:
                    max = lng_str
        # print("  max",max)    
        return max
'''