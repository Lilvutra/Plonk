t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        sum_a = 0
        for i in range(len(arr1)):
            sum_a += arr1[i] + 1
        sum_b = sum(arr2)
