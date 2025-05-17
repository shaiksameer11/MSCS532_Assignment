def insertion_sort_decreasing(arr):
    # Make a copy of the original array
    A = arr.copy()
    
    # Start from the second element (index 1)
    for j in range(1, len(A)):
        key = A[j]
        
        # Insert A[j] into the sorted sequence A[0..j-1]
        i = j - 1
        # Change comparison to > instead of < for decreasing order
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
            
    return A