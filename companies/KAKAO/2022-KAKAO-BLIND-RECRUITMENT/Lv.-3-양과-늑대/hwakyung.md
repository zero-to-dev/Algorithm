# 220830

## 양과 늑대(python)

### 풀이

- 스스로 해결하지 못하고 아이디어를 얻은 문제
  - 재귀 조건 설정에 대해서 막혔음
- [아이디어 풀이](https://velog.io/@youngcheon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B3%BC-%EB%8A%91%EB%8C%80-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-DFS)
  - visited 별도 객체를 설정하고 자식 및 부모 노드에 대한 방문 여부를 설정하고 재귀 호출 시, wolf의 수보다 child의 수가 더 크면 return 아니면 sheep를 리스트에 추가

```python
def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0]  = 1

    def count_sheep(sheep,wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            is_wolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = 1
                count_sheep(sheep+(is_wolf== 0),wolf+(is_wolf == 1))
                visited[child] = 0
    count_sheep(1,0)
    return max(answer)
```
