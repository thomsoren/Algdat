# !/usr/bin/python3
# coding=utf-8
from itertools import combinations
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
# Laveste mulige antall trafokiosker i generert instans.
substations_lower = 3
# Høyest mulig antall trafokiosker generert instans.
# NB: Om dette antallet settes høyt (>8) vil det ta veldig lang tid å kjøre
# testene, da svaret på instansene finnes ved bruteforce.
substations_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

class Graph:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False  
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True


def power_grid(m, n, substations):
    if not substations or len(substations) == 1:
        return 0
    
    # Assign unique IDs to substations
    id_map = {point: idx for idx, point in enumerate(substations)}
    num_points = len(substations)
    
    points = substations  # Alias for clarity
    
    # Define all sorting keys, including sorted by x and y
    sorting_keys = [
        lambda p: (p[0] + p[1], p[0], p[1]),
        lambda p: (p[0] - p[1], p[0], p[1]),
        lambda p: (-p[0] + p[1], p[0], p[1]),
        lambda p: (-p[0] - p[1], p[0], p[1]),
        lambda p: (p[0], p[1]),  # Sorted by x then y
        lambda p: (p[1], p[0])   # Sorted by y then x
    ]
    
    # Generate all potential edges using list comprehensions
    edges = set()
    
    for key in sorting_keys:
        sorted_points = sorted(points, key=key)
        # Iterate using indices to pair adjacent points
        for i in range(len(sorted_points) - 1):
            p1 = sorted_points[i]
            p2 = sorted_points[i + 1]
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # Manhattan distance
            id1 = id_map[p1]
            id2 = id_map[p2]
            # Ensure the smaller ID comes first to avoid duplicate edges
            if id1 > id2:
                id1, id2 = id2, id1
            edges.add((dist, id1, id2))
    
    # Convert the set to a sorted list of edges based on distance
    sorted_edges = sorted(edges)
    
    # Initialize Union-Find structure
    uf = Graph(num_points)
    total_length = 0
    edges_used = 0
    required_edges = num_points - 1
    
    # Krusky's algorithm to find the Minimum Spanning Tree (MST)
    for dist, id1, id2 in sorted_edges:
        if uf.union(id1, id2):
            total_length += dist
            edges_used += 1
            if edges_used == required_edges:
                break  # MST is complete
    
    return total_length


print(power_grid(m=3, n=4, substations=[(0, 1), (2, 1), (0, 0), (1, 1), (2, 3), (0, 2), (2, 2), (1, 0), (1, 3)])) # should of given 8

import random
m, n = 1000000, 1000000
num_substations = 100000  # Adjust as needed
substations = set()
while len(substations) < num_substations:
    x = random.randint(0, m)
    y = random.randint(0, n)
    substations.add((x, y))
substations = list(substations)
print(power_grid(m, n, substations))

#Hardkodete instanser på format: (m, n, substations)
tests = [
    (2, 2, [(1, 1)]),
    (2, 2, [(0, 0), (1, 1)]),
    (2, 2, [(0, 0), (0, 1), (1, 0)]),
    (2, 2, [(0, 0), (0, 1), (1, 0), (1, 1)]),
    (3, 3, [(0, 2), (2, 0)]),
    (3, 3, [(0, 0), (1, 1), (2, 2)]),
    (3, 3, [(1, 1), (0, 1), (2, 1)]),
    (3, 3, [(1, 2)]),
    (3, 3, [(2, 0), (1, 1), (0, 1)]),
    (2, 3, [(1, 1)]),
    (2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
    (2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
    (3, 3, [(0, 1), (0, 2), (2, 1), (2, 2)]),
    (3, 3, [(0, 1), (0, 2), (1, 2), (2, 1)]),
    (2, 3, [(1, 0), (1, 1), (0, 2)]),
    (2, 3, [(1, 0)]),
    (3, 2, [(1, 0), (2, 1), (0, 0)]),
    (3, 3, [(0, 1), (1, 1), (2, 1), (0, 0)]),
    (3, 3, [(0, 2)]),
]


def gen_examples(substations_lower, substations_upper, k):
    for _ in range(k):
        n, m = random.randint(3, 50), random.randint(3, 50)
        s = random.randint(substations_lower, min(substations_upper, n * m))
        substations = set()
        while len(substations) < s:
            substations.add((
                random.randint(0, m - 1),
                random.randint(0, n - 1)
            ))
        substations = list(substations)

        yield (m, n, substations)

def get_answer(m, n, substations):
    # Finner løsningen på problemet ved bruteforce.
    # NB: Bruker minst noen minutter hvis det er 10+ substations
    s = len(substations)
    if s <= 1:
        return 0

    E = [(i, j) for i in range(0, s - 1) for j in range(i + 1, s)]
    def visit(S, v, ST):
        if v in S:
            return
        S.add(v)
        for (a, b) in ST:
            if a == v:
                visit(S, b, ST)
            if b == v:
                visit(S, a, ST)

    solution = float("inf")
    for ST in combinations(E, s - 1):
        S = set()
        visit(S, 0, ST)
        if len(S) != s:
            continue

        answer = 0
        for (a, b) in ST:
            answer += max(substations[a][0], substations[b][0])
            answer -= min(substations[a][0], substations[b][0])
            answer += max(substations[a][1], substations[b][1])
            answer -= min(substations[a][1], substations[b][1])
        if answer < solution:
            solution = answer

    return solution

if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        substations_lower,
        substations_upper,
        random_tests
    ))

failed = False
for m, n, substations in tests:
    answer = get_answer(m, n, substations)
    student = power_grid(m, n, substations)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
m: {m}
n: {n}
substations: {', '.join(map(str, substations))}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
