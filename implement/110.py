n = int(input())

plans = list(input().split()) # 여행 계획

x,y = 1,1 #처음 위치

dir = ['L','R','U','D'] #방향

dx = [0,0,-1,1] #방향 순서대로위 x의 좌표 변화값
dy = [-1,1,0,0] # ... y 좌표 변화값

for plan in plans :
  for i in range(len(dir)) :

    if plan == dir[i] :

      nx = x + dx[i]    # 방향에 맞는 좌표 변화값 적용
      ny = y + dy[i]

  if nx > n or nx < 1 or ny > n or ny < 1 : # 맵 나가는 경우
    continue

  x,y = nx, ny # 좌표 적용


print(nx,ny)