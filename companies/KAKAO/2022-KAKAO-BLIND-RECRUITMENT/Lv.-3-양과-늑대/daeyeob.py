# 피보나치 함수를 재귀로 구현할 때 중복이 발생하는 문제를 메모이제이션으로 해결한것 처럼
# 비트마스킹을 이용하여 vis[...]에 특정 상태를 방문했는지를 저장
# {0,1,7,8,9}번 정점을 방문한 상태는 1110000011 = 899로 나타내어 vis[899]를 1로 만듦
# 각 상태를 정점으로 나타냄



def solution(info, edges):
    visited = [0]*len(info)
    visited[0] = 1   # 루트 노드에는 항상 양이 존재
    result = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            result.append(sheep)
        else:   # 늑대의 수가 양의 수보다 크거나 같은 케이스
            return   # 모든 양을 잡아 먹어버린 것

        for idx in range(len(edges)):
            parent = edges[idx][0]
            child = edges[idx][1]
            isWolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(isWolf==0), wolf+(isWolf==1))
                visited[child]=0

    dfs(1,0)
    return max(result)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))


'''
다른 칸으로 건너갈 수 있는 조건
1. 부모 노드를 먼저 방문했는가
2. 자식 노드를 방문한 적이 있는가


'''