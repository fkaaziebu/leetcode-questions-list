from ast import List
from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads, seats):
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        self.ans = 0

        def dfs(i, prev, people=1):
            for x in graph[i]:
                if x == prev:
                    continue
                people += dfs(x, i)
            self.ans += (int(ceil(people / seats)) if i else 0)
            return people

        dfs(0, 0)
        return self.ans


obj = Solution()
roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats = 2
print(obj.minimumFuelCost(roads, seats))
