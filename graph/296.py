from collections import deque

# v : 노드의 개수, e : 간선의 개수
v , e = map(int,input().split())
# 모든 노드들의 진입차수를 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보 연결
graph = [[]for i in range(v+1)]

#방향 그래프의 모든 간선 정보 입력받기
for _ in range(e) :
  a,b = map(int,input().split())
  graph[a].append(b)
  #a->b 진입차수 1증가
  indegree[b] += 1

#위상 정렬 함수
def topology_sort() :
  result = []
  q = deque()

  #처음 시작은 진입차수가 0인 노드를 삽입해야함
  for i in range(1,v+1) :
    if indegree[i] == 0 :
      q.append(i)

  # 큐가 빌 때까지
  while q:
    
    now = q.popleft()
    result.append(now)

    #해당 원소와 연결된 노드들의 진입차수 1 감소
    for i in graph[now] :
      indegree[i] -= 1
      #새로 집입차수가 0인 노드를 넣는다
      if indegree[i] == 0 :
        q.append(i)

  
  for i in result :
    print(i,end=' ')

topology_sort()



