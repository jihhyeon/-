def solution(n, k):
    answer = 0
    
    # 소수 판별하기
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # k진수로 변환해주기
    res = ""
    while n > 0:
        res += str(n % k)
        n = n // k
    res = res[::-1]# 문자열 뒤집기    # res = "".join(reversed(res))
    res = res.split('0')
    
    for x in res:
        if x:
            answer += int(is_prime(int(x)))
    
    return answer