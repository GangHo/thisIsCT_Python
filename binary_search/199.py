#계수 정렬 풀이

n = int(input())
count = [0] * 1000000

array = list(map(int,input().split()))

#가게에 있는 전체 번호 기록
for i in array :
  count[int(i)] = 1

m = int(input())

data = list(map(int,input().split()))

for i in data :
  if count[i] == 1:
    print('yes',end=' ')
  
  else :
    print('no',end=' ')

