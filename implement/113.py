n = int(input())

count = 0

#시
for i in range(n+1) :
  #분
  for j in range(60) :
    #초
    for k in range(60) :

       #문제 조건 숫자'3'이 포함되는 경우 
      if '3' in str(i) + str(j) + str(k) :
        count += 1


print(count)