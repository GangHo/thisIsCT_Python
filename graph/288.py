
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

# v : 노드의 개수 , e : 간선의 개수
v , e = map(int,input().split())

parent = [0] * (v+1)

edges = []
result = 0

#부모노드 초기화
for i in range(1,v+1) :
  parent[i] = i

#모든 간선에 대한 정보 입력 
for _ in range(e) :
  a, b, cost = map(int,input().split())
  #비용순으로 정려하기 위해 cost를 맨 앞
  edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#모든 간선들을 조사
for edge in edges :
  cost , a , b = edge

  #사이클 발생 안하면 트리에 포함
  if find_parent(parent,a) != find_parent(parent,b) :
    union_parent(parent,a,b)
    result += cost

print(result)
