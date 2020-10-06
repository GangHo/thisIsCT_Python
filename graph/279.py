
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

# v : 노드의 개수, e : 간선의 개수
v,e= map(int,input().split())

#부모 노드 선언
parent = [0] * (v+1)

#부모 노드를 자기 자신으로 초기화
for i in range(1,v+1) :
  parent[i] = i

cycle = False

for i in range(e) :
  a , b = map(int,input().split())

  if find_parent(parent,a) == find_parent(parent,b) :
    cycle = True
    break
  else :
    union_parent(parent,a,b)


if cycle :
  print("사이클이 발생 했습니다.")
else :
  print("사이클이 발생하지 않았습니다.")


