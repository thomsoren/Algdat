def rod_cutting(n, p):
    # R[i]: Maksimal inntekt for stavlengde i
    R = [0] * (n + 1)
    # S[i]: Første kutt for å oppnå maksimal inntekt for lengde i
    S = [0] * (n + 1)
    
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + R[j - i]:
                q = p[i] + R[j - i]
                S[j] = i
        R[j] = q
    return R, S

def print_cut_solution(n, p):
    R, S = rod_cutting(n, p)
    print("Maksimal inntekt:", R[n])
    print("Kuttlengder:", end=" ")
    while n > 0:
        print(S[n], end=" ")
        n -= S[n]

# Eksempelbruk:
n = 7
p = [0,1, 4, 3, 6, 8, 5, 9]  # Indeksering starter fra 1 for enkelhets skyld
print_cut_solution(n, p)