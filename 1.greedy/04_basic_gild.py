# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 ‘공포도’를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.

# 모험가 길드장은 모험가 그룹을 안전하게 구성하자 **공포도가 X인 모험가는 반드시 X명 이상으로 구성**한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.

# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

# 예를 들어 N=5이고, 각 모험가의 공포도가 2 3 1 2 2 라고 가정.

# 이 경우 그룹 1에 공포도가 1, 2 ,3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면 총 2개의 그룹을 만들 수 있다.

# 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때고문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없다.

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for score in data:
    count += 1
    if score <= count:  # 공포도가 현재 그룹에 포함된 모험가의 수보다 작거나 같다면 그룹 결성 완료
        result += 1
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)
