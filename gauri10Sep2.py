def getNumPairs(arr, queries):
    n = len(arr)
    maxima = arr[0]
    minima = arr[n - 1]
    pref_max = []
    suf_min = []
    for i in range(n):
        if arr[i] > maxima:
            maxima = arr[i]
        pref_max.append(maxima)
    for i in range(n - 1, -1, -1):
        if arr[i] < minima:
            minima = arr[i]
        suf_min.append(minima)

    answer = []
    for q in queries:
        counter = 0
        for i in pref_max:
            for j in suf_min:
                if i * j == q:
                    counter += 1
        answer.append(counter)

    return answer


print(getNumPairs([1, 2, 4, 4], [1, 2, 3, 4]))
