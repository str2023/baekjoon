# 백준 https://www.acmicpc.net/problem/2178
# 문제
# N×M크기의 배열로 표현되는 미로가 있다.
# 1 0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
from collections import deque

def BFS(x, y):
    queue = deque()         # bfs는 큐를 이용
    queue.append((x, y))    # 큐에 루트 노드 삽입
    
    while queue:                # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # 큐에서 최상단 노드 꺼냄
        for i in range(4):      # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue        # 탐색 노드가 범위를 벗어나면 무시
            if graph[nx][ny] == 0:    # 해당 위치가 0이면 무시
                continue
            if graph[nx][ny] == 1:    # 해당 위치가 1이면,
                queue.append((nx, ny))  # 큐에 삽입
                graph[nx][ny] = graph[x][y] + 1 # 직전 위치값 +1로 변경 
            # (시작 위치(1,1)도 바뀌지만 우리가 원하는 값은 (N,M)의 값이므로 신경쓰지 않는다)

    return graph[N-1][M-1]  # 인덱스이므로 -1

dx = [-1, 1, 0, 0]  # 상하 이동
dy = [0, 0, -1, 1]  # 좌우 이동
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = BFS(0,0)

print(result)