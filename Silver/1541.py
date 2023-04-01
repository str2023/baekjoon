#백준 https://www.acmicpc.net/problem/1541
# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

result = 0
num = "0"
plus = 0
minus = 0
operator = "+"
polynomial = "+"+input()+"+"
for i in polynomial:
    if i == "+":
        if operator == "+":
            plus += int(num)
            num = "0"
        else:
            minus += int(num)
            num = "0"
    elif i == "-":
        if operator == "+":
            plus += int(num)
            num = "0"
            operator = "-"
        else:
            minus += int(num)
            num = "0"
    else:
        num += i

result = plus - minus
print(result)

# "-"로 스플릿 후 각 원소를 "+"로 스플릿, 합계를 구한 뒤 첫번째 원소에서 빼면 쉽게 구함.