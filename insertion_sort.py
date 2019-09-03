def insertion_sort(A):
    for i in range(1, len(A)):
        current = A[i]
        j = i
        while(current < A[j - 1] and j > 0):
            A[j] = A[j - 1]
            j -= 1

        A[j] = current

    return A
