def quick_sort(q, ll, r):
    if ll >= r:
        return q
    x = q[ll]
    i = ll - 1
    j = r + 1
    while i < j:
        while True:  # do i++; while (q[i] < x);
            i += 1
            if q[i] >= x:  # if not q[i] < x:
                break
        while True:
            j -= 1
            if q[j] <= x:
                break
        if i < j:
            q[i], q[j] = q[j], q[i]
    quick_sort(q, ll, j)
    quick_sort(q, j + 1, r)


if __name__ == "__main__":
    n = int(input("n: "))
    lst = [int(num) for num in input("numbers: ").split()]
    quick_sort(lst, 0, n - 1)
    [print(i, end=" ") for i in lst]
