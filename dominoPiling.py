a = input().split()
i = min(int(a[0]) , int(a[1]))
while 2 * i <= (int(a[0]) * int(a[1])):
    i += 1
print (i - 1)
