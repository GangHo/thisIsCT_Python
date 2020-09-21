input_data = input()

#위치입력 / ord() : 문자 to ASCII
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 플러스1은 좌표가 1부터 시작하므로

#L,U,R,D 순 
dir = [(-1,-2),(1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1)]


count = 0

#8가지 방향에 대해 체크
for i in range(len(dir)) :
  dx = dir[i][0]
  dy = dir[i][1]

  #이동 위치
  nx = row + dx
  ny = column + dy

  #범위 나가는 경우는 제외
  if nx > 8 or ny > 8 or ny < 1 or nx < 1 :
    continue

  #제외 하고 가능한 경우 카운트
  count += 1


print(count)

#모범답안
'''
steps = [(-1,-2),(1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1)]

count = 0


for step in steps :

  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >=1 and next_row <= 8 or next_column >=1 and next_column <=8:
    count += 1

print(count)

''''