# 백준 https://www.acmicpc.net/problem/1931
# 문제
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
import sys
input = sys.stdin.readline

n = int(input())
schedule = []
for i in range(n):
    time = list(map(int, input().split()))
    schedule.append(time)

schedule.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간 오름차 정렬 이후 시작 시간 순 정렬
result = 0  # 회의 개수
prev = 0    # 이전 회의의 종료 시간
for start, end in schedule: # 시작시간 start, 종료시간 end 로 대입하며 반복
    if prev <= start:       # 이전 종료시간보다 시작시간이 같거나 늦으면,
        prev = end          # 갱신 후 결과+1
        result += 1

print(result)