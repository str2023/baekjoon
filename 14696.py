# 백준 https://www.acmicpc.net/problem/14696
# 문제
# 두 어린이 A, B가 딱지놀이를 한다. 딱지놀이 규칙은 다음과 같다. 두 어린이는 처음에 여러 장의 딱지를 가지고 있고,
# 매 라운드마다 각자 자신이 가진 딱지 중 하나를 낸다. 딱지에는 별(★), 동그라미(●), 네모(■), 세모(▲), 네 가지 모양 중 하나 이상의 모양이 표시되어 있다.
# 두 어린이가 낸 딱지 중 어느 쪽이 더 강력한 것인지는 다음 규칙을 따른다.

# 만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
# 별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
# 예를 들어, 두 어린이 A, B가 낸 딱지가 다음 그림과 같다고 하자.



# 위 규칙을 따르면 A의 딱지는 별 하나를 가지고 있고 B의 딱지는 별이 없으므로 승자는 A이다.
# 위의 그림이 라운드 1의 상황이었고, 라운드 2, 3, 4, 5의 상황이 아래 표와 같을 때, 라운드 2, 3, 4의 승자는 각각 B, B, A이며,
# 라운드 5에서는 무승부가 되어 이를 D로 표현하였다.

# 라운드	A의 딱지	B의 딱지	결과
# 1	    ★	         ●●■▲	    A
# 2	    ■★●■▲   	★●●▲	   B
# 3	    ●■▲▲	      ■●■▲       B
# 4	    ★●■▲	     ★●■	   A
# 5	    ★★■●▲     	★■★▲●	  D
# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1로 표현한다.
# 예를 들어, 라운드 1의 경우 어린이 A가 낸 딱지의 그림 ★는 4로 표현할 수 있고, 어린이 B가 낸 딱지의 그림 ●●■▲는 3 3 2 1 로 표현할 수 있다.

# 라운드의 수 N과 두 어린이가 순서대로 내는 딱지의 정보가 주어졌을 때, 각 라운드별로 딱지놀이의 결과를 구하는 프로그램을 작성하시오.

# 입력
# 표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 딱지놀이의 총 라운드 수를 나타내는 자연수 N이 주어진다. N 은 1 이상 1,000 이하이다.
# 다음 줄에는 라운드 1에서 어린이 A가 내는 딱지에 나온 그림의 총 개수 a가 주어진다. a는 1 이상 100 이하이다.
# 뒤따라 나오는 a개의 정수는 어린이 A가 낸 딱지의 그림을 나타내는데, 각각 4, 3, 2, 1 중 하나의 값이다.
# 4, 3, 2, 1의 순서대로 주어지지 않을 수 있음에 주의하라.
# 다음 줄에는 라운드 1에서 어린이 B가 내는 딱지에 나온 그림의 총 개수 b가 주어진다. b도 1 이상 100 이하이다.
# 뒤따라 나오는 b개의 정수는 어린이 B가 낸 딱지의 그림을 나타내는데, 역시 4, 3, 2, 1 중 하나의 값이다.
# 역시 4, 3, 2, 1의 순서대로 주어지지 않을 수 있음에 주의하라.
# 다음 두 줄에는 라운드 2에서 어린이 A, B가 낸 딱지의 그림들을 같은 식으로 표현한다.
# 위와 같은 식으로 매 라운드마다 두 어린이가 낸 딱지의 정보는 두 줄에 표현되며, N 라운드의 딱지 정보는 차례대로 총 2N 개의 줄에 주어진다.

# 출력
# 표준 출력으로 총 N 줄을 출력한다.
# 출력의 i번째 (1 ≤ i ≤ N) 줄에 정확히 한 글자를 출력하는데, 출력하는 글자는 A, B, D 중 하나로 라운드 i의 결과를 나타낸다.
# 각 라운드의 결과는 A가 승자라면 A, B가 승자라면 B, 무승부라면 D이다.

def counting(card):
    result = []
    for i in range(1, 5):
        result.insert(0, card.count(str(i)))
    return result

n = int(input())
round = []
for i in range(n):
    aCard = counting(input().split()[1:])
    bCard = counting(input().split()[1:])
    for j in range(4):
        if aCard[j] > bCard[j]:
            round.append('A')
            break
        elif aCard[j] < bCard[j]:
            round.append('B')
            break
        elif j == 3:
            round.append('D')
    print(round[i])

# for i in range(n):
#     print(round[i])
