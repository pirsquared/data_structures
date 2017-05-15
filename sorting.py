def qsrt_last(a, i, j):
    if j - i > 0:
        p = a[j]
        b = i
        for k in range(i, j):
            if a[k] < a[j]:
                a[k], a[b], b = a[b], a[k], b + 1
        a[b], a[j] = a[j], a[b]
        print(' '.join(map(str, a)))
        qsrt_last(a, i, b - 1)
        qsrt_last(a, b + 1, j)
