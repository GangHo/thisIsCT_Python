#이진 탐색 풀이
#시간복잡도 O((M+N)logN))

def binary_search(array,target,start,end) :
  while start <= end :
    
    mid = (start + end) // 2

    if array[mid] == target :
      return mid

    elif array[mid] <= target :
      start = mid + 1
    
    else :
      end = mid - 1

  return None


#가게 부품
n = int(input())
array = list(map(int,input().split()))

#이진탐색은 정렬 되어 있어야 함
array.sort()

#손님이 찾는 부품
m = int(input())
data = list(map(int,input().split()))

#답을 찾는 과정
for i in data :
  answer = binary_search(array,i,0,n-1)

  if answer != None :
    print('yes',end=' ')
  else :
    print('no',end=' ')

