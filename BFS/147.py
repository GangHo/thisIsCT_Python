from collections import deque

def bfs(graph,start,visited) :
  #queue 구현을 위한 deque사용 및 처음값
  queue = deque([start])
  #방문한 곳은 처리
  visited[start] = True

  #queue가 빌 때까지
  while queue :
    #qeue에서 하나의 원소 뽑고 출력
    v = queue.popleft()
    print(v,end=" ")
    
    #해당 원소와 연결 되어있고, 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True



graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False] * 9
bfs(graph,1,visited)