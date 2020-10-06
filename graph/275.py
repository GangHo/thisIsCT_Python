def find_parent(parent,x) :
  #루트 노드가 아니라면 , 루트를 찾을때 까지 재귀
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
v , e = map(int,input().split())
#부모테이블 선언
parent = [0] * (v+1)
#보모노드를 부모 자기 자신으로 초기화
for i in range(1,v+1) :
  parent[i] = i

#결합연산 수행
for i in range(e) :
  a , b = map(int,input().split())
  union_parent(parent,a,b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end=' ')
for i in range(1,v+1) :
  print(find_parent(parent,i),end=' ')

print()
#부모노드 출력
print('부모노드 출력 : ',end=' ')
for i in range(1,v+1) :
  print(parent[i],end=' ')




  
