# 로또의 최고 순위와 최저 순위
# 첫번째는 본인의 번호 두번째는 당첨 번호
# 본인의 번호에서 0은 로또가 훼손되어 알수없는 수 



import sys

lottos = list(map(int,sys.stdin.readline().split()))
win_nums = list(map(int,sys.stdin.readline().split()))


def solution(lottos,win_nums):
    answer = [7,7]
    count = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            answer[0] -= 1
            answer[1] -= 1 
            count += 1

        if lottos[i] == 0 :
            answer[0] -= 1
        
        if sum(lottos) == 0 :
            answer[0] = 1
            answer[1] = 6
            count = 6

    if count == 0:
        answer[0] = 6
        answer[1] = 6

    
    return answer

print(solution(lottos,win_nums))

