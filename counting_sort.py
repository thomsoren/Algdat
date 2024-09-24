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
    # Skriv koden din her
    highest = 0

    for num in A:
        if num > highest:
            highest = num
    #finne høyeste tall k først. 
    k = highest
    
    B = [0] * n
    C = [0] * (k + 1)

    # Count occurrences
    for j in range(n):
        C[A[j]] += 1

    # Cumulative counts
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    # Build the output array
    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

# Hardkodete tester
tests = [
    [],
    [1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 1, 2, 1],
    [1281, 1, 2],
    [0, 2047, 0, 2047],
    [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
    [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        yield [
                random.randint(0, 2047)
                for _ in range(random.randint(lower, upper))
            ]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A in tests:
    answer = sorted(A)
    student = counting_sort(A[:], len(A))
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
A: {A}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")