import sys

lottos = list(map(int,sys.stdin.readline().split()))
win_nums = list(map(int,sys.stdin.readline().split()))


def solution(lottos,win_nums):
    answer = [7,7]

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            answer[0] -= 1
            answer[1] -= 1 

        if lottos[i] == 0 :
            answer[0] -= 1
        
        if sum(lottos) == 0 :
            answer[0] = 1
            answer[1] = 6


    
    return answer

print(solution(lottos,win_nums))

