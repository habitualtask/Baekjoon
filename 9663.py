def Chess(i):
    for j in range(i):
        if row[i] == row[j]:            #같은 열 검사
            return False
        if abs(row[j]-row[i]) == abs(j-i): #대각선 검사
            return False
    return True
 
def queen(i):
    global result                       #전역변수 result 끌어다 씀
    if i == N:
        result += 1                     #가능한 경우의 수
    else:
        for j in range(N):              #다음 열로 넘어감
            row[i] = j                  #새 퀸을 열에 넣는다
            if Chess(i):
                queen(i+1)

N = int(input())
row = [0]*15                            #1< n <15
result = 0
queen(0)
print(result)