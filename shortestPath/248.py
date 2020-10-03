import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) #무한을 의미

#n:노드의 개수 , m:간선의 개수
n,m = map(int,input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
#최단 거리 테이블 생성 및 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력
for _ in range(m) :
  a,b,c = map(int,input().split())
  #a번 노드에서 b번 노드로 가는 비용이 c
  graph[a].append((b,c))

def dijkstra(start) :
  q = []
  #시작 노드로 가는 최단경로는 0으로 하고 큐에 넣기
  
  heapq.heappush(q,(0,start))
  distance[start] = 0

  while q :
    #가장 최단 거리가 짧은 노드 정보
    dist,now = heapq.heappop(q)
    #이미 처리 된 적이 있으면 다음으로
    if distance[now] < dist :
      continue
    
    #현재 노드와 연결된 다른 노드들 확인
    for i in graph[now] :
      cost = dist +i[1]
      #현재 노드를 거쳐서 다른 노드로 가는 길이 더 짧은 경우
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))


dijkstra(start)

for i in range(1,n+1) :
  #도달 할 수 없는 경우, 무한 (INFINITY) 출력
  if distance[i] == INF :
    print('INFINITY')

  else :
    print(distance[i])

    

