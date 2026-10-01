class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        alice_graph, bob_graph = UnionFind(n), UnionFind(n)
        alice_edges, bob_edges = [], []
        while edges:
            edge = edges.pop()
            if edge[0] == 3:
                alice_graph.union(edge[1] - 1, edge[2] - 1)
                bob_graph.union(edge[1] - 1, edge[2] - 1)
            elif edge[0] == 2:
                alice_edges.append(edge)
            else:
                bob_edges.append(edge)
        redundant_3 = alice_graph.redundant
        for edge in alice_edges:
            alice_graph.union(edge[1] - 1, edge[2] - 1)
        redundant_1 = alice_graph.redundant
        for edge in bob_edges:
            bob_graph.union(edge[1] - 1, edge[2] - 1)
        redundant_2 = bob_graph.redundant
        if (alice_graph.component == 1) and (bob_graph.component == 1):
            return (redundant_1 + redundant_2 - redundant_3) 
        return -1

class UnionFind:
    def __init__(self, n: int):
        self.id = list(range(n))
        self.sz = [1] * n
        self.redundant, self.component = 0, n

    def root(self, i: int) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def is_connected(self, i: int, j: int)-> bool:
        self.root(i) == self.root(j)

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
        self.component -= 1