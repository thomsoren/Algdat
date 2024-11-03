# !/usr/bin/python3
# coding=utf-8
import random
import itertools
import math

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
# Lavest mulig antall reaksjoner i generert instans.
reactions_lower = 10
# Høyest mulig antall reaksjoner i generert instans. Om denne verdien er satt høyt
# (>25), kan det ta lang tid å generere instansene.
reactions_upper = 15
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0



from collections import defaultdict, deque

class Node:
    def __init__(self,id):
        self.id = id
        self.d = float('inf')
        self.pi = None
        self.neighbors = []
        self.finished = False

    def __lt__(self, other):
        return self.d < other.d

def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u
        return True
    return False

def init_single_source(nodes, s):
    for node in nodes.values():
        node.d = float('inf')
        node.pi = None 
    s.d = 0

def get_nodes_from_edges(edges):
    nodes = {}
    for u, v, w in edges:
        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)
        nodes[u].neighbors.append((nodes[v],w))
    return nodes


def min_heapify(A, i):
    l = i*2+1
    r = i*2+2
    if l < len(A) and A[l].d < A[i].d:
        m = l
    else:
        m = i
    if r < len(A) and A[r].d < A[m].d:
        m = r
    if m != i:
        holder = A[i]
        A[i] = A[m]
        A[m] = holder
        min_heapify(A, m)

def decrease_key(A, x, key):
    x.d = key
    i = A.index(x)
    while i > 0 and A[par(i)].d > A[i].d:
        holder = A[i]
        A[i] = A[par(i)]
        A[par(i)] = holder
        i = par(i) 

def heap_minimum(A):
    if len(A) < 1:
        return
    return A[0]
    
def extract_min(Q):
    min = heap_minimum(Q)
    Q_size = len(Q)
    Q[0] = Q[Q_size-1]
    Q.pop() 
    Q_size = Q_size-2
    min_heapify(Q,0)
    return min


def par(i):
    return (i-1)//2

def dijkstra(edges, start, goal):
    nodes = get_nodes_from_edges(edges)
    init_single_source(nodes, nodes[start])

    Q = list(nodes.values())
    min_heapify(Q,0)

    while len(Q) != 0:
        print([i.d for i in Q])
        u = extract_min(Q)
        print(u.id)
        u.finished = True
        for v,w in u.neighbors:
            if not v.finished and relax(u,v,w): 
                decrease_key(Q,v,v.d)
    return nodes

def least_energy(reactions, start, goal, laws_of_thermodynamics=False):
    nodes = dijkstra(reactions, start, goal)
    path = []
    current = nodes[goal]
    print(current) 
    while current:
        if (current not in path):
            path.insert(0, current.id)
            current = current.pi
        else:
            break
    return path

# def least_energy(reactions, start, goal, laws_of_thermodynamics=False):
#     print(f"reactions {reactions}")
#     nodes, edges = bellman_ford(reactions, start, goal)
     
#     if (edges != reactions):
#         prev_edges = None
#         while edges != prev_edges:
#             prev_edges = edges
#             nodes, edges = bellman_ford(edges, start, goal)

#     path = []
#     current = goal

#     if nodes[goal].d == float('inf'):
#         return "No path found"
    
#     while current:
#         if (current not in path):
#             path.insert(0, current)
#             current = nodes[current].pi
#         else:
#             break
#     return path

def bellman_ford(edges, start, goal):
    nodes = get_nodes_from_edges(edges)
    init_single_source(nodes, nodes[start])
    for _ in range(len(nodes)-1):
        for u, v, w in edges: 
            relax(u,v,w, nodes)

    # Detekter negativ sykel
    negative_cycle_start = None
    for u, v, w in edges:
        if nodes[v].d > nodes[u].d + w:
            print(f"Negativ sykel funnet med kan {u}-> {v} med vekt {w}")
            negative_cycle_start = v

    if negative_cycle_start is not None:
        # 1: Identifiser node i sykel
        cycle_node = negative_cycle_start
        cycle_nodes = set()
        for _  in range(len(nodes)):
            cycle_node = nodes[cycle_node].pi

        # 2: Finn den negative sykel
        cycle = []
        current_node = cycle_node
        while current_node not in cycle:
            cycle.append(current_node)
            current_node = nodes[current_node].pi
        cycle.append(current_node)                    
        cycle.reverse()
        print(f"Negative cycle nodes: {cycle}")

        # 3: Hent kanter i sykel
        cycle_edges = []
        for i in range(len(cycle)-1):
            u = cycle[i]
            v = cycle[i+1]
            # Finn kant mellom u og v
            for edge in edges:
                if edge[0] == u and edge[1] == v:
                    cycle_edges.append(edge)
                    break
        
        print(f"Edges in negative cycle: {cycle_edges}")

        # 4: Finn sykel som peker til allerede besøkt noder
        reachable_from_start = set()

        def bfs(start_node, excluded_edges):
            visited = set()
            queue = deque([start_node])
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for u, v, _ in edges:
                    if (u == node) and ((u, v, _) not in excluded_edges):
                        queue.append(v)
            return visited
        
        visited_from_start = bfs(start, set(cycle_edges))
        print(f"Nodes reachable from {start} excluding the negative cycle: {visited_from_start}")
        
        edge_to_remove = None
        for edge in cycle_edges:
            u, v, _ = edge
            if v in visited_from_start:
                edge_to_remove = edge
                print(f"Selected edge {edge_to_remove} for removal")

        if edge_to_remove:
            new_edges = [edge for edge in edges if edge != edge_to_remove]
            return nodes, new_edges
        else:
            # Hvis ingen kant som det finnes, fjern en tilfeldig
            edge_to_remove = cycle_edges[0]
            new_edges = [edge for edge in edges if edge != edge_to_remove]
            print("No edge found to remove to reach target without negative cycles") 
            return nodes, new_edges
    else:
        print(f"No negative cycle detected. Proceeding: {edges}")
        return nodes, edges

def topological_sort(edges, nodes):
    from collections import defaultdict

    adj = defaultdict(list)
    for u, v, _ in edges:
        adj[u].append(v)
    
    visited = {}
    stack = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        if has_cycle:
            return
        visited[u] = 'visiting'
        for v in adj[u]:
            if v not in visited:
                dfs(v)
            elif visited[v] == 'visiting':
                has_cycle = True
                return
        visited[u] = 'visited'
        stack.append(u)

    for node in nodes:
        if node not in visited:
            dfs(node)
            if has_cycle:
                break

    if has_cycle:
        return []
    stack.reverse()
    return stack

def dag_shortest_paths(edges, s):
    nodes = get_nodes_from_edges(edges)
    topo_sort = topological_sort(edges, nodes)
    if not topo_sort:
        return "Graph not DAG"

    init_single_source(nodes, nodes[s])

    for u in topo_sort:
        for edge in edges:
            if edge[0] == u:
                relax(edge[0], edge[1], edge[2], nodes)
    return nodes

#print(least_energy([("A", "B", 100), ("B", "C", 100), ("B", "C", 70)], "A", "C"))
#print(least_energy([("A", "B", 100), ("B", "C", 50), ("C", "D", -100), ("D", "B", -50)], "A", "D"))
#print(least_energy([("A", "B", 3), ("A", "C", 1), ("C", "D", 1), ("B", "D", -3), ("D", "E", 1)], "A", "E"))
print(least_energy([('A', 'B', 100), ('B', 'A', -100)], "B", "A"))
print(least_energy([('A', 'B', 100), ('B', 'C', -50), ('A', 'C', 70)], "A", "C"))

# Hardkodete tester på format: (reactions, start, goal), lavest mulig energi
tests = [
    (([("A", "B", 100)], "A", "B"), 100),
    (([("B", "A", -100)], "B", "A"), -100),
    (([("A", "B", 100), ("B", "A", -100)], "A", "B"), 100),
    (([("A", "B", 100), ("B", "A", -100)], "B", "A"), -100),
    (([("A", "B", 100), ("B", "C", -50), ("A", "C", 70)], "A", "C"), 50),
    (([("A", "B", 100), ("B", "C", -20), ("A", "C", 70)], "A", "C"), 70),
    (
        (
            [
                ("A", "C", -100),
                ("B", "C", -100),
                ("A", "C", -201),
                ("B", "A", 100),
            ],
            "A",
            "C",
        ),
        -201,
    ),
    (([("Y", "N", 11), ("N", "Y", -10)], "Y", "N"), 11),
    (
        (
            [
                ("E", "K", 68),
                ("F", "K", 21),
                ("K", "F", -21),
                ("F", "E", 50),
                ("K", "E", 10),
                ("E", "F", -1),
            ],
            "E",
            "F",
        ),
        -1,
    ),
    (
        (
            [("C", "V", 36), ("C", "B", 18), ("B", "C", -17), ("V", "B", 54)],
            "C",
            "B",
        ),
        18,
    ),
    (
        (
            [
                ("P", "G", 47),
                ("G", "T", 52),
                ("T", "P", 20),
                ("P", "T", -19),
                ("G", "P", 30),
            ],
            "T",
            "G",
        ),
        67,
    ),
    (
        (
            [
                ("F", "Y", 69),
                ("U", "F", 47),
                ("Y", "U", -5),
                ("Y", "F", 18),
                ("U", "Y", 6),
            ],
            "U",
            "Y",
        ),
        6,
    ),
    (
        (
            [
                ("K", "G", -27),
                ("A", "G", 52),
                ("G", "A", 18),
                ("K", "A", -17),
                ("A", "K", 17),
            ],
            "K",
            "A",
        ),
        -17,
    ),
    (
        (
            [
                ("X", "H", 2),
                ("X", "U", 48),
                ("H", "X", -1),
                ("U", "H", 41),
                ("H", "U", 36),
                ("U", "X", 49),
            ],
            "X",
            "U",
        ),
        38,
    ),
    (([("V", "L", 11), ("L", "V", -10)], "V", "L"), 11),
    (([("C", "W", 23), ("W", "C", -22)], "W", "C"), -22),
    (
        (
            [("K", "P", 30), ("I", "P", 21), ("I", "K", 19), ("P", "I", -20)],
            "P",
            "K",
        ),
        -1,
    ),
]


def bruteforce_solve(S, R, s, g):
    S.remove(s)
    S.remove(g)
    R = {(a, b): e for a, b, e in R}
    sol = float("inf")
    for i in range(0, len(S)):
        for perm in itertools.permutations(S, r=i):
            cost = 0
            perm = tuple([s]) + perm + tuple([g])
            for x, y in zip(perm, perm[1:]):
                if (x, y) not in R:
                    break
                cost += R[(x, y)]
            else:
                sol = min(sol, cost)
    return sol


def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(max(1, nl), nu)
        ns = random.randint(
                max(5, math.ceil(1.2*math.ceil(math.sqrt(n)))),
                max(5, min(2*math.ceil(math.sqrt(n)), n))
            )
        substances = set()
        while len(substances) < ns:
            substances.add(
                "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                        k=math.ceil(math.log(ns, 20))))
            )
        substances = tuple(substances)

        R = dict()
        for _ in range(n):
            a, b = substances[:2]
            while (a, b) in R:
                a, b = random.sample(substances, k=2)

            R[(a, b)] = random.randint(-50, 99)

        for i in range(2, len(substances) + 1):
            for perm in itertools.permutations(substances, r=i):
                if all((a, b) in R for a, b in zip(perm, perm[1:] + perm[:1])):
                    e = sum(R[(a, b)] for a, b in zip(perm, perm[1:] + perm[:1]))
                    if e < 0:
                        R[(perm[0], perm[1])] += -e

        R = [(*x, e) for x, e in R.items()]
        random.shuffle(R)


        s, g = random.sample(substances, k=2)
        while bruteforce_solve(set(substances), R, s, g) == float("inf"):
            s, g = random.sample(substances, k=2)

        yield (R, s, g), bruteforce_solve(set(substances), R, s, g)



if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        reactions_lower,
        reactions_upper,
    ))


def get_feedback(student, answer, reactions, start, goal):
    if type(student) != list:
        return "Du returnerte ikke en liste"
    if len(student) < 2:
        return "Du returnerte en liste med færre en to elementer"
    if student[0] != start:
        return "Listen din starter ikke med startstoffet"
    if student[-1] != goal:
        return "Listen din ender ikke med målstoffet"
    costs = {}
    for a, b, e in reactions:
        costs[(a, b)] = e
    cost = 0
    for i in range(len(student) - 1):
        if (student[i], student[i + 1]) not in costs:
            return "Du gjør en reaksjon som ikke er lov"
        cost += costs[(student[i], student[i + 1])]
    if cost > answer:
        return "Du lager ikke stoffet på den mest energieffektive måten"


failed = False
for test_case, answer in tests:
    reactions, start, goal = test_case
    student = least_energy(reactions[:], start, goal)
    response = get_feedback(student, answer, reactions, start, goal)
    if response is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
start: {start}
goal: {goal}
reactions:
    {(chr(10) + '    ').join(f"{a} -> {b} (energi: {e})" for a, b, e in reactions)}

Ditt svar: {student}
Minste mulige energi: {answer}
Feilmelding: {response}
""")


if not failed:
    print("Koden fungerte for alle eksempeltestene.")