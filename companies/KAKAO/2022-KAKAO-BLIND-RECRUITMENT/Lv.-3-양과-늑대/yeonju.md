### 코드
디버깅 중이었는데, 아직 미완성 상태로 일단 제출합니다! (도륵)
고쳐서 정답 맞춘 후 다시 푸시할게요! (도륵)

```python
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)

    def dfs(cur, sheep, wolf, path):

        if info[cur]:
            wolf += 1
        else:
            sheep += 1

        if sheep > wolf:
            max_sheep = sheep
        else:
            return 0

        for cur_node in path:
            for next_node in graph[cur_node]:
                if next_node not in path:
                    path.append(next_node)
                    max_sheep = max(max_sheep, dfs(cur_node, sheep, wolf, path))
                    path.pop()
        return max_sheep

    ans = dfs(0, 0, 0, [0])
    return ans

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

```