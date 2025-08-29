for i in range(10, 0, -2):
    print(i)

for i in range(1,6):
    print([i]*i)

# num = 5
# # map = [[True for _ in range(num)] for _ in range(num)]
# map = [[True, False, False, True, True], [True, False, True, False, True], [True, True, True, True, True], [False,True,True,True,True], [False,False,True,True,True]]
num = 5
map = [[True for _ in range(num)] for _ in range(num)]

longest = []

def route(x, y, path):
    global longest

    # 현재 위치 방문 처리
    map[x][y] = False
    path.append((x, y))

    # 종료 조건
    if x == 4 and y == 4:
        if len(path) > len(longest):
            longest = path[:] # 경로를 깊은 복사로 저장
        # 돌아오기 전에 방문 상태와 경로 복원
        path.pop()
        map[x][y] = True
        return

    # 4방향 탐색 (상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < num and 0 <= ny < num and map[nx][ny]:
            route(nx, ny, path)

    # 백트래킹: 함수 호출이 끝난 후 상태 복원
    path.pop()
    map[x][y] = True

route(0, 0, [])
print(longest)