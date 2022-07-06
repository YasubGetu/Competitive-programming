def countingSort(arr):
    if len (arr) >= 100:
        result = [0] * (100)
    else:    
        result = [0] * (max(arr) + 1)
    for num in arr:
        result[num] += 1
    return result[: 101]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
