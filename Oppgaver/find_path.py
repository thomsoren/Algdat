#!/usr/bin/python3
# coding=utf-8
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall tall i hver kolonne og rad i generert instans.
numbers_lower = 3
# Høyest mulig antall tall i hver kolonne og rad i generert instans.
# NB: Om denne verdien settes høyt (>15) vil det ta veldig lang tid å
# generere testene.
numbers_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def find_path(weights):
    rows = len(weights)
    if rows == 0:
        return []
    cols = len(weights[0])
    if cols == 0:
        return []
    
    # Initialize DP table
    dp = [[0] * cols for _ in range(rows)]
    path = [[-1] * cols for _ in range(rows)]  # To track the path

    # Initialize the first row of DP table
    for j in range(cols):
        dp[0][j] = weights[0][j]
    
    # Populate the DP table
    for i in range(1, rows):
        for j in range(cols):
            min_prev = dp[i-1][j]
            path[i][j] = j
            if j > 0 and dp[i-1][j-1] < min_prev:
                min_prev = dp[i-1][j-1]
                path[i][j] = j-1
            if j < cols -1 and dp[i-1][j+1] < min_prev:
                min_prev = dp[i-1][j+1]
                path[i][j] = j+1
            dp[i][j] = weights[i][j] + min_prev
    
    # Find the minimum weight in the last row
    min_weight = min(dp[-1])
    min_index = dp[-1].index(min_weight)
    
    # Reconstruct the path
    shortest = []
    j = min_index
    for i in range(rows-1, -1, -1):
        shortest.append((j, i))
        j = path[i][j]
    
    shortest.reverse()
    return shortest

# def find_path(weights):
#     # Finn en sti av piksler fra topp til bunn der summen av vektene er lavest mulig.
#     rows = len(weights)
#     if rows == 0:
#         return []
#     cols = len(weights[0])
#     if cols == 0:
#         return []
    
#     if cols == 1 and rows == 1:
#         return [(0,0)]

#     if cols == 2 and rows == 1:
#         return [(0,0)] 


#     path = []

#     # Lage grid som regner ut kostnad av vektende vertikalt

#     for i in range(rows):
#         row = []
        
#         if i == 0 and cols == 1:
#             row.append(weights[i][0])
#             if rows == 1:
#                 break
        

#         for j in range(cols):
#             if i == 0:
#                 row.append(weights[i][j])
#             elif (j == 0):
#                 row.append(weights[i][j] + max(weights[i-1][j], weights[i-1][j+1]))
#             elif (j == cols-1):
#                 row.append(weights[i][j] + max(weights[i-1][j], weights[i-1][j-1])) 
#             else:
#                 row.append(weights[i][j] + max(weights[i-1][j], weights[i-1][j-1]), weights[i-1][j+1])  
#         path.append(row)

#     # Finne korteste rute
#     shortest = []
#     previous_j = 0
#     for i in range(rows, 0):
#         lowest = float('inf')
#         x = 0
#         for j in range(cols):
#             current = path[i][j]
#             # finne billigste for laveste rad
#             if i == rows and current < lowest:
#                 lowest = current
#                 x = j
#                 previous_j = j

#             elif (previous_j == 0 and j == previous_j):
#                 min =  min(path[i][j], path[i][j+1])
#                 x = path[i].index(min)
#             elif (previous_j == cols and j == previous_j):
#                 min =  min(path[i][j], path[i][j-1])
#                 x = path[i].index(min)
#             elif(j == previous_j):
#                 min =  min(path[i][j], path[i][j-1], path[i][j+1])
#                 x = path[i].index(min)

#             shortest.append((x,i))
#     shortest.reverse() 
#     return shortest

# Hardkodete tester
tests = [
    [[1]],
    [[1, 1]],
    [[1], [1]],
    [[2, 1], [2, 1]],
    [[1, 1], [1, 1]],
    [[2, 1], [1, 2]],
    [[3, 2, 1], [1, 3, 2], [2, 1, 3]],
    [[1, 9, 3, 3], [1, 9, 3, 3], [9, 9, 3, 3]],
    [[1, 2, 7, 4], [9, 3, 2, 5], [5, 7, 8, 3], [1, 3, 4, 6]],
]

# Treg bruteforce løsning for å finne vekten til den optimale stien
def bruteforce(w, i=None, j=0):
    if i is None:
        return min(bruteforce(w, i)
                   for i in range(len(w[0])))

    if j == len(w):
        return 0

    best = float("inf")
    if i > 0:
        best = min(best, bruteforce(w, i - 1, j + 1))
    best = min(best, bruteforce(w, i, j + 1))
    if i < len(w[0]) - 1:
        best = min(best, bruteforce(w, i + 1, j + 1))

    return w[j][i] + best


# Verifiserer at en løsning er riktig gitt vektene, stien og den minst
# mulige vekten man kan ha på en sti.
def verify(weights, path, optimal):
    if path is None:
        return False, "Svaret er ikke en sti"

    if len(path) != len(weights):
        return False, "Stien er enten for lang eller for kort."

    last = -1
    for index, element in enumerate(path):
        if type(element) != tuple:
            return False, "Stien består ikke av tupler."
        if len(element) != 2:
            return False, "Stien består ikke av tupler på formatet (x,y)."
        if index != element[1]:
            return False, "Stien er ikke vertikal."
        if element[0] < 0 or element[0] >= len(weights[0]):
            return False, "Stien går utenfor bildet."
        if last != -1 and not last - 1 <= element[0] <= last + 1:
            return False, "Stien hopper mer enn en piksel per rad."
        last = element[0]

    weight = sum(weights[y][x] for x, y in path)
    if weight != optimal:
        return (
            False,
            "Stien er ikke optimal. En optimal sti ville hatt"
            + "vekten {:}, mens din hadde vekten {:}".format(optimal, weight),
        )

    return True, ""


def gen_examples(k, lower, upper):
    for _ in range(k):
        w, h = random.randint(lower, upper), random.randint(lower, upper)
        yield [[random.randint(0, 9) for _ in range(w)] for _ in range(h)]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))


failed = False

for test in tests:
    student = find_path([row[:] for row in test])
    optimal_weight = bruteforce(test)
    correct, error_message = verify(test, student, optimal_weight)
    if not correct:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
weights:
{chr(10).join(["  ".join(map(str, row)) for row in test])}

Ditt svar: {student}
Feilmelding: {error_message}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
