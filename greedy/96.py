n , m = map(int,input().split())


min_Num = 0
result = 0

for i in range(n) :
  data = list(map(int,input().split()))

  min_Num = min(data)   # 행의 가장 작은 값

  result = max(result,min_Num) #행의 가장 작은 값들 중 제일 큰 값


  
print(result)


