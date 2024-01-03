def merge_sort(q, ll, r):
    if ll >= r:
        return
    mid = ll + r >> 1  # (ll + r) >> 1
    merge_sort(q, ll, mid)
    merge_sort(q, mid + 1, r)
    k = 0
    i = ll
    j = mid + 1
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp[k] = q[i]  # tmp[k++] = q[i++]
            k += 1
            i += 1
        else:
            tmp[k] = q[j]  # tmp[k++] = q[j++]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = q[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = q[j]
        k += 1
        j += 1
    for i, j in zip(range(ll, r + 1), range(n)):
        q[i] = tmp[j]


if __name__ == "__main__":
    n = int(input("n:"))
    tmp = [0] * n
    lst = [int(num) for num in input("numbers:").split()]  # type(num) == string
    merge_sort(lst, 0, n - 1)
    [print(i, end=" ") for i in lst]
