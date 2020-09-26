#반복문 이진탐색 소스코드

def binary_search(array,target,start,end) :
  
  while start <= end :
    mid = (start+end) // 2

    #중간이 찾는 값일 경우
    if array[mid] == target :
      return mid

    #찾는값이 중간값보다 큰 경우 -> 오른쪽 탐색
    elif array[mid] <= target :
      start = mid + 1

    #찾는값이 중간값보다 작은 경우 -> 왼쪽 탐색
    else :
      end = mid - 1

  return None


#입력받기
n,target = map(int,input().split())

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None :
  print("원소가 존재하지 않습니다.")

else :
  print(result + 1)