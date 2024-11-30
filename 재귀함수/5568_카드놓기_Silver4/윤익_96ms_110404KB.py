from itertools import permutations
n,k=int(input()),int(input())
nums=[input() for _ in range(n)]
print(len(set([''.join(perm) for perm in permutations(nums,k)])))