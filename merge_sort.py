def merge(A, B):
    C = []
    Ai = 0
    Bi = 0

    while Ai < len(A) and Bi < len(B):    
        if A[Ai] <= B[Bi]:
            C.append(A[Ai])
            Ai += 1
        else:
            C.append(B[Bi])
            Bi += 1

    while Ai < len(A):
        C.append(A[Ai])
        Ai += 1

    while Bi < len(B):
        C.append(B[Bi])
        Bi += 1

    # Returns both input vectors merged and sorted
    return C

def merge_sort(A):
    B = A[:int(len(A)/2)]
    C = A[int(len(A)/2):]

    if len(A) > 2:
        B = merge_sort(B)
        C = merge_sort(C)

    # Returns sorted vector
    return merge(B, C)
