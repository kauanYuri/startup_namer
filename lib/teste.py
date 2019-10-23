l = input().split()

for x in range(len(l)):
    l[x] = int(l[x])

for i in sorted(l):
    print(i)

print()

for i in l:
    print(i)