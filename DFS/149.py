
n,m = map(int,input().split())

graph = []

for i in range(n) :
  graph.append(list(map(int,input())))


def dfs(x,y) :
  #범위가 벗어난 경우 제외
  if x >= n or x <= -1 or y >= m or y <= -1 :
    return False

  #현재 노드 방문 체크
  if graph[x][y] == 0 :
    graph[x][y] = 1

    #상,하,좌,우 재귀
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

  return False

result = 0

for i in range(n) :
  for j in range(m) :
    # i,j 위치에서 DFS 완료시 카운트
    if dfs(i,j) == True :
      result += 1

print(result)

