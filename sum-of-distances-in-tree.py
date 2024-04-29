from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = [0]*n
        cnt = [0]*n
        if n>2:
            adj = defaultdict(list)
        elif n >1:
            res=[1,1]
            return res
        else:
            res=[0]
            return res

        for i in range(0,len(edges)):
            a= int(edges[i][0])
            b= int(edges[i][1])
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs1(cur_n , parent):
            cnt[cur_n] = 1
            for child in adj[cur_n]:
                if child != parent:
                    dfs1(child , cur_n)
                    cnt[cur_n] += cnt[child]
                    res[cur_n] += res[child] + cnt[child]
        
        def dfs2(cur_n,parent):
            for child in adj[cur_n]:
                if child != parent:
                    res[child] = res[cur_n] + n - 2*cnt[child]
                    dfs2(child , cur_n)
        
        dfs1(0,-1)
        dfs2(0,-1)

        return res


        




                    





obj1=Solution()
print("[8,12,6,10,10,10]",obj1.sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]]))
print("[0]",obj1.sumOfDistancesInTree(1,[]))
print("[1,1]",obj1.sumOfDistancesInTree(2,[[1,0]]))
print("",obj1.sumOfDistancesInTree(4,[[1,2],[3,2],[3,0]]))
print("[8,9,8,5,6]",obj1.sumOfDistancesInTree(5,[[2,3],[0,3],[4,1],[4,3]]))
# print("",obj1.sumOfDistancesInTree())
# print("",obj1.sumOfDistancesInTree())
# print("",obj1.sumOfDistancesInTree())
# print("",obj1.sumOfDistancesInTree())


'''
        for i in range(0,n):
            for j in range(0,n):
                if arr[i][j] > 0 or i==j:
                    continue
                else:
                    arr[i][j] = arr[j][i] =  self.get_dist(arr,n,i,j)

        for i in range(0,n):
            print(arr[i])
        
        for i in range(0,n):
            res.append(0)
            for j in range(0,n):
                if arr[i][j] >= 0:
                    res[i]+=arr[i][j]
                elif arr[j][i] >= 0:
                    res[i]+=arr[j][i]
                else:
                    arr[i][j] = arr[j][i] =  self.get_dist(arr,n,i,j)
                    res[i]+=arr[i][j]

        for i in range(0,n):
            print(arr[i])
        
        return res        
        
    def get_dist(self,arr,n,i,j):
        min_val = float('inf')
        for k in range(0,n):
            if arr[j][k] > 0:
                if arr[i][k] > 0:
                    # print("here")
                    min_val = min(min_val ,arr[j][k]+arr[i][k]  )
        
        if min_val == float('inf'):
            return -1
        else:
            return min_val
'''