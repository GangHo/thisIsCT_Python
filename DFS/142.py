# DFS 메소드 정의 ( 재귀 )
def dfs(graph, v, visited) :
  #현재 방문한 노드 체크
  visited[v] = True
  print(v, end=' ')
  
  for i in graph[v] :
    #현재 노드와 인접한 노드들 방문 체크
    if not visited[i] :
      dfs(graph,i,visited)


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

dfs(graph,1,visited)
