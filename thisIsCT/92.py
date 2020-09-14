n, m, k = map(int,input().split())

data = list(map(int,input().split()))

data.sort(reverse = True)

num1= data[0]
num2 = data[1]


count = 0 #연속 더한 횟수
result = 0 
for i in range(m) :
  if count == k :
    result += num2
    count = 0
  else :
    result += num1
    count += 1

print(result)