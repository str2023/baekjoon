# 백준 https://www.acmicpc.net/problem/24444
# 문제
# 오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
# 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

# 너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }
# 입력
# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
# (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 출력
# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다.
# 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

from collections import deque
import sys

input = sys.stdin.readline

def BFS(graph, R, visited):
    queue = deque() # 데큐로 큐 구현
    count = 1
    visited[R-1] = count    # 처음 정점 방문 처리
    queue.append(R)         # 큐에 삽입
    while queue:                    # 큐가 빌 때까지 반복
        node = queue.popleft()      # 큐에서 정점 꺼냄
        for i in graph[node]:       # 인접 정점 순회
            if visited[i-1] == 0:   # 방문하지 않았다면,
                count += 1          # 방문처리
                visited[i-1] = count
                queue.append(i)     # 큐에 삽입
    return visited


N, M, R = map(int, input().split())

visited = [0] * N # 방문 기록 초기화
graph = [[] for _ in range(N+1)]    # 2차원 배열 초기화

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)  # 간선 정보 입력
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()     # 오름차순으로 방문하므로 오름차 정렬

result = BFS(graph, R, visited)

print(*result, sep="\n")