#파이썬 장점 퀵 정렬 소스코드
#시간 면에서 조금 비효율적

def quick_sort(array) :
  # 리스트가 하나 이하라면 종료
  if len(array) <= 1:
    return array

  pivot = array[0] #퀵소트 첫 번째 원소는 피벗
  tail = array[1:] #피벗을 제외한 리스트

  #분할
  left_side = [x for x in tail if x <= pivot] #피벗보다 작은 값
  right_side = [x for x in tail if x > pivot] #피벗보다 큰 값

  #분할 이후 왼쪽,오른쪽 각각 정렬 후 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)


array = [5,7,9,0,3,1,6,2,4,8]

print(quick_sort(array))