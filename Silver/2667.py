# 백준 https://www.acmicpc.net/problem/2667
# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

def DFS(x, y):
    global count    # 집 숫자 전역 변수 선언
    if x < 0 or x >= N or y < 0 or y >= N:  # 범위를 벗어나는 경우 반환
        return False
    if graph[x][y] == "1":  # 해당 포커스가 집이면,
        count += 1          # 집 숫자 +1
        graph[x][y] = "0"   # 방문했으므로 0으로 변경
        DFS(x-1, y)         # 상
        DFS(x, y-1)         # 좌
        DFS(x+1, y)         # 하
        DFS(x, y+1)         # 우 탐색
        return True         # 참 반환
    return False

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(input())
    
house = []  # 단지 초기화
count = 0
for i in range(N):
    for j in range(N):  # 모든 구역 탐색
        if DFS(i, j):           # 단지 탐색이 끝나면,
            house.append(count) # 단지에 집 개수 삽입
            count = 0           # 집 개수 초기화

print(len(house))
print(*sorted(house), sep="\n")