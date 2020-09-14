n , k = map(int,input().split()) #n은 항상 k 보다 크거나 같다


count = 0   # 연산 횟수

while n!=1 :
  if n % k == 0 :
    n = n / k
    count += 1

  else :
    n = n -1
    count += 1

print(count)
