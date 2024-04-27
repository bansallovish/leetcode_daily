class Solution(object):
   
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        cache = {}

        def helper(r,k):
            if k ==len(key):
                return 0
            if (r,k) in cache:
                return cache[(r,k)]
            
            res = float('inf')
            
            for i,c in enumerate(ring):
                if c == key[k]:
                    min_dist = min(abs(r-i) , n-abs(r-i))
                    res= min ( res , min_dist + 1 + helper(i,k+1))

            cache[(r,k)] = res
            return res
        
        return helper(0,0)



obj1 = Solution()
print("4",obj1.findRotateSteps("godding","gd"))
obj2 = Solution()
print("13",obj2.findRotateSteps("godding","godding"))
obj3 = Solution()
print("6",obj3.findRotateSteps("abcde","ade"))
obj4 = Solution()
print("11",obj4.findRotateSteps("iotfo","fioot"))
obj5 = Solution()
print("19",obj5.findRotateSteps("nyngl","yyynnnnnnlllggg"))
obj6 = Solution()
print("204",obj6.findRotateSteps("xrrakuulnczywjs","jrlucwzakzussrlckyjjsuwkuarnaluxnyzcnrxxwruyr"))
# print("",obj1.findRotateSteps())


'''
        print(counter)
        ginr = ring[::-1]
        for i in key:
            i1 = ring.find(i)
            i2 = ginr.find(i) + 1

            if i1 <= i2:
                counter = counter + i1 
                for j in range(0,i1):
                    temp = ring[0]
                    ring = ring[1:]
                    ring = ring + temp
                ginr = ring[::-1]
                print(i1,counter)
            else:
                counter = counter + i2
                for j in range(0,i2):
                    temp = ring[n-1]
                    ring = ring[:n-1]
                    ring =  temp + ring
                ginr = ring[::-1]
                print(i1,counter)
            
            print(ring)

        return counter
        '''
'''
        counter = self.recursion_solve(ring , key ,counter)
        return self.ans
        
    
    def recursion_solve(self ,ring , key ,counter):
        # print(ring , key ,counter)
        ginr = ring[::-1]
        if len(key) == 0:
            if counter < self.ans:
                self.ans = counter
            return counter
        else:

            n = len(ring)
            i1 = ring.find(key[0])
            c1 = counter + i1
            r1 = ring
            for j in range(0,i1):
                temp = r1[0]
                r1 = r1[1:]
                r1 = r1 + temp
            
            i2 = ginr.find(key[0]) + 1
            c2 = counter + i2
            r2 = ring
            for j in range(0,i2):
                temp = r2[n-1]
                r2 = r2[:n-1]
                r2 =  temp + r2

            if c1 < self.ans and c2< self.ans: 
                return min ( self.recursion_solve(r1 , key[1:] ,c1) , self.recursion_solve(r2 , key[1:] ,c2) )
            elif c1 > self.ans and c2< self.ans:
                return  self.recursion_solve(r2 , key[1:] ,c2) 
            else:
                return  self.recursion_solve(r1 , key[1:] ,c1) 
            
'''