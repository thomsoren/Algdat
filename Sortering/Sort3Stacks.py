#!/usr/bin/python3
# coding=utf-8
import random


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raises an error if the stack is empty."""
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """Return the top item of the stack without removing it. Raises an error if the stack is empty."""
        if not self.empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

def printStack():
    s1_list = []
    s2_list = []
    s3_list = []
    for element in stack1.items:
        s1_list.append(element)

    for element in stack2.items:
        s2_list.append(element)

    for element in stack3.items:
        s3_list.append(element)
    print(s1_list)
    print(s2_list)
    print(s3_list)
    

def sort(stack1, stack2, stack3):
    
    # stack 1 er resultat
    # stack 2 og 3 er hjelpestacks

    # pop øverste element fra stack1 og legg til i stack3

    # popper øverste element fra stack1 og legger til i stack2
    # deretter popper vi øverste element fra stack1 og sammenligner med elementet i stack2 som vi nettopp la til
    # hvis elementet i stack1 er større enn elementet i stack2,  til stack3



    sorted = False
    while not sorted:
        sorted = True

        while not stack1.empty():
            top1 = stack1.pop()

            if (stack2.empty()):
                stack2.push(top1)
            else:
                if top1 >= stack2.peek():
                        stack2.push(top1)
                else:
                    stack3.push(top1)
        
       
        
        while not stack2.empty() or not stack3.empty():
            #hvis stack2 og stack3 har tall i seg
            if not stack2.empty() and not stack3.empty():
                #skjekk hva som er i 2 og 3
                    peek2 = stack2.peek()
                    peek3 = stack3.peek() 
                    #hvis det i 2 er større enn 3 
                    if peek2 > peek3:    
                        #hvis 1 ikke er tom kan du sammenligne 1 og 2 om de er sortert og så legge 2 i 1
                        if not stack1.empty():
                            if stack1.peek() < peek2:
                                sorted = False
                        stack1.push(stack2.pop())       
    
                    #ellers hvis 
                    else:
                        if not stack1.empty():
                            if stack1.peek() < peek3:
                                sorted = False
                        stack1.push(stack3.pop())
            elif not stack2.empty():
                if not stack1.empty():
                    if stack1.peek() < stack2.peek():
                        sorted = False
                stack1.push(stack2.pop())
            else:
                if not stack1.empty():
                    if stack1.peek() < stack3.peek():
                        sorted = False
                stack1.push(stack3.pop())


    return stack1, stack2, stack3


stack1 = Stack()
stack2 = Stack()
stack3 = Stack()
stack1.push(1)
stack1.push(1)
stack1.push(1)
stack1.push(1)

printStack()

sort(stack1, stack2, stack3)

printStack()


# Hardkodetetester, høyre side blir toppen av stakken
tests = [
    [4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 2, 1, 7],
    [1, 1, 1, 1],
    [7, 3, 9, 2, 0, 1, 3, 4],
    [7, 3, 0, 13, 48, 49, 233, 9, 2, 0, 1, 3, 4],
]

# Genererer k tilfeldige tester, hver med et tilfeldig antall elementer plukket
# uniformt fra intervallet [nl, nu].
def gen_examples(k, nl, nu):
    for _ in range(k):
        yield [random.randint(-99, 99) for _ in range(random.randint(nl, nu))]



class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, operation_counter, element_counter, initial=None):
        self.stack = []
        if initial is not None:
            self.stack = initial

        self.element_counter = element_counter
        self.operation_counter = operation_counter

    def push(self, value):
        if self.element_counter.get_value() <= 0:
            raise RuntimeError(
                "Du kan ikke ta vare på flere elementer på "
                "stakkene enn det fantes originalt."
            )
        self.stack.append(value)
        self.element_counter.decrement()
        self.operation_counter.increment()

    def pop(self):
        if self.element_counter.get_value() >= 2:
            raise RuntimeError(
                "Du kan ikke ha mer enn 2 elementer i minnet " "av gangen."
            )
        self.element_counter.increment()
        self.operation_counter.increment()
        return self.stack.pop()

    def peek(self):
        self.operation_counter.increment()
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

failed = False
first = True

for test in tests:
    counter1 = Counter()
    counter2 = Counter()
    stack1 = Stack(counter1, counter2, initial=test[:])
    stack2, stack3 = Stack(counter1, counter2), Stack(counter1, counter2)

    sort(stack1, stack2, stack3)

    result = []
    counter2.value = float("-inf")
    while not stack1.empty():
        result.append(stack1.pop())

    if not first:
        print("-"*50)

    if result != sorted(test):
        print(f"""
Koden feilet for følgende instans:
Start (stack1, fra topp til bunn): {test[::-1]}

Ditt svar (stack1, fra topp til bunn): {result}
Forventet svar: {sorted(test)}
""")
        failed = True
    elif result != sorted(test):
        result2 = []
        while not stack2.empty():
            result2.append(stack2.pop())

        result3 = []
        while not stack3.empty():
            result3.append(stack3.pop())
        print(f"""
Koden feilet for følgende instans.
---------------
 Starttilstand
---------------

--------
Stack 1:
--------
{chr(10).join(map(str, test[::-1])) or "ingen elementer i stakken"}

--------------
 Sluttilstand
--------------

--------
Stack 1:
--------
{chr(10).join(map(str, result)) or "ingen elementer i stakken"}

--------
Stack 2:
--------
{chr(10).join(map(str, result2)) or "ingen elementer i stakken"}

--------
Stack 3:
--------
{chr(10).join(map(str, result3)) or "ingen elementer i stakken"}
""")
        failed = True
    else:
        print(f"""
Koden brukte {counter1.get_value() - len(result)} operasjoner på sortering av
{test[::-1]}
""")

    first = False

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")