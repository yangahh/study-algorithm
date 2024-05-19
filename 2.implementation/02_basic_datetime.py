# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# 예를들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 한느 시각입니다.

# - 00시 00분 03초
# - 00시 13분 30초

# 반면에 다음은 3이 하나라도 포함되어 있지 않으므로 세면 안되는 시각입니다.

# - 00시 02분 55초
# - 01시 27분 45초
n = int(input())
count = 0


def check_contain_3(n):
    return '3' in str(n)


for h in range(n + 1):
    if check_contain_3(h):
        count += 3600
        continue
    for m in range(60):
        if check_contain_3(m):
            count += 60
            continue
        for s in range(60):
            if check_contain_3(s):
                count += 1

print(count)
