#계수 정렬 
#모든 원소가 0보다 크거나 같다고 가정

#핵심은 모든 범위를 담을 수 있는 크기의 배열을 선언

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0] * (max(array)+1)

for i in range(len(array)) :
  count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 개수 증가

#계수 정렬 출력
for i in range(len(count)) :
  for j in range(count[i]) :
    print(i,end=' ')