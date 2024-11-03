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

import random
from collections import deque
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
        if x not in self.parent:
            raise KeyError(f"Substation {x} not initialized in UnionFind.")
        if self.parent[x] != x:
            self.parent[x] = self.findset(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.findset(x)
        root_y = self.findset(y)
        if root_x == root_y:
            return False  # Ingen union utført

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        return True  # Union utført

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


def multi_source_bfs(subnet_nodes, substations, m, n, uf, cache):
 
    heap = [(0, node) for node in subnet_nodes]  # (distance, node)
    heapq.heapify(heap)
    visited = set(subnet_nodes)
    
    source_set = uf.findset(subnet_nodes[0])
    
    while heap:
        dist, current_node = heapq.heappop(heap)
        
        if current_node in cache:
            cached_substation, cached_dist = cache[current_node]
            if cached_substation != -1:
                total_dist = dist + cached_dist
                if cached_substation not in substations:
                    continue
                neighbor_set = uf.findset(cached_substation)
                if neighbor_set != source_set:
                    return cached_substation, total_dist
            continue
        
        neighbors = get_neighbors(current_node, m, n)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor in substations:
                    try:
                        neighbor_set = uf.findset(neighbor)
                        if neighbor_set != source_set:
                            cache[current_node] = (neighbor, dist + 1)
                            return neighbor, dist + 1
                    except KeyError:
                        # Neighbor is a substation but not initialized; skip
                        continue
                else:
                    heapq.heappush(heap, (dist + 1, neighbor))
        
        cache[current_node] = (-1, -1)
    
    return -1, -1

def power_grid(m, n, substations):
    if not substations:
        return 0

    uf = UnionFind()
    substations_set = set(substations)

    # Initialiser Union-Find med alle substasjonene
    for s in substations:
        uf.makeset(s)

    kanter = []
    total_distance = 0
    substations_not_connected = list(substations)

    # Global cache for multi_source_bfs
    multi_source_bfs_cache = {}

    # Koble alle substasjoner til deres nærmeste nabo med BFS
    # while substations_not_connected:
    #     substation_not_connected = substations_not_connected[0]
    #     try:
    #         nearest_node, dist = multi_source_bfs([substation_not_connected], substations_set, m, n, uf, multi_source_bfs_cache)
    #     except KeyError as e:
    #         print(f"Feil: {e}")
    #         return 0

    #     if nearest_node != -1 and dist != -1:
    #         if uf.findset(substation_not_connected) != uf.findset(nearest_node):
    #             if uf.union(substation_not_connected, nearest_node):
    #                 kanter.append((dist, substation_not_connected, nearest_node))
    #                 total_distance += dist
    #                 substations_not_connected.remove(substation_not_connected)
    #                 if nearest_node in substations_not_connected:
    #                     substations_not_connected.remove(nearest_node)
    #     else:
    #         substations_not_connected.remove(substation_not_connected)

    # Finne nærmeste ved stegvis BFS fra alle noder 
    while len(set(uf.findset(sub) for sub in substations)) > 1:
        # Grupper substasjoner etter deres respektive sett
        subnets = {}
        for sub in substations:
            set_id = uf.findset(sub)
            if set_id not in subnets:
                subnets[set_id] = []
            subnets[set_id].append(sub)

        # Iterer over hvert subnet for å finne den nærmeste noden i et annet subnet
        for subnet_id, subnet_nodes in subnets.items():
            nearest_node, dist = multi_source_bfs(subnet_nodes, substations_set, m, n, uf, multi_source_bfs_cache)


            

            if nearest_node != -1 and dist != -1:
                # Finn den første noden i subnettet for å koble med den nærmeste noden
                first_node = subnet_nodes[0]
                if uf.union(first_node, nearest_node):
                    kanter.append((dist, first_node, nearest_node))
                    total_distance += dist
                    print(f"Connected subnet: {first_node} to {nearest_node} with distance {dist}")
                    connected = True
                    break

        if not connected:
            # Ingen videre tilkoblinger kan gjøres, unngå uendelig løkke
            print("No further connections can be made. Exiting loop to prevent infinite iteration.")
            break

    

    # Sjekk om alle substasjoner er koblet
    root = uf.findset(substations[0])
    for substation in substations:
        if uf.findset(substation) != root:
            return 0  # Ikke alle er koblet sammen

    return total_distance

print(power_grid(2, 2, [(0, 0), (1, 1)]))
print(power_grid(2, 2, [(0, 0), (0, 1), (1, 0)]))
print(power_grid(2, 2, [(0, 0), (0, 1), (1, 0), (1, 1)]))
print(f"Skulle vært 2 fikk: {power_grid(2, 3, [(0, 1), (1, 0), (1, 1)])}")

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
