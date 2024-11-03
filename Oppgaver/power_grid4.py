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

import heapq

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeset(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def findset(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findset(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        root_x = self.findset(x)
        root_y = self.findset(y)
        if root_x == root_y:
            return False  
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        return True  

def get_neighbors(node, m, n):
    x, y = node
    neighbors = []
    if x > 0:  # Up
        neighbors.append((x - 1, y))
    if y < n - 1:  # Right
        neighbors.append((x, y + 1))
    if x < m - 1:  # Down
        neighbors.append((x + 1, y))
    if y > 0:  # Left
        neighbors.append((x, y - 1))
    return neighbors

def power_grid(m, n, substations):
    if not substations:
        return 0

    uf = UnionFind()
    for s in substations:
        uf.makeset(s)

    # Priority queue: (distance, originating_substation, current_node)
    heap = []
    visited = {}  # Maps node to (originating_substation, distance)

    # Initialize heap with all substations
    for sub in substations:
        heapq.heappush(heap, (0, sub, sub))
        visited[sub] = (sub, 0)  # Mark substation as visited by itself with 0 distance

    total_distance = 0
    connected_components = len(substations)

    while heap:
        dist, origin, current = heapq.heappop(heap)

        # If the current node has already been visited by a closer substation, skip it
        if current in visited and visited[current][1] < dist:
            continue

        # Explore neighbors and propagate search
        for neighbor in get_neighbors(current, m, n):
            if neighbor not in visited:
                # Visit the neighbor for the first time
                visited[neighbor] = (origin, dist + 1)
                heapq.heappush(heap, (dist + 1, origin, neighbor))
            else:
                # Check if neighbor has been visited by a different substation
                other_origin, other_dist = visited[neighbor]
                if other_origin != origin:
                    # Attempt to union the two substations' sets
                    if uf.union(origin, other_origin):
                        total_distance += dist + 1 + other_dist
                        connected_components -= 1
                        if connected_components == 1:
                            return total_distance

    # Verify all substations are connected
    root = uf.findset(substations[0])
    for substation in substations:
        if uf.findset(substation) != root:
            return 0  # Not all substations are connected

    return total_distance

print(f"Skulle vært 2 fikk: {power_grid(2, 3, [(0, 1), (1, 0), (1, 1)])}")
print(f"Skulle vært 4 fikk: {power_grid(3, 3, [(0, 2), (2, 0)])}")


# Hardkodete instanser på format: (m, n, substations)
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
