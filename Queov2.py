import random
from math import erf, sqrt
class Queue:
    
    def __init__(self, max_size):
        self.tail = 0
        self.head = 0
        self.list = [] 
        self.size = max_size
    

        # Initialiser de underliggende datastrukturene her

    def enqueue(self, value):
        # Hvis lista er full, ikke gjør noe
        if len(self.list) == self.size:
            print("Queue is full!")
            return
        # Hvis lista er tom

        # Legg til ny verdi der halen er
        self.list.append(value)
        if self.tail == self.size:
            self.tail = 0
        else: 
            self.tail = self.tail + 1
        return self.list


    def dequeue(self):
        if len(self.list) == 0:
            return self.list
        
        x = self.list.pop(0)
        if self.head == self.size:
            self.head = 0
        else:
            self.head = self.head + 1
        return x
    

q1 = Queue(3)
q1.enqueue(1)
print(q1.list)
q1.dequeue()
print(q1.list)
q1.enqueue(3)
print(q1.list)
q1.enqueue(7)
print(q1.list)
q1.enqueue(2)
print(q1.list)
q1.dequeue()
print(q1.list)


# Hardkodetete tester på format (verdier, operasjoner, maksimum størrelse)
tests = [
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        3,
    ),
    (
        [1, 7, 3],
        ("enqueue", "dequeue", "enqueue", "dequeue", "enqueue", "dequeue"),
        1,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "enqueue",
            "dequeue",
            "dequeue",
        ),
        2,
    ),
    (
        [-1, 12, 0, 99],
        (
            "enqueue",
            "enqueue",
            "enqueue",
            "enqueue",
            "dequeue",
            "dequeue",
            "dequeue",
            "dequeue",
        ),
        4,
    ),
]

multiple_queues_tests = [
    (
        [
            [-525, -593, -224, -965, 321, 910, -203, -667],
            [-876, -867, 170, -422, 229, 508, 247, 619],
            [666, 147, -59, -160, 426, -895, 248, -730]
        ],
        [
            (
                'enqueue',
                'enqueue',
                'enqueue',
                'enqueue',
                'enqueue',
                'dequeue',
                'dequeue',
                'enqueue',
                'enqueue',
                'enqueue',
                'dequeue',
                'dequeue',
                'dequeue',
                'dequeue',
                'dequeue',
                'dequeue'
            ),
            (
                'enqueue',
                'dequeue',
                'enqueue',
                'enqueue',
                'dequeue',
                'dequeue',
                'enqueue',
                'dequeue',
                'enqueue',
                'dequeue',
                'enqueue',
                'dequeue',
                'enqueue',
                'enqueue',
                'dequeue',
                'dequeue'
            ),
            (
                'enqueue',
                'enqueue',
                'enqueue',
                'dequeue',
                'enqueue',
                'dequeue',
                'dequeue',
                'dequeue',
                'enqueue',
                'enqueue',
                'enqueue',
                'dequeue',
                'enqueue',
                'dequeue',
                'dequeue',
                'dequeue'
            )
        ],
        3,
        7,
    ),
]


# CDF for normalfordeling
def cdf(mean, sd, x):
    return (1.0 + erf((x - mean) / (sd*sqrt(2.0)))) / 2.0


# Generer en instans. Lastfaktoren varierer tilfeldig basert på en
# tilnærmet normalfordeling.
def gen_example(n_lower, n_upper):
    n = random.randint(n_lower, n_upper)
    max_size = random.randint(1, max(n // 4, 1))
    mean = random.randint(1, max_size)
    sd = random.randint(1, max(max_size // 3, 1))
    values = [random.randint(-99, 99) for _ in range(n)]
    sequence = []
    load = 0
    while len(sequence) < 2*n:
        action = "undecided"
        if load == max_size or load + len(sequence) == 2*n:
            action = "dequeue"
        elif load > 0:
            action = ["enqueue", "dequeue"][random.random() < cdf(mean, sd, load)]
        else:
            action = "enqueue"

        if action == "dequeue":
            load -= 1
        else:
            load += 1

        sequence.append(action)

    return values, sequence, max_size




def tester(values, sequence, max_size, has_failed):
    """
    Tester en oppgitt sekvens av operasjoner og sjekker at verdiene
    (values) kommer ut i riktig rekkefølge.
    """
    index = 0
    queue = Queue(max_size)
    output = []
    for action in sequence:
        if action == "enqueue":
            queue.enqueue(values[index])
            index += 1
        elif action == "dequeue":
            output.append(queue.dequeue())

    if output != values:
        if has_failed:
            print("-"*50)

        print(f"""
Feilet for følgende instans:
Operasjoner: {", ".join(sequence)}
Verdier: {", ".join(map(str, values))}
Maksimal størrelse: {max_size}

Din implementasjon produserte følgende output fra `dequeue`-operasjonene:
{", ".join(map(str, output))}
""")
        return True
    return False

def test_multiple_queues(values, sequences, number_of_queues, max_size,
                         has_failed):
    queues = [Queue(max_size) for _ in range(number_of_queues)]
    outputs = [[] for _ in range(number_of_queues)]
    indexes = [0] * number_of_queues

    for i in range(len(sequences[0])):
        for j in range(number_of_queues):
            if sequences[j][i] == "enqueue":
                queues[j].enqueue(values[j][indexes[j]])
                indexes[j] += 1
            elif sequences[j][i] == "dequeue":
                outputs[j].append(queues[j].dequeue())

    failed_flag = False
    feedback = f"\nKoden feilet når den ble kjørt med {number_of_queues} køer samtidig:\n"
    for queue_number, (input, output) in enumerate(zip(values, outputs)):
        if input != output:
            failed_flag = True
            feedback += f"""
-----
Kø {queue_number + 1}:
-----
Produserte feil svar!

Operasjoner: {", ".join(sequences[queue_number])}
Verdier: {", ".join(map(str, values[queue_number]))}
Maksimal størrelse: {max_size}

Din implementasjon produserte følgende output fra `dequeue`-operasjonene:
{", ".join(map(str, output))}
"""
        else:
            feedback += f"""
-----
Kø {queue_number + 1}:
-----
Produserte riktig svar!

Operasjoner: {", ".join(sequences[queue_number])}
Verdier: {", ".join(map(str, values[queue_number]))}
Maksimal størrelse: {max_size}
"""
    if failed_flag:
        if has_failed:
            print("-"*50)
        print(feedback)
    return failed_flag


failed = False

for values, sequence, max_size in tests:
    failed |= tester(values, sequence, max_size, failed)

for values, sequences, number_of_queues, max_size in multiple_queues_tests:
    failed |= test_multiple_queues(values, sequences, number_of_queues,
                                   max_size, failed)

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")