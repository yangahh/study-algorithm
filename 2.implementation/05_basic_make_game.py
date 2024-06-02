'''
[게임 개발]
게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 직사각형으로,
각각의 칸은 육지 또는 바다이다

캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A. B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다

캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼은 이러하다
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는,
    바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에,
캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

- 입력 조건
1. 첫째 줄에 맵의 세로크기 N과 가로 크기 M을 공백으로 구분하여 입력(N >= 3, M <= 50)
2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A, B)와 바라보는 방향 d가 서로 공백으로 구분하여 주어진다. 방향 d의 값은 다음과 같다.
    - 0: 북쪽
    - 1: 동쪽
    - 2: 남쪽
    - 3: 서쪽
3. 셋째 줄부터 맵이 육지인지 바다인지 입력한다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
    맵의 외각은 항상 바다로 되어 있다. (0: 육지, 1: 바다)
4. 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
면
- 출력 조건
첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
'''
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
x, y, d = map(int, sys.stdin.readline().rstrip().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 북, 동, 남, 서 순서로 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited_map = [[0] * m for _ in range(n)]
visited_map[x][y] = 1


def turn_left(d, x, y):
    nd = d - 1
    if nd == -1:
        nd = 2
    nx = x + dx[nd]
    ny = y + dy[nd]
    return nd, nx, ny


def move_back(d, x, y):
    nd = d + 2
    if nd >= 4:
        nd = 4 - nd
    nx = x + dx[nd]
    ny = y + dy[nd]
    return nd, nx, ny


turn_cnt = 0  # 한 자리에서 몇번 돌았는지(4번 채우면 뒤로 한 칸 이동)
result = 1
while True:
    nd, nx, ny = turn_left(d, x, y)
    d = nd

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        turn_cnt += 1  # index range error때문에 먼저 처리

    elif matrix[nx][ny] == 0 and visited_map[nx][ny] == 0:
        visited_map[nx][ny] = 1
        x, y = nx, ny
        turn_time = 0  # 초기화
        result += 1
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4:
        nd, nx, ny = move_back(d, x, y)
        if matrix[nx][ny] == 0:
            x, y = nx, ny
        else:  # 바다일때
            break

        turn_cnt = 0

print(result)
