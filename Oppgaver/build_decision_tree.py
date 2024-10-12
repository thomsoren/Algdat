#!/usr/bin/python3
# coding=utf-8
import random
import uuid
from math import log, ceil

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
# Lavest mulig antall utfall.
n_lower = 3
# Høyest mulig antall utfall.
n_upper = 10
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


class TestNode:
    def __init__(self, i):
        self.function = i
        self.true = None
        self.false = None
        self.index = None


class LeafNode:
    def __init__(self, name):
        self.name = name

def build_decision_tree_highscore(decisions, T):
    return build_tree(decisions, T)

def build_tree(decisions, T):
    if len(decisions) == 1:
        return LeafNode(decisions[0][0])

    best_balance = None
    best_test_index = None
    best_splits = None

    # itererer igjennom T og har med index for å brukes senere i funksjonen
    for i, T_func in enumerate(T):

        # lager to lister med sanne og usanne valg
        true_decisions = []
        false_decisions = []

        # hvis testfunksjonen blir true av name som input legger vi til valget i "true_decisions" ellers i "false_decisions"
        for name, prob in decisions:
            if T_func(name):
                true_decisions.append((name,prob))
            else:
                false_decisions.append((name,prob))

        # Skip hvis testen ikke splitter opp på valg
        if not true_decisions or not false_decisions:
            continue

        # Sum av sannsynligheter i true og false 
        true_prob = sum(prob for _, prob in true_decisions)
        false_prob = sum(prob for _, prob in false_decisions)

        # regner ut balansen mellom true og false, 0 er balansert, høye verdier er ubalansert
        balanse = abs(true_prob - false_prob)

        # hvis beste balanse ikke er satt enda eller gjeldene balanse er best: så setter vi balanse, index og split
        if best_balance is None or balanse < best_balance:
            best_balance = balanse
            best_test_index = i
            best_splits = (true_decisions, false_decisions)

    # hvis index ikke ble gitt
    if best_test_index is None:
        # finner mest sansynlig avgjørelse
        highest_prob = 0
        for name, prob in decisions:
            if prob >= highest_prob:
                most_probable_decision = name
        return LeafNode(most_probable_decision)
    
    # Lager nye noder rekursivt helt til vi står igjen med én rotnode
    node = TestNode(best_test_index)
    node.true = build_tree(best_splits[0], T)
    node.false = build_tree(best_splits[1], T)
    return node





# Hardkodete tester på formatet: decisions, tests
tests = [
    ([("a", 0.5), ("b", 0.5)], [lambda x: x == "a"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x == "a", lambda x: x == "b"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x in ["a", "b"], lambda x: x == "b"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"]]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.2), ("d", 0.2)], [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"]]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.2), ("d", 0.2)],
     [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"], lambda x: x == "d"]),
]


def test_answer(student, decisions, functions):
    if not isinstance(student, TestNode):
        print("Testen feilet: rotnoden i svaret er ikke en TestNode")
        return -1

    expectance = 0
    for name, prob in decisions:
        questions = 0
        node = student
        while isinstance(node, TestNode):
            questions += 1
            if functions[node.function](name):
                node = node.true
            else:
                node = node.false

        if not isinstance(node, LeafNode):
            print("Testen feilet: noden som ble nådd for {:} er ikke en løvnode".format(name))
            return -1

        if name != node.name:
            print(
                "Testen feilet: Løvnoden som nås av {:} tilhører ikke denne beslutningen".format(
                    name
                )
            )
            return -1

        expectance += prob * questions

    return expectance

def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(max(2, nl), nu)
        decisions = set()
        while len(decisions) < n:
            decisions.add(
                "".join(random.choices("abcdefghijklmnopqrstuvwxyz",
                                       k=ceil(log(n, 26)) + 1))
            )
        prob = [random.randint(1, 10*n) for _ in range(n)]
        scale = sum(prob)
        decisions = [(a, b/scale) for a,b in zip(decisions, prob)]

        def gen_test(var):
            def test(x):
                return x in var
            return test

        names = [a for a,_ in decisions]
        tests = [
            gen_test(random.sample(names, k=random.randint(0, len(names))))
            for _ in range(random.randint(n//3, 3*n))
        ]

        for a in names:
            for b in names:
                if a == b:
                    continue
                if all(test(a) == test(b) for test in tests):
                    subset = random.sample(names, k=random.randint(0, len(names)))
                    if a not in subset:
                        subset.append(a)
                    if b in subset:
                        subset.remove(b)
                    tests.append(gen_test(subset))


        yield decisions, tests


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(random_tests, n_lower, n_upper))

first = True
for test_num, test in enumerate(tests):
    if not first:
        print("-"*50)

    first = False

    tests_string = ""
    for i, check in enumerate(test[1]):
        tests_string += f"T{i + 1}: "
        tests_string += "   ".join(f"{a}={str(check(a)).ljust(5)}" for a, _ in test[0])
        tests_string += "\n"

    print(f"""
Kjører følgende test:
decisions:
{chr(10).join(x + ": " + str(y) for x,y in test[0])}

tests:
{tests_string}
    """)

    student = build_decision_tree_highscore(test[0], test[1])
    result = test_answer(student, test[0], test[1])

    if result != -1:
        print(f"Fikk en forventing på {result}")
    print()