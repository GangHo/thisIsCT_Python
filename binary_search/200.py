# set을 활용한 풀이

n = int(input())

#가게에 있는 부품 번호 리스트
array = set(map(int,input().split()))


m = int(input())

#손님이 요청한 번호 리스트
x = list(map(int,input().split()))

for i in x :
  if i in array :
    print("yes",end=' ')
  else :
    print("no",end=' ')

