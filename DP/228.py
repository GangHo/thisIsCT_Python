# n: 화폐 단위정보, m:가치의 합

n , m = map(int,input().split())

array = []

for i in range(n) :
  array.append(int(input()))

dp = [10001] * (m+1)

dp[0] = 0

for i in array :
  for j in range(i,m+1) :
    dp[j] = min(dp[j] , dp[j-i]+1)

if dp[m] == 10001 :
  print(-1)
else :
  print(dp[m])