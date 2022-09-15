# 20220915 등산코스 정하기

### 풀이
- 다익스트라 기법을 이용하여 풀이
- 시간 초과를 방지하기 위해 heapq 사용
  
```python
import heapq
def solution(n, paths, gates, summits):
    graphes = [[] for _ in range(n+1)]
    summits.sort() 
    for path in paths:
        start,end,weight = path[0],path[1],path[2]
        graphes[start].append((end,weight)) # 양방향으로 이동할 수 있기 때문에 시작 노드, 끝 노드 모든 추가
        graphes[end].append((start, weight))

    def dijkstra(q): # zb
        while q:
            distance, current = heapq.heappop(q)
            if distances[current] < distance or current in summits : # 만약 현재 intensity 보다 더 크거나 정상에 도착 시
                continue

            for graph in graphes[current]:
                temp = max(distance, graph[1]) 
                if distances[graph[0]] > temp   :
                    distances[graph[0]] = temp
                    heapq.heappush(q,(temp, graph[0]))
        # 가장 작은 intensity를 가진 값을 반환하기 위해 설정
        result_intensity = {}
        for s in summits:
            result_intensity[s] = distances[s]
        result = sorted(result_intensity.items(),key = lambda x :x[1])
        return [result[0][0], result[0][1]]

    distances = (n + 1) * [float('INF')]
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))

    return dijkstra(q)
```