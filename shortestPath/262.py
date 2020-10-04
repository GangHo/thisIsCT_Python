import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n : 노드의 수, m: 간선의 수, start : 시작노드
n , m , start = map(int,input().split())

#각 노드에 연결되어 있는 노드의 정보 리스트
graph = [[] for _ in range(n+1)]

#최단거리 테이블
distance = [INF] * (n+1)

for _ in range(m) :
  a,b,c = map(int,input().split())
  #a노드에서 b노드까지 c의 비용
  graph[a].append((b,c))

def dijkstra(start) :
  q= []
  #시작 노드 설정
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q :
    dist,now = heapq.heappop(q)
    
    #중복이면 넘어간다
    if distance[now] < dist :
      continue

    for i in graph[now] :
      cost = dist + i[1]
      #i[0] 의 노드를 거쳐가는게 더 짧은 경우 
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))



dijkstra(start)

#갈 수 있는 노드 수
count = 0

#갈 수 있는 노드중에서 가장 멀리 있는 노드와의 최단거리
max_distance = 0

for d in distance :
  #도달 할 수 있는 노드인 경우
  if d != INF :
    count += 1
    max_distance = max(max_distance,d)

#시작 노드는 제외해야 하므로 count -1
print(count - 1,max_distance)


    
    








