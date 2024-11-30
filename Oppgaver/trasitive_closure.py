        def transitive_closure(T, n, general_floyd_warshall):
    # Velg funksjoner til Floyd-Warshall
    def f(x, y):
        # Hva skal f returnere?

    def g(x, y):
        # Hva skal g returnere?
        return 

    def general_floyd_warshall(D, n, f, g):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                        D[i][j] = f(D[i][j], g(D[i][k], D[k][j]))


    general_floyd_warshall(T, n, f, g)
