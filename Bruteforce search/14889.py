"""조합 방법"""
"""from itertools import combinations, permutations
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
lineup = [i for i in range(1, n+1)]
lineup = deque(list(combinations(lineup, n//2)))
ans = int(1e9)

def cal(team):
    skill = 0
    case = deque(list(combinations(team, 2)))

    while case:
        s1, s2 = case.popleft()
        skill += s[s1-1][s2-1] + s[s2-1][s1-1]
    return skill


# 1. 앞에서 한개, 뒤에서 한개 => 팀 조합
for i in range(len(lineup)//2):
    start = lineup.popleft()
    link = lineup.pop()
    s_skill = cal(start)
    l_skill = cal(link)
    ans = min(ans, abs(s_skill - l_skill))
print(ans)"""


"""백트래킹 방법"""


def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)