# 백준 https://www.acmicpc.net/problem/1260
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
from collections import deque
import sys
input = sys.stdin.readline

def DFS(graph, V):
    visited = set() # 방문 기록을 set 구조로 선언
    stack = [V]
    while stack:    # 스택이 빌 때까지 반복
        node = stack.pop() 
        if node not in visited: # 방문하지 않았다면,
            visited.add(node)   # 방문처리
            print(node, end=' ')
            for i in reversed(graph[node]): # 오름차순으로 방문하므로 내림차 정렬 후 스택삽입
                if i not in visited:
                    stack.append(i)
    return 

def BFS(graph, V):
    visited = set() # 방문 기록을 set 구조로 선언
    queue = deque([V])
    while queue:    # 큐가 빌 때까지 반복
        node = queue.popleft()
        if node not in visited:     # 방문하지 않았다면,
            visited.add(node)       # 방문처리
            print(node, end=' ')
            for i in graph[node]:
                if i not in visited:
                    queue.append(i)
    return



N, M, V = map(int, input().split())
graph = [set() for _ in range(N+1)] # 중복 조건이 있으므로 set 자료구조를 사용

for i in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)  # 간선 정보 입력
    graph[v].add(u)


for i in range(N+1):
    graph[i] = sorted(graph[i])

DFS(graph, V)
print()
BFS(graph, V)