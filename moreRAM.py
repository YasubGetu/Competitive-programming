t = int(input())
for _ in range(t):
    n , k = map(int , input().split())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    stack = []
    for i in range(n):
        stack.append([a[i],b[i]])
    stack.sort()
    for i in range(n):
        if k >= stack[i][0]:
            k += stack[i][1]
        else:
            break
    print(k)
