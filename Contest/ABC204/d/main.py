# -*- coding: utf-8 -*-

n = int(input())

tlist = list(map(int, input().split()))
tlist.sort(reverse=True)

tlistsum = sum(tlist)


def check(tar, objlist):
    if tar == 0 or sum(objlist) == tar:
        return True
    if tar < 0 or tar > sum(objlist):
        return False
    return check(tar - objlist[0], objlist[1:]) or check(tar, objlist[1:])


ans = 0

tarlist = []
if check((tlistsum + 1) // 2, tlist):
    ans = (tlistsum + 1) // 2
else:
    left = (tlistsum + 1) // 2
    right = tlistsum
    while right - left != 1:
        tar = (right + left) // 2
        if tar in tarlist:
            print("-1")
            break
        tarlist.append(tar)
        if check(tar, tlist):
            right = tar
        else:
            left = tar
    ans = right
print(ans)
