class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        UF = UnionFind(n)
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    UF.union(i, j)
        return UF.components

class UnionFind:
    def __init__(self, n: int):
        self.id = list(range(n))
        self.sz = [1] * n
        self.components = n
    
    def root(self, i: int) -> int:
        while(i != self.id[i]):
            self.id[i] = self.id[self.id[i]] # Path Compression
            i = self.id[i]
        return i

    def isConnected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p:int, q: int):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return

        if self.sz[i] > self.sz[j]:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            
        else:
            self.id[i] = j
            self.sz[j]+= self.sz[i]
        self.components -= 1
