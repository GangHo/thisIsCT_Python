# 최소 신장 트리중 가장 비용이 큰 간선을 빼 두개의 도시로 나눈다

def find_parent(parent,x) :
  if parent[x] != x :
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union_parent(parent,a,b) :
  a = find_parent(parent,a)
  b = find_parent(parent,b)

  if a < b :
    parent[b] = a
  else :
    parent[a] = b

# n : 집(노드) 개수 , m : 길(간선) 개수
n, m = map(int,input().split())

parent = [0] * (n+1)

for i in range(1,n+1) :
  parent[i] = i

edges=[]

for _ in range(m) :
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

edges.sort()
last_cost = 0 # 비용 중 가장 큰 간선의 비용

result =0

for edge in edges :
  cost,a,b = edge

  if find_parent(parent,a) != find_parent(parent,b) :
    union_parent(parent,a,b)

    result += cost

    last_cost = cost

print(result - last_cost)

  

