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
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall tall i generert instans.
numbers_lower = 3
# Høyest mulig antall tall i generert instans.
numbers_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def counting_sort(A, n):
    if n == 0:
        return []

    min_value = min(A)
    max_value = max(A)
    range_of_elements = max_value - min_value + 1

    B = [0] * n
    C = [0] * range_of_elements

    # Count occurrences
    for j in range(n):
        C[A[j] - min_value] += 1

    # Cumulative counts
    for i in range(1, range_of_elements):
        C[i] += C[i - 1]

    # Build the output array
    for j in range(n - 1, -1, -1):
        B[C[A[j] - min_value] - 1] = A[j]
        C[A[j] - min_value] -= 1

    return B

def k_largest(A, n, k):
    liste = counting_sort(A, n)
    ny_liste = []
    for i in range(n - 1, n - k - 1, -1):
        ny_liste.append(liste[i])
    return ny_liste
    # r = len(A)
    # p = 0

    # while (r-p+1)%5 !=0:
    #     for j in range(p+1,r):
    #         if A[p] > A[j]:
    #             A[p], A[j] = A[j],A[p]
    # if i == 1:
    #     return A[p]
    # p = p + 1
    # i = i - 1 

    # g = (r - p + 1) / 5
    # for j in range(p, p+g -1):
    #     sort A[j + () *g]
    # x = Select(A, p+2*g, p+ 3*g -1, g//2)

    # q = Partition-Around(A, p, r, x)
    # k = q - p + 1
    # if i == k:
    #     return A[q]
    # elif i < k:
    #     return Select(A, p, q-1, i)
    # else:
    #     return Select(A, q + 1, r, i -k)


# Sett med hardkodete tester på format: (A, k)
tests = [
    ([], 0),
    ([1], 0),
    ([1], 1),
    ([1, 2], 1),
    ([-1, -2], 1),
    ([-1, -2, 3], 2),
    ([1, 2, 3], 2),
    ([3, 2, 1], 2),
    ([3, 3, 3, 3], 2),
    ([4, 1, 3, 2, 3], 2),
    ([4, 5, 1, 3, 2, 3], 4),
    ([9, 3, 6, 1, 7, 3, 4, 5], 4),
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        A = [
                random.randint(-50, 50)
                for _ in range(random.randint(lower, upper))
            ]
        yield A, random.randint(0, len(A))


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A, k in tests:
    answer = sorted(A, reverse=True)[:k][::-1]
    student = k_largest(A[:], len(A), k)

    if type(student) != list:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}
k: {k}

Metoden må returnere en liste
Ditt svar: {student}
""")
    else:
        student.sort()
        if student != answer:
            if failed:
                print("-"*50)
            failed = True
            print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}
k: {k}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")