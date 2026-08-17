class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append([v, w])
        
        pq = []

        dist = [sys.maxsize] * n

        heapq.heappush(pq, [0, src])
        dist[src] = 0

        while pq:
            u = heapq.heappop(pq)[1]
            
            for x in adj[u]:
                v, w = x[0], x[1]
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, [dist[v] , v])
        final = {}
        for i in range(len(dist)):
            final[i] = dist[i]
            if dist[i] == sys.maxsize:
                final[i] = -1
        return final
