from itertools import permutations
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall agenter i generert instans.
n_lower = 3
# Høyest mulig antall agenter i generert instans.
# NB: Om dette antallet settes høyt vil det ta veldig lang tid å kjøre
# testene, da mulige svar sjekkes ved bruteforce.
n_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def find_cycle(n, values):
    visited = [False] * n  # lag liste over besøkte agenter
    path = [] # lag vei i liste
    
    # Dybde først søk
    def dfs(v, parent):
        nonlocal cycle  # Gjør 'cycle' tilgjengelig i hele find_cycle
        visited[v] = True # Marker agent som besøkt
        path.append(v) # Legg til node i graf

        for neighbor in range(n): # Iterer naboer
            if values[v][neighbor]: # Hvis du er sjalu på nabo
                if not visited[neighbor]: # Hvis du ikke har besøkt nabo
                    if dfs(neighbor, v): # Hvis DFS av Nabo med deg som parent finner en sykel
                        return True
                elif neighbor in path: # Hvis nabo er besøkt så har vi funnet en sykel!
                    cycle_start_index = path.index(neighbor) # Sykel startindex
                    cycle = path[cycle_start_index:] # Sykel er gjeldene path fra start index
                    return True

        path.pop() # Resett path til neste DFS søk
        return False # Fant ingen sykel, returner False

    cycle = None  # Initialiser 'cycle' før DFS
    for node in range(n): # Iterer noder
        if not visited[node]: # Hvis node ikke har blitt besøkt
            if dfs(node, -1): # Hvis noden har en sykel
                return cycle  # Returner første syklus funnet
    return None

def detect_envy_cycle(n, values):
    # Bygg nabomatrise basert på sjalusi-verdier
    nabomatrise = [[0] * n for _ in range(n)]
    # Dersom i er sjalu på j, sett nabomatrisen for [i][j] = 1
    for i in range(n):
        for j in range(n):
            if i != j and values[i][j] > values[i][i]:
                nabomatrise[i][j] = 1
    # Finn en syklus i nabomatrisa og returner den
    return find_cycle(n, nabomatrise)


# Hardkodede tester på formatet (n, values)
tests = [
    (1, [[1]]),
    (2, [[1, 0], [0, 1]]),
    (2, [[0, 1], [1, 0]]),
    (3, [[1, 2, 2], [0, 1, 2], [0, 2, 1]]),
    (5, [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]),
    (5, [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]),
    (5, [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
    ]),
    (5, [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
    ]),
    (5, [
        [3, 5, 2, 1, 2],
        [1, 4, 5, 3, 3],
        [5, 5, 6, 8, 1],
        [0, 1, 1, 2, 3],
        [8, 3, 5, 6, 7],
    ]),
    (6, [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ]),
    (6, [
        [3, 1, 2, 2, 1, 4],
        [6, 7, 9, 5, 1, 6],
        [3, 3, 4, 7, 2, 1],
        [1, 5, 1, 2, 0, 1],
        [3, 3, 6, 2, 4, 3],
        [1, 6, 6, 7, 9, 8],
    ]),
]

def gen_examples(n_l, n_u, k):
    # Tester med liten sannsynlighet for misunnelsessykler
    for _ in range(k//2):
        n = random.randint(n_l, n_u)
        values = [[int(random.randint(0, 9) == 9) for _ in range(n)] for _ in range(n)]
        yield n, values

    # Tester med stor sannsynlighet for misunnelsessykler
    for _ in range(k - k//2):
        n = random.randint(n_l, n_u)
        values = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
        yield n, values


def gen_answers(n, values):
    # Sjekker om instans har en misunnelsessykel ved hjelp av bruteforce
    # NB: Veldig tregt for store instanser.
    cycle_exists = False
    agents = list(range(n))
    for k in range(1, n + 1):
        for x in permutations(agents, k):
            if valid_cycle(values, x):
                yield list(x)
                cycle_exists = True
    if not cycle_exists:
        yield None

def valid_cycle(values, answer):
    # Sjekker om answer er en gyldig misunnelsessykel
    return all(values[x][y] > values[x][x] for x, y in zip(answer, answer[1:] +
                                                           answer[:1]))

if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(n_lower, n_upper, random_tests))

failed = False
for n, values in tests:
    possible_answers = list(gen_answers(n, values))
    answer = detect_envy_cycle(n, [row[:] for row in values])

    if answer not in possible_answers:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
Agenter: {n}
Verdier:
{chr(10).join(', '.join(map(str, row)) for row in values)}

Ditt svar var {answer}, mens mulige svar er:""")
        print(*possible_answers, sep="\n", end="\n\n")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
