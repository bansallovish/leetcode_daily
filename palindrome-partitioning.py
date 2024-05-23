class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)

        def party(s,p):
            ls=[]
            for i in range(0,n-p+1):
                temp = s[i:i+p]
                if s[i:i+p] == reverse(s[i:i+p]):
                    ls.append(s[i:i+p])
                elif p != n :
                    ls.append(s[i+1])
                print(temp,reverse(temp))
            
            return ls
        
        def reverse(s):
            str=''
            for i in range(len(s)-1,-1,-1):
                str+=s[i]
            return str

        res = []
        for i in range(1,n+1):
            r = n%i
            if r == 0:
                ls1 = party(s,i)
            else:
                ls1 = party(s[r:n],i)

            if len(ls1) > 0:
                res.append(ls1)

            # break
        
        if n==1:
            return [[s]]
        return res



obj1=Solution()
# print("final :",obj1.partition('aab'))
# print("final :",obj1.partition('a'))
# print("final :",obj1.partition('ab'))
# print("final :",obj1.partition('bb'))
print("final :",obj1.partition('cdd'))

'''
        def party(s,p):
            ls=[]
            for i in range(0,n-p+1):
                temp = s[i:i+p]
                if s[i:i+p] == reverse(s[i:i+p]):
                    ls.append(s[i:i+p])
                elif p != n :
                    ls.append(s[i+1])
                print(temp,reverse(temp))
            
            return ls
        
        def reverse(s):
            str=''
            for i in range(len(s)-1,-1,-1):
                str+=s[i]
            return str

        res = []
        for i in range(1,n+1):
            ls1 = party(s,i)
            if len(ls1) > 0:
                res.append(ls1)

            # break
        
        if n==1:
            return [[s]]
        return res
'''