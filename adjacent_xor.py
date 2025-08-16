def transform_with_forward_backward(a, b):
    n = len(a)
    a = a[:]  # make a copy so we don't mutate input

    # Forward pass
    for i in range(n - 1):
        if (a[i] ^ a[i + 1]) == b[i]:
            print(f"Forward pass: a[{i}] = {a[i]}, a[{i + 1}] = {a[i + 1]}, b[{i}] = {b[i]}")
            a[i] = b[i]

    # Backward pass
    for i in range(n - 2, -1, -1):
        if (a[i] ^ a[i + 1]) == b[i]:
            print(f"Backward pass: a[{i}] = {a[i]}, a[{i + 1}] = {a[i + 1]}, b[{i}] = {b[i]}")
            a[i] = b[i]

    # Final check
    return a == b

input = get(input())

#00001
#00010

print(transform_with_forward_backward([1, 2, 3, 4, 5], [3, 2, 7, 1, 5]))  # True
print(transform_with_forward_backward([0, 0, 1], [1, 0, 1]))  # False
print(transform_with_forward_backward([0, 0, 1], [0, 0, 0]))  # False
print(transform_with_forward_backward([0, 0, 1, 2], [1, 3, 3, 2]))  # False
print(transform_with_forward_backward([1, 1, 4, 5, 1, 4], [0, 5, 4, 5, 5, 4]))  # True
print(transform_with_forward_backward([0, 1, 2], [2, 3, 2]))  # False
print(transform_with_forward_backward([10, 10], [11, 10]))  # False
