#세로가 2로 고정
#n : 가로 길이

n = int(input())

dp = [0] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3,n+1) :
  dp[i] = (dp[i-1] + 2 * dp[i-2]) % 796796

print(dp[n])
