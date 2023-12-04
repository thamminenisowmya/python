# Function to sort a bimary list in linear time
def sort(A):
    # count number of 0's
    zeros = A.count(0)
    # put 0's at the beginning
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k+1
    # fill all remaining elements by 1
    for k in range(k, len(A)):
        A[k] = 1
A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 8, 5, 2]
sort(A)
print(A)
