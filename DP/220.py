#bottom up 방식 / 개미 전사

# n : 식량창고 개수
n = int(input())
# array : 각각의 식량창고에 저장되어 있는 식량
array = list(map(int,input().split()))

dp = [0] * 100

dp[0] = array[0]
dp[1] = max(array[1],array[0])

for i in range(2,n) :
  dp[i] = max(dp[i-1],dp[i-2]+array[i])

print(dp[n-1])

