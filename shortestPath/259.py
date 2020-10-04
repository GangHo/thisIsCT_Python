INF = int(1e9)

# n : 노드의 개수 , m : 간선의 개수
n , m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0
for a in range(1,n+1) :
  for b in range(1,n+1) :
    if a==b :
      graph[a][b] = 0

#간선에 대한 정보 입력
for _ in range(m) :
  a,b = map(int,input().split())
  # a,b 서로에게 가는 비용은 1임
  graph[a][b] = 1
  graph[b][a] = 1

#점화식에 따라 알고리즘 수행
for k in range(1,n+1) :
  for a in range(1,n+1) :
    for b in range(1,n+1) :
      graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

#거쳐갈 노드 k 와 목적지 노드 x
x , k = map(int,input().split())
#수행 결과 ( 1에서 출발해서 k를 거쳐 x로 도착)
distance = graph[1][k] + graph[k][x]

#갈 수 없는 경우 -1 출력
if distance >= INF :
  print("-1")
else :
  print(distance)

