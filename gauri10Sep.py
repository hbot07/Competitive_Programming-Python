def getNumPairs(arr, queries):
    maxima = arr[0]
    minima = arr[0]
    pref_max = []
    suf_min = []
    for i in range(len(arr)):
        if arr[i] > maxima:
            maxima = arr[i]
        pref_max.append(maxima)

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < minima:
            minima = arr[i]
        suf_min.append(minima)
    suf_min.reverse()

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
