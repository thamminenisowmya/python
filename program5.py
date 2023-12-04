def get_sum_second_largest(even_matrix, odd_matrix):
    if len(even_matrix) >= 2:
        even_second_largest = even_matrix[-2]
    else:
        even_second_largest = float('-inf')
    if len(odd_matrix) >= 2:
        odd_second_largest = odd_matrix[-2]
    else:
        odd_second_largest = float('-inf')
    return even_second_largest + odd_second_largest
size = int(input("enter the size of array: "))
matrix = []
for i in range(size):
    element = int(input(f"Enter element at{i} index: "))
    matrix.append(element)
even_matrix = matrix[::2]  # Element at even indices
odd_matrix = matrix[1::2]  # Element at odd indices
even_matrix.sort()
odd_matrix.sort()  
print(f"sorted even array: {even_matrix}")
print(f"sorted odd every: {odd_matrix}")
   # calculate and print the sum of second-largest numbers
sum_second_largest = get_sum_second_largest(even_matrix,odd_matrix) 
print(f"sum of second-largest numbers: {sum_second_largest}")