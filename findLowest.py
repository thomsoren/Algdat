def solution(A):
    # Implement your solution here
    setA = set(A)
    for i in range(1, len(A)+1):
        if i not in setA:
            return i

print(solution([1, 3, 6, 4, 1, 2])) # Expected output: 5    
print(solution([1, 2, 3])) # Expected output: 4
print(solution([-1, -3])) # Expected output: 1