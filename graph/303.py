from collections import deque
import copy

# v : 노드의 개수
v = int(input())
# 진입차수 행렬
indegree= [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1,v+1) :
  data = list(map(int,input().split()))
  time[i] = data[0]
  #각 강의에 대한 정보 입력(선수과목 및 진입차수)
  for x in data[1:-1] :
    indegree[i] += 1
    #선수과목이 x 인 것에 유의 ! 
    graph[x].append(i)

def topology_sort() :
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1,v+1) :
    if indegree[i] == 0 :
      q.append(i)

#q가 빌 때까지
  while q :
    #큐에서 원소 꺼내기
    now = q.popleft()
    #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
    for i in graph[now] :
      result[i] = max(result[i],result[now] + time[i])
      indegree[i] -= 1
      if indegree[i] == 0 :
        q.append(i)

  for i in range(1,v+1) :
    print(result[i])

topology_sort()




