"""다리위 = w개의 트럭만 동시에 올라갈 수 있음
다리의 길이 =w단위길이
각 트럭들은 하나의 단위시간에 하나의 단위길이만큼만 이동 가능
동시 다리위에 올라가있는 트럭의 무게합은 다리의 최대하중인 l보다 작거나 같아야함
"""
n, w, l = map(int, input().split())
array = list(map(int, input().split()))

bridge = [0]*w#[0,0]
time = 0

while bridge:
    time += 1
    bridge.pop(0)#맨앞 pop!
    if array:
        if sum(bridge) + array[0] <= l:
            bridge.append(array.pop(0))
        else:
            bridge.append(0)
print(time)

