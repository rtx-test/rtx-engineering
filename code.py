def merge_arrays(a, b, n):
    i = 0
    j = 0
    c = []

    while i < n and j < n:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < n:
        c.append(a[i])
        i += 1

    while j < n:
        c.append(b[j])
        j += 1

    return c


# Input handling
n = int(input())
a = [int(input()) for _ in range(n)]

n = int(input())
b = [int(input()) for _ in range(n)]

result = merge_arrays(a, b, n)

for num in result:
    print(num)