"""
1. 먹을 수  있는 물고기 있는지 파악 (자기보다 크기 작은)
1-1. 한마리 이상 : bfs로 거리 측정, 거리 가장 작은 곳 가기
1-2. 한마리 : 그 물고기 먹기
2. 물고기 먹을 떄 : 그칸은 빈칸으로 두기
3. 물고기 개수만큼 먹은 후 크기 +1 하기"""
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(max(max(graph)))
fish = 2 # 물고기 크기

# def bfs():
