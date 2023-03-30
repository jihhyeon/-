def solution(triangle):
    for i in range(1, len(triangle)):#몇번째 줄인지
        for j in range(i+1):#j=줄안에서 인덱스
            #가장 왼쪽인 경우
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            #가장 오른쪽인 경우
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            #가운데인 경우
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])#마지막 리스트에서 최대값 뽑기