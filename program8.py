def reorder(A):
    # 'k' stores the index of the next available position
    k = 0
    # do for each element
    for i in A:
        # if the current element is non-zero, put the element at t
        # next free position in the list
        if i:
            A[k] = i
            k = k + 1
    # move all 0's to the end of the list (remaining indices)
    for i in range(k, len(A)):
        A[i] = 0
A = [5, 4, 6, 0, 1, 0, 2, 7, 0, 3, 9, 0]
reorder(A)
print(A)