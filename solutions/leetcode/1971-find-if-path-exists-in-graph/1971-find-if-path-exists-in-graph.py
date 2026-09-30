class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        while edges:
            u, v = edges.pop()
            uf.union(u, v)
        return uf.isConnected(source, destination)

class UnionFind:
    def __init__(self, n: int):
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]

    def isConnected(self, i: int, j: int) -> bool:
        return self.root(i) == self.root(j)

    def root(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    
    def union(self, i: int, j: int):
        p = self.root(i)
        q = self.root(j)
        if p == q:
            return
        if self.sz[i] < self.sz[j]:
            self.id[p] = q
            self.sz[q] += self.sz[p]
        else:
            self.id[q] = p
            self.sz[p] += self.sz[q]