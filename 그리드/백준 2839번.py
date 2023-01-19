#설탕봉지 최소 문제 => 가장 큰 kg으로 나눠주기
sugar = int(input())

bag = 0
while sugar >= 0 :#설탕이 남아 있다면
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  #아니면 계속 3을 빼줌
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)#설탕이 0이 아니라 음수가 될 경우ㄹㅇㄴ
