t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int , input().split()))
    a.sort()
    start , end = 1 , n-1
    bs , rs = a[0] , 0
    no = 0
    while start <= end:

        if bs >= rs:
            bs += a[start]
            rs += a[end]
            start += 1
            end -= 1
        if bs < rs:
            print("YES")
            no += 1
            break
    if no == 0:
        print ("NO")
