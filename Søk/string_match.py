# !/usr/bin/python3
# coding=utf-8
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å juste på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres
random_tests = 10
# Lavest mulig antall tegn i dna.
n_lower = 3
# Høyest mulig antall tegn i dna.
n_upper = 100
# Lavest mulig antall tegn i hvert segment.
d_lower = 1
# Høyest mulig antall tegn i hvert segment.
d_upper = 10
# Lavest mulig antall segmenter.
k_lower = 1
# Høyest mulig antall segmenter.
k_upper = 20
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


# def string_match(dna, segments):
#     # dna er sekvens(streng) vi skal søke i
#     # liste av dna segmenter (liste med strenger)
#     #   Hvis lengden på dna er n
#     # n, antallet DNA-segmenter er k
#     # k og det lengste av DNA-segmentene er d
#     # d, må koden din ha en kjøretid på O(d(n+k))
#     # O(d(n+k)) for å bli godkjent.
        
#     count = 0
    
#     for seg in segments:
#         for i in range(len(dna) - len(seg) + 1):
#             if dna[i:i+len(seg)] == seg:
#                 count += 1
#         # telle antall ganger seg i dna streng

#     # returnere antall ganger DNA-segmentene forekommer i DNA sekvensen
#     return count

def string_match(dna, segments):
    count = 0
    # bygger treet
    root = build_tree(segments)

    n = len(dna)
    # For hver posisjon i dna, prøv å matche segmentene som starter fra den posisjonen 
    for i in range(n):
        current_node = root
        j = i
        while j < n and dna[j] in current_node.children:
            current_node = current_node.children[dna[j]]
            if current_node.is_end_of_word:
                count += current_node.count
            j += 1
    return count

def build_tree(segments):
    root = Node()
    for seg in segments:
        current_node = root
        for letter in seg:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node.children[letter] = Node()
                current_node = current_node.children[letter]
        current_node.is_end_of_word = True
        current_node.count += 1 
    return root


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end_of_word = False

    def __str__(self):
        return (
            f"{{count: {self.count}, children: {{"
            + ", ".join(
                [f"'{c}': {node}" for c, node in self.children.items()]
            )
            + "}"
        )




# Hardkodete tester på format: ((dna, segments), riktig svar)
tests = [
    (("A", []), 0),
    (("AAAA", ["A"]), 4),
    (("ACTTACTGG", ["A", "ACT", "GG"]), 5),
    (("AAAAAAAAAAAAAAAAAAAA", ["A"]), 20),
    (("AAAAAAAAAAAAAAAAAAAA", ["AA"]), 19),
    (("AAAAAAAAAAAAAAAAAAAA", ["A", "A"]), 40),
    (("AAAAAAAAAAAAAAAAAAAA", ["A", "AA"]), 39),
    (("ABABABABABABABABABAB", ["AB"]), 10),
    (("ABABABABABABABABABAB", ["A", "AB"]), 20),
    (("ABABABABABABABABABAB", ["A", "B"]), 20),
]


# Løser problemet ved bruteforce. Har kjøretid Ω(kn).
def bruteforce_solve(dna, segments):
    counter = 0
    for segment in segments:
        for i in range(len(dna) - len(segment) + 1):
            if dna[i : i + len(segment)] == segment:
                counter += 1
    return counter


def gen_examples(k, nl, nu, dl, du, kl, ku):
    for _ in range(k):
        n = random.randint(nl, nu)
        k_ = random.randint(kl, ku)
        dna = "".join(random.choices("AGTC", k=n))
        segments = [
            "".join(random.choices("AGTC", k=random.randint(dl, du)))
            for _ in range(k_)
        ]
        yield (dna, segments), bruteforce_solve(dna, segments)


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        n_lower,
        n_upper,
        d_lower,
        d_upper,
        k_lower,
        k_upper,
    ))

failed = False

for test_case, answer in tests:
    dna, segments = test_case
    student_answer = string_match(dna, segments[:])
    if student_answer != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
dna: {dna}
segments: {", ".join(segments)}

Ditt svar: {student_answer}
Riktig svar: {answer}
""")

if not failed:
    print("Koden din fungerte for alle eksempeltestene")