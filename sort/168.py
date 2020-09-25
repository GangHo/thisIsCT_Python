#일반적인 퀵 정렬 소스코드

def quick_sort(array,start,end) :
  if start >= end : #원소가 1개라면 종료
    return

  pivot = start #리스트의 첫번째 원소가 pivot
  left = start + 1
  right = end

  while left <= right :
    # pivot보다 큰 데이터를 찾을 때 까지 반복 (왼쪽)
    while left <= end and array[left] <= array[pivot]:
      left += 1

    # pivot보다 작은 데이터를 찾을 때 까지 반복 (오른쪽)
    while right > start and array[right] >= array[pivot]:
      right -= 1

    if left > right : # 찾은값이 교차된다면 작은값과 pivot 교환
      array[pivot],array[right] = array[right],array[pivot]

    else : # 교차되지 않았다면 작은값과 큰값 교환
      array[left],array[right] = array[right],array[left]


  quick_sort(array,start,right-1) #분할이후 왼쪽에서 정렬 수행
  quick_sort(array,right+1,end) #분할이후 오른쪽에서 정렬 수행



#test case
array= [5,7,9,0,3,1,6,2,4,8]

quick_sort(array,0,len(array)-1)
print(array)

