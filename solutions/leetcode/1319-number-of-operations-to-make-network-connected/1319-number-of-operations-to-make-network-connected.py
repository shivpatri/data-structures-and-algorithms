class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)
        if uf.components <= uf.redundant + 1:
            return uf.components - 1
        else:
            return -1
            
class UnionFind:
    def __init__(self, n: int):
        self.id, self.sz = [], []
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)
        self.components, self.redundant = n, 0
    
    def root(self, i: int) -> int:
        while self.id[i] != i:
            self.id[i] = self.id[self.id[i]] # Path Compression
            i = self.id[i]
        return i

    def is_connected(self, i: int, j: int) -> bool:
        return self.root(i) == self.root(j)

    def union(self, i: int, j: int):
        p = self.root(i)
        q = self.root(j)
        if p == q:
            self.redundant += 1
            return
        elif self.sz[p] > self.sz[q]:
            self.id[q] = p
            self.sz[p] += self.sz[q]
        else:
            self.id[p] = q
            self.sz[q] += self.sz[p]
        
        self.components -= 1