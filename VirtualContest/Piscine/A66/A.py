s = input()
even = 0
odd = 0

for i in range(len(s)):
    tar = int(s[i])
    if i % 2 == 1:
        even += tar
    else:
        odd += tar

print(odd - even)