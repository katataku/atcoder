n = int(input())

a = list(map(int, input().split()))

tar = sum(a) / 10
b = [0]
acc = 0
for i in a:
    acc += i
    b.append(acc)
for i in a:
    acc += i
    b.append(acc)


ans = "No"
left = 0
right = 1
while right < 2 * n - 1:
    tmp = b[right] - b[left]
    if tar == tmp:
        ans = "Yes"
        break
    if tar > tmp:
        right += 1
    else:
        left += 1
print(ans)