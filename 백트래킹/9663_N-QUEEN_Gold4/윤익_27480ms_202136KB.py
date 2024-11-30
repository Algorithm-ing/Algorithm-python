N=int(input())
used=[0]*N
def check(x):
    for i in range(x):
        if used[i] == used[x] or abs(used[x]-used[i]) == x-i: return False
    return True
cnt=0
def dfs(x):
    global cnt
    if x == N: cnt+=1; return 
    if used[x]: return
    for i in range(N):
        used[x]=i
        if check(x): dfs(x+1)
        used[x]=0
dfs(0)
print(cnt)