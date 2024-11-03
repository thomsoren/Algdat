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
# Laveste mulige antall dyr i generert instans.
animals_lower = 3
# Høyest mulig antall dyr generert instans.
# NB: Om dette antallet settes høyt (>9) vil det ta veldig lang tid å kjøre
# testene, da svaret på instansene finnes ved bruteforce.
animals_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def hamming_distance(s1, s2):
    # Skriv koden din her
    pass


def find_clusters(E, n, k):
    """
    Finner k klynger ved hjelp av kantene i E. Kantenen i E er på
    formatet (i, j, avstand), hvor i og j er indeksen til noden (dyret)
    kanten knytter sammen og avstand er Hamming-avstanden mellom
    gensekvensen til dyrene. Funksjonen returnerer en liste av k
    lister. Hvor de indre listene representerer en klynge og består av
    indeksene til nodene (dyrene). F.eks. har vi tre dyr som skal
    i to klynger, hvor dyr 0 og 2 ender i samme klynge returnerer
    funksjonen [[0, 2], [1]].

    :param E: Kanter i grafen på formatet (i, j, avstand). i og j er
              indeksen til dyrene kanten går mellom.
    :param n: Antall noder
    :param k: Antall klynger som ønskes
    :return: En liste av k lister.
    """
    # Skriv koden din her
    pass


def find_animal_groups(animals, k):
    # Lager kanter basert på Hamming-avstand
    E = []
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            E.append((i, j, hamming_distance(animals[i][1], animals[j][1])))

    # Finner klynger
    clusters = find_clusters(E, len(animals), k)

    # Gjøre om fra klynger basert på indekser til klynger basert på dyrenavn
    animal_clusters = [
        [animals[i][0] for i in cluster] for cluster in clusters
    ]
    return animal_clusters


# Hardkodete tester på format: animals, k, optimal_vekt
tests = [
    ([("Ugle", "AGTC"), ("Ørn", "AGTA")], 2, 1),
    ([("Ugle", "CGGCACGT"), ("Elg", "ATTTGACA"), ("Hjort", "AATAGGCC")], 2, 8),
    (
        [("Ugle", "ATACTCAT"), ("Hauk", "AGTCTCAT"), ("Hjort", "CATGGCCG")],
        2,
        6,
    ),
    (
        [
            ("Ugle", "CGAAGTTA"),
            ("Hauk", "CGATGTTA"),
            ("Hamster", "AAAATCAC"),
            ("Mus", "AAAATGAC"),
        ],
        2,
        6,
    ),
    (
        [
            ("Ugle", "CAAACGAT"),
            ("Spurv", "CAGTCTAA"),
            ("Mus", "TCTGGACG"),
            ("Hauk", "CGAACTAT"),
        ],
        2,
        8,
    ),
    (
        [
            ("Ugle", "ATAACTCC"),
            ("Hauk", "TTACCTCC"),
            ("Hjort", "AGTGAACC"),
            ("Mus", "GTAGGACC"),
            ("Spurv", "ATGTCCCA"),
        ],
        3,
        4,
    ),
    (
        [
            ("Hauk", "CCTACTGATGACGCGC"),
            ("Ugle", "CCTAGTGATGAAGCAC"),
            ("Hjort", "ACTTTAACATCGCGGG"),
            ("Spurv", "ACGACTGATGAAGCAC"),
            ("Mus", "GTTAGACAATGGAGTG"),
            ("Rotte", "GTCGTACAATTGAGTG"),
        ],
        3,
        9,
    ),
    (
        [
            ("Ugle", "GGAGACCGGCTTCCTA"),
            ("Marsvin", "GCTACCTTGCTCACGT"),
            ("Hauk", "CGAGACCAGCTGCTGG"),
            ("Hjort", "GACATCTCTGTTCGGC"),
            ("Spurv", "GGAGACCGGCTTCCTG"),
            ("Rotte", "ACTACCTTGCGCACGA"),
            ("Mus", "TCTACCTTGCCCACGA"),
        ],
        3,
        10,
    ),
    (
        [
            ("Spurv", "TAGCAGTTCCTGAGAA"),
            ("Hjort", "ATGCATATCAGACGAT"),
            ("Ugle", "TAGCGATTTCAGAATT"),
            ("Rotte", "GACGGATTATTCCCCA"),
            ("Marsvin", "GAGGAATGGTAATCGC"),
            ("Hauk", "GATCGGTATCAGAACT"),
            ("Elg", "ATTCGTATAACCAAAG"),
            ("Mus", "GAGGGATGCTCCTCCC"),
        ],
        3,
        9,
    ),
    (
        [
            ("Katt", "CCGTGGTATCAAATAA"),
            ("Hjort", "TTACAGGCGGGCGTTC"),
            ("Hauk", "GGGAAATGAGCTTTCT"),
            ("Rotte", "ATCCTATAATGACCCT"),
            ("Elg", "TTGCATGCGGGCGATT"),
            ("Marsvin", "TTCGGCGGAGGTTCTA"),
            ("Mus", "ATCGGAGGAGGATCTC"),
            ("Ugle", "GGCTAGTGCGCTTTTT"),
            ("Spurv", "TGCCAGTCCGCTTTAT"),
        ],
        4,
        9,
    ),
    (
        [
            ("Hjort", "GATTACCCATGCTGGA"),
            ("Leopard", "TTTTCCTACCTAGTTA"),
            ("Ugle", "TCCCGGGAAGGGGATG"),
            ("Hauk", "TCCCAGCAAGGGGCTG"),
            ("Rotte", "CGCAGGACCGGAGGCA"),
            ("Spurv", "TCACGTGACGGGGGTG"),
            ("Katt", "TTTTCCTAACGGGTTA"),
            ("Mus", "CGCCGGAGCGAAACTA"),
            ("Elg", "GTATAGCTGTGCAGGA"),
            ("Marsvin", "AGCTGGGGCGTCAAGA"),
        ],
        4,
        9,
    ),
    (
        [
            ("Spurv", "AATCCCTGTAACGCGT"),
            ("Rotte", "CACCAGTCCGAGGAAC"),
            ("Leopard", "CACCCTATATCAAAGG"),
            ("Hauk", "AAATTGTCTCACGGGG"),
            ("Mus", "CACCACTCCTAGGAAC"),
            ("Elg", "ATGAGAGAGAGCTCCT"),
            ("Hjort", "ATGCTAGTGGGCCGCT"),
            ("Elefant", "TTTGAACAGTTTTAAT"),
            ("Marsvin", "AAGCCCTCAGAGCAAC"),
            ("Nesehorn", "TTTGACCAGTATTAAC"),
            ("Ugle", "AAAATGTCTAACGAGG"),
            ("Katt", "CACCCTATACCAAAGG"),
        ],
        5,
        9,
    ),
]


# Finner største mulig separasjonsavstand med bruteforce
def bruteforce_solve(A, k):
    def z(Z, R):
        t = lambda x: abs(ord(x[-1])-ord(x[-2]))>0
        if not R:
            return min(
                min(sum(map(t, zip(a[1],b[1]))) for a in A for b in B)
                for A, B in itertools.permutations(Z, r=2)
            )
        m = 0
        for i in range(len(Z)):
            m = max(m, z([A if i != j else A + [R[0]] for j,A in enumerate(Z)],
                         R[1:]))
        return m
    return max(z([[x] for x in X], [a for a in A if a not in X])
               for X in itertools.combinations(A, k))


def gen_examples(nl, nu, k):
    A = ["Spurv", "Rotte", "Leopard", "Hauk", "Mus", "Elg", "Hjort", "Elefant",
         "Marsvin", "Nesehorn", "Ugle", "Katt", "Hund", "Ekorn", "Ape",
         "Slange", "Gorilla", "Gaupe", "Lemen", "Bjørn", "Piggsvin", "Pingvin",
         "Flaggermus", "Rein", "Moskus", "Dåhjort", "Rådyr", "Nise",
         "Spermhval", "Blåhval", "Ulv", "Røyskatt", "Jerv", "Mink", "Oter",
         "Grevling", "Isbjørn", "Hvalross", "Sel", "Kanin", "Hare", "Bever",
         "Sjiraff", "Løve", "Påfugl"]
    dna_gen = lambda x: "".join(random.choices("ACGT", k=x))
    for _ in range(k):
        n = random.randint(nl, nu)
        if n <= len(A):
            animals = random.sample(A, n)
        else:
            animals = [f"Animal{i}" for i in range(1, n + 1)]
        animals = [(a, dna_gen(10)) for a in animals]
        k = random.randint(2, n)
        yield animals, k, bruteforce_solve(animals, k)


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        animals_lower,
        animals_upper,
        random_tests
    ))

def check(animals, k, optimal, clusters):
    if type(clusters) != list:
        return "find_animal_groups skal returnere en liste av klynger."

    if len(clusters) != k:
        return f"Det skal være {k} klynger ikke {len(clusters)}."

    cluster_animals = [animal for cluster in clusters for animal in cluster]
    if len(cluster_animals) > len(animals):
        return "Klyngene dine inneholder flere elementer enn det som finnes."

    if len(cluster_animals) > len(set(cluster_animals)):
        return "Klygene dine inneholder duplikater"

    if set(name for name, _ in animals) != set(cluster_animals):
        return "Klygene dine inneholder ikke alle dyrene"

    lookup = {
        animal: index
        for index, cluster in enumerate(clusters)
        for animal in cluster
    }
    t = lambda x: x[0] != x[1]
    sep_dist = min(
        sum(map(t, zip(a1[1], a2[1])))
        for a1, a2 in itertools.combinations(animals, 2)
        if lookup[a1[0]] != lookup[a2[0]]
    )
    if sep_dist < optimal:
        return f"""
Klyngene har ikke maksimal separasjonsavstand. Den maksimale
seperasjonsavstanden er {optimal}, men koden resulterte i en seperasjonsavstand
på {sep_dist}."""

    return False


failed = False
for animals, k, optimal in tests:
    clusters = find_animal_groups(animals[:], k)
    incorrect = check(animals, k, optimal, clusters)
    if incorrect:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
animals: {animals}
k: {k}

Ditt svar: {clusters}
Feilmelding: {incorrect}
""")

if not failed:
    print("Koden fungerte for alle eksempeltestene.")
