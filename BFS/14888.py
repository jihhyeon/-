n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))#[1,0,1,0]
max_idx = [3,1,0,2]
min_idx = [2,0,1,3]

def max(n,a,operator, max_idx):
    for i in max_idx:
        if operator[i]!=0:
            