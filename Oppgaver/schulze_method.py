# !/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 500 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True. Merk at det kan
# ta litt tid å kjøre alle de 500 ekstra testene.
use_extra_tests = False

def schulze_method(A, n):
    # Lag matrise p
    p = [[0 for _ in range(n)] for _ in range(n)]
    
    # Sett verdier i p 
    for i in range(n):
        for j in range(n):
            if i != j:
                if A[i][j] > A[j][i]:
                    p[i][j] = A[i][j]
                else:
                    p[i][j] = 0
    
    # Floyd-Warshall for å regne ut p
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue
                p[i][j] = max(p[i][j], min(p[i][k], p[k][j]))
    
    # Ranger kandidater
    C = list(range(n))
    resultat = []
    
    while C:
        # Finn kandidater som slår alle andre i C
        potential_winners = []
        for u in C:
            beats_all = True
            for v in C:
                if u != v and p[u][v] <= p[v][u]:
                    beats_all = False
                    break
            if beats_all:
                potential_winners.append(u)
        
        if potential_winners:
            # Velg en kandidat med lavest index
            winner = min(potential_winners)
            resultat.append(winner)
            C.remove(winner)
            continue
        
        # Hvis det er ingen klar vinner, bruk regler som gjelder når uavgjort
        # Finner kandidater med p(u, v) >= p(v, u) for alle v
        candidates = []
        for u in C:
            if all(p[u][v] >= p[v][u] for v in C if v != u):
                candidates.append(u)
        
        if candidates:
            # Velg den som slår flest andre
            max_beats = -1
            selected = []
            for u in candidates:
                beats = sum(1 for v in C if v != u and p[u][v] > p[v][u])
                if beats > max_beats:
                    max_beats = beats
                    selected = [u]
                elif beats == max_beats:
                    selected.append(u)
            # Velg kandidaten med lavest index
            winner = min(selected)
            resultat.append(winner)
            C.remove(winner)
            continue
        
        # Ellers velg kandidat med lavest index
        winner = min(C)
        resultat.append(winner)
        C.remove(winner)
    
    return resultat


# Hardkodete tester på format: (A, svar)
tests = [
    ([[0]], [0]),
    ([[0, 1], [3, 0]], [1, 0]),
    ([[0, 2], [2, 0]], [0, 1]),
    ([[0, 4, 3], [2, 0, 2], [3, 4, 0]], [0, 2, 1]),
    ([[0, 2, 1], [4, 0, 4], [5, 2, 0]], [1, 2, 0]),
    (
        [
            [0, 1, 3, 3, 3],
            [9, 0, 5, 5, 7],
            [7, 5, 0, 5, 4],
            [7, 5, 5, 0, 6],
            [7, 3, 6, 4, 0],
        ],
        [1, 3, 4, 2, 0],
    ),
    (
        [
            [0, 6, 7, 8, 7, 8],
            [6, 0, 6, 8, 7, 8],
            [5, 6, 0, 6, 5, 7],
            [4, 4, 6, 0, 5, 6],
            [5, 5, 7, 7, 0, 6],
            [4, 4, 5, 6, 6, 0],
        ],
        [0, 1, 4, 2, 3, 5],
    ),
]


def validate(student, answer):
    try:
        len(student)
    except:
        return "Koden returnerte ikke en liste"

    if len(student) != len(answer):
        return "Listen inneholder ikke riktig antall kandidater"

    if set(student) != set(answer):
        return "Listen inneholder ikke alle kandidatene"

    if any(a != b for a, b in zip(student, answer)):
        return "En eller flere av kandidatene opptrer i feil rekkefølge"


def generate_feedback(test, expected, student):
    feedback = ""
    feedback += "Koden din feilet for input\n"
    feedback += str(test) + "\n"
    feedback += "Ditt svar er\n"
    feedback += str(student) + ",\n"
    feedback += "men riktig svar er\n"
    feedback += str(expected) + "."
    return feedback


table_format = lambda T: "\n    " + "\n    ".join(map(str, T))
failed = False
for A, answer in tests:
    student = schulze_method([row[:] for row in A], len(A))
    feedback = validate(student, answer)
    if feedback is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
A: {table_format(A)}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")

if use_extra_tests:
    with open("tests_schulze_method.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            A, answer = map(eval, line.strip().split(" | "))
            extra_tests.append((A, answer))

    n_failed = 0
    for A, answer in extra_tests:
        student = schulze_method([row[:] for row in A], len(A))
        feedback = validate(student, answer)
        if feedback is not None:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans.
A: {table_format(A)}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din passerte alle eksempeltestene.")