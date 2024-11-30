N,poles,moves=int(input()),set([1,2,3]),[]
def tower_of_hanoi(floors, start, end, cnt=0):
    if floors==1:
        cnt+=1 
        moves.append(f'{start} {end}'); return cnt
    rest=(poles - {start,end}).pop()
    cnt=tower_of_hanoi(floors-1,start,rest,cnt)
    cnt=tower_of_hanoi(1,start,end,cnt)
    cnt=tower_of_hanoi(floors-1,rest,end,cnt)
    return cnt
if N<21:
    print(tower_of_hanoi(N,1,3))
    for move in moves: print(move)
else:
    cnt=0
    while N:cnt=cnt*2+1; N-=1
    print(cnt)