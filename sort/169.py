#파이썬 장점 퀵 정렬 소스코드

def quick_sort(array) :
  #리스트 크기가 1이하라면 종료
  if len(array) <= 1:
    return array

  pivot = array[0] # 퀵 소트 피벗은 첫 번째 원소
  tail = array[1:] # 나머지

  #분할
  left_side = [x for x in tail if x <= pivot] # pivot 보다 작은 것들
  right_side = [x for x in tail if x > pivot] # pivot 보다 큰 것들 

  #분할 이후 왼쪽,오른쪽 각각 퀵 정렬 후 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

  

array = [5,7,9,0,3,1,6,2,4,8]

print(quick_sort(array))