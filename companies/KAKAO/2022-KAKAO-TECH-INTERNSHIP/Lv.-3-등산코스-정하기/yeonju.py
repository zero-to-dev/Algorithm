from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, j))

    def check_min_intensity():
        queue = []
        visited = [10000001] * (n + 1)
        for gate in gates:
            heapq.heappush(queue, (0, gate))
            visited[gate] = 0

        while queue:
            dist, node = heapq.heappop(queue)

            if node in ordered_summits:
                return [node, dist]

            for weight, next_node in graph[node]:
                new_intensity = max(dist, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heapq.heappush(queue, (new_intensity, next_node))

        return [-1, -1]

    summits.sort()
    ordered_summits = set(summits)
    return check_min_intensity()
    