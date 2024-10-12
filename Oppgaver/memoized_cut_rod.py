def memoized_cut_rod(p, n):
    r = [-float('inf')] * (n + 1)  # Adjusted size of r
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1):  # Include n in the range
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q