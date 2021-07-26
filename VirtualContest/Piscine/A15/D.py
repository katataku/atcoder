n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

ng_list = [ng1, ng2, ng3]

memo = [-1 for i in range(301)]


def solve(n, cnt):
    if cnt == 0 or n in ng_list:
        return 0
    if memo[n] != -1:
        return memo[n]
    if n == 1 or n == 2 or n == 3:
        memo[n] = 1
    else:
        tmp = 0
        if n - 3 not in ng_list:
            tmp += solve(n - 3, cnt - 1)
        if n - 2 not in ng_list and tmp == 0:
            tmp += solve(n - 2, cnt - 1)
        if n - 1 not in ng_list and tmp == 0:
            tmp += solve(n - 1, cnt - 1)
        memo[n] = tmp
    return memo[n]


ans = solve(n, 100)
if ans == 1:
    print("YES")
else:
    print("NO")
