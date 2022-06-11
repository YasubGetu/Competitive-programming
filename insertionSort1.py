import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    store = arr[n-1]
    for i in range(n - 1 , -1 , -1):
        if arr[i - 1] > store and i != 0:
            arr[i] = arr[i - 1]
            print(*arr)
        elif i == 0:
            arr[i] = store 
            print (*arr)
            break 
        else:
            arr[i] = store 
            print (*arr)
            break   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    
