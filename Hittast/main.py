import heapq


def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        currdist, currnode = heapq.heappop(pq)
        if currdist > dist[currnode]:
            continue
        for n, w in graph[currnode]:
            distance = currdist + w
            if distance < dist[n]:
                dist[n] = distance
                heapq.heappush(pq, (distance, n))
    return dist


n, m = map(int, input().split())
costs = list(map(int, input().split()))
alf = [[] for _ in range(n + 1)]
graph_benedikt = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost_alf, cost_ben = map(int, input().split())
    alf[a].append((b, cost_alf))
    alf[b].append((a, cost_alf))
    graph_benedikt[a].append((b, cost_ben))
    graph_benedikt[b].append((a, cost_ben))

dist_alf = dijkstra(alf, 1, n)
dist_ben = dijkstra(graph_benedikt, n, n)
min_cost = float('inf')
for i in range(1, n + 1):
    total = dist_alf[i] + dist_ben[i] + costs[i - 1]
    min_cost = min(min_cost, total)

print(min_cost)
