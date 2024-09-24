def insertion_sort(A):
    # Skriv koden din her
    for i in range (1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A 
        
ans = insertion_sort([2,7,4,5,1])
print(ans)
