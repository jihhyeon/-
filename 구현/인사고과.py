def solution(scores):
    answer = 1
    wanho = scores[0]
    sum_w = wanho[0] + wanho[1]
    scores.sort(key = lambda x : (-x[0], x[1]))
    flag = 0
    for score in scores:
        # 완호가 작을 경우
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        if flag <= score[1]:
            if sum_w < score[0] + score[1]:
                print(flag, score[0], score[1])
                answer += 1
            flag = score[1]
    return answer