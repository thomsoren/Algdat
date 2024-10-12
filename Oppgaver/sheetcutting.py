#!/usr/bin/python3
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

def sheet_cutting(w, h, p): 
    # make 2d list with 0 as values
    r = [[0] * (h+1) for _ in range(w+1)]
    # iterate width
    for i in range(1, w+1):
        # iterate height and get prices and place them in r
        for j in range(1, h+1):
            r[i][j] = p.get((i, j), 0)
            # iterate half of width and find the highest width
            for k in range(1, i//2 + 1):
                r[i][j] = max(r[i][j], r[k][j] + r[i - k][j])
            # iterate halv of the height and find highest height
            for l in range(1, j//2 + 1):
                r[i][j] = max(r[i][j], r[i][l] + r[i][j - l])
    return r[w][h]

# def sheet_cutting(w, h, p):
#     # If w = 1 and h = 1 then we cant cut it an return the price, base case
#     if (w == 1 and h == 1): 
#         return p[w,h]
#     # Lager 2d liste    
#     r = [[-float('inf') ] * (h+ 1) for _ in range(w + 1)]
#     return sheet_cutting_aux(w, h, p, r)

def sheet_cutting_aux(w, h, p, r):
    if w == 0 or h == 0:
        return 0
    if r[w][h] >= 0:
        return r[w][h]
    q = p.get((w,h),0)
    for i in range(1, w):
        q = max(q, sheet_cutting_aux(i,h,p,r) + sheet_cutting_aux(w-i,h,p,r))
    for j in range(1, h):
        q = max(q, sheet_cutting_aux(w, j, p, r) + sheet_cutting_aux(w, h-j, p, r))
    r[w][h] = q
    return q


# p = [1,4,3,6,8,5,9]
p = {(1, 1): 1, (2, 1): 3, (1, 2): 3, (2, 2): 3}
w = 2 
h = 2

print(sheet_cutting(w,h,p)) # should print 4

# Tester på formatet (p, w, h, solution)
tests = [
    ({(1, 1): 1}, 1, 1, 1),
    ({(1, 1): 1, (2, 1): 3, (1, 2): 3, (2, 2): 3}, 2, 2, 6),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 5}, 2, 2, 5),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 1, (1, 2): 1, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (2, 1): 0, (1, 2): 0, (2, 2): 3}, 2, 2, 4),
    ({(1, 1): 1, (1, 2): 1}, 1, 2, 2),
    ({(1, 1): 1, (2, 1): 3}, 2, 1, 3),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (3, 1): 4, (2, 2): 3, (3, 2): 7},
        3, 2, 8,
    ),
    (
        {(1, 1): 1, (2, 1): 2, (1, 2): 2, (1, 3): 4, (2, 2): 3, (2, 3): 7},
        2, 3, 8,
    ),
    (
        {(1, 1): 1, (2, 1): 3, (3, 1): 3, (4, 1): 7, (5, 1): 3, (6, 1): 8},
        6, 1, 10,
    ),
    (
        {(1, 1): 1, (1, 2): 2, (2, 1): 2, (1, 3): 1, (3, 1): 1, (1, 4): 2,
         (4, 1): 2, (1, 5): 2, (5, 1): 2, (1, 6): 5, (6, 1): 5, (1, 7): 10,
         (7, 1): 10, (1, 8): 10, (8, 1): 10, (2, 2): 5, (2, 3): 5,
         (3, 2): 5, (2, 4): 2, (4, 2): 2, (2, 5): 10, (5, 2): 10,
         (2, 6): 7, (6, 2): 7, (2, 7): 11, (7, 2): 11, (2, 8): 16,
         (8, 2): 16, (3, 3): 1, (3, 4): 1, (4, 3): 1, (3, 5): 1, (5, 3): 1,
         (3, 6): 11, (6, 3): 11, (3, 7): 11, (7, 3): 11, (3, 8): 24,
         (8, 3): 24, (4, 4): 12, (4, 5): 25, (5, 4): 25, (4, 6): 29,
         (6, 4): 29, (4, 7): 25, (7, 4): 25, (4, 8): 9, (8, 4): 9,
         (5, 5): 12, (5, 6): 10, (6, 5): 10, (5, 7): 26, (7, 5): 26,
         (5, 8): 45, (8, 5): 45, (6, 6): 35, (6, 7): 44, (7, 6): 44,
         (6, 8): 50, (8, 6): 50, (7, 7): 1, (7, 8): 41, (8, 7): 41, (8, 8): 5},
        8, 8, 91,
    ),
    (
        {(1, 1): 1, (1, 2): 0, (2, 1): 0, (1, 3): 0, (3, 1): 0, (1, 4): 4,
         (4, 1): 4, (1, 5): 0, (5, 1): 0, (1, 6): 0, (6, 1): 0, (1, 7): 0,
         (7, 1): 0, (1, 8): 1, (8, 1): 1, (1, 9): 3, (9, 1): 3, (1, 10): 0,
         (10, 1): 0, (2, 2): 0, (2, 3): 0, (3, 2): 0, (2, 4): 0, (4, 2): 0,
         (2, 5): 0, (5, 2): 0, (2, 6): 13, (6, 2): 13, (2, 7): 0, (7, 2): 0,
         (2, 8): 0, (8, 2): 0, (2, 9): 0, (9, 2): 0, (2, 10): 0, (10, 2): 0,
         (3, 3): 13, (3, 4): 3, (4, 3): 3, (3, 5): 0, (5, 3): 0, (3, 6): 16,
         (6, 3): 16, (3, 7): 0, (7, 3): 0, (3, 8): 0, (8, 3): 0, (3, 9): 31,
         (9, 3): 31, (3, 10): 0, (10, 3): 0, (4, 4): 0, (4, 5): 0, (5, 4): 0,
         (4, 6): 10, (6, 4): 10, (4, 7): 20, (7, 4): 20, (4, 8): 0, (8, 4): 0,
         (4, 9): 4, (9, 4): 4, (4, 10): 0, (10, 4): 0, (5, 5): 0, (5, 6): 43,
         (6, 5): 43, (5, 7): 0, (7, 5): 0, (5, 8): 0, (8, 5): 0, (5, 9): 0,
         (9, 5): 0, (5, 10): 0, (10, 5): 0, (6, 6): 11, (6, 7): 0, (7, 6): 0,
         (6, 8): 0, (8, 6): 0, (6, 9): 0, (9, 6): 0, (6, 10): 0, (10, 6): 0,
         (7, 7): 0, (7, 8): 0, (8, 7): 0, (7, 9): 50, (9, 7): 50, (7, 10): 0,
         (10, 7): 0, (8, 8): 0, (8, 9): 0, (9, 8): 0, (8, 10): 0, (10, 8): 0,
         (9, 9): 0, (9, 10): 126, (10, 9): 126, (10, 10): 0, (11, 1): 1,
         (1, 11): 1, (11, 2): 0, (2, 11): 0, (11, 3): 0, (3, 11): 0, (11, 4): 0,
         (4, 11): 0, (11, 5): 0, (5, 11): 0, (11, 6): 0, (6, 11): 0, (11, 7): 0,
         (7, 11): 0, (11, 8): 0, (8, 11): 0, (11, 9): 0, (9, 11): 0,
         (11, 10): 0, (10, 11): 0, (12, 1): 0, (1, 12): 0, (12, 2): 0,
         (2, 12): 0, (12, 3): 0, (3, 12): 0, (12, 4): 22, (4, 12): 22,
         (12, 5): 0, (5, 12): 0, (12, 6): 0, (6, 12): 0, (12, 7): 0, (7, 12): 0,
         (12, 8): 0, (8, 12): 0, (12, 9): 48, (9, 12): 48, (12, 10): 0,
         (10, 12): 0, (13, 1): 17, (1, 13): 17, (13, 2): 0, (2, 13): 0,
         (13, 3): 0, (3, 13): 0, (13, 4): 0, (4, 13): 0, (13, 5): 65,
         (5, 13): 65, (13, 6): 30, (6, 13): 30, (13, 7): 0, (7, 13): 0,
         (13, 8): 7, (8, 13): 7, (13, 9): 0, (9, 13): 0, (13, 10): 0,
         (10, 13): 0, (14, 1): 0, (1, 14): 0, (14, 2): 0, (2, 14): 0,
         (14, 3): 0, (3, 14): 0, (14, 4): 3, (4, 14): 3, (14, 5): 0, (5, 14): 0,
         (14, 6): 0, (6, 14): 0, (14, 7): 0, (7, 14): 0, (14, 8): 0, (8, 14): 0,
         (14, 9): 0, (9, 14): 0, (14, 10): 0, (10, 14): 0, (15, 1): 0,
         (1, 15): 0, (15, 2): 0, (2, 15): 0, (15, 3): 0, (3, 15): 0, (15, 4): 0,
         (4, 15): 0, (15, 5): 0, (5, 15): 0, (15, 6): 0, (6, 15): 0, (15, 7): 0,
         (7, 15): 0, (15, 8): 146, (8, 15): 146, (15, 9): 0, (9, 15): 0,
         (15, 10): 0, (10, 15): 0, (16, 1): 0, (1, 16): 0, (16, 2): 0,
         (2, 16): 0, (16, 3): 0, (3, 16): 0, (16, 4): 0, (4, 16): 0, (16, 5): 0,
         (5, 16): 0, (16, 6): 0, (6, 16): 0, (16, 7): 80, (7, 16): 80,
         (16, 8): 0, (8, 16): 0, (16, 9): 43, (9, 16): 43, (16, 10): 0,
         (10, 16): 0, (17, 1): 0, (1, 17): 0, (17, 2): 0, (2, 17): 0,
         (17, 3): 0, (3, 17): 0, (17, 4): 0, (4, 17): 0, (17, 5): 0, (5, 17): 0,
         (17, 6): 82, (6, 17): 82, (17, 7): 0, (7, 17): 0, (17, 8): 83,
         (8, 17): 83, (17, 9): 0, (9, 17): 0, (17, 10): 200, (10, 17): 200,
         (18, 1): 23, (1, 18): 23, (18, 2): 0, (2, 18): 0, (18, 3): 0,
         (3, 18): 0, (18, 4): 0, (4, 18): 0, (18, 5): 0, (5, 18): 0, (18, 6): 0,
         (6, 18): 0, (18, 7): 116, (7, 18): 116, (18, 8): 0, (8, 18): 0,
         (18, 9): 0, (9, 18): 0, (18, 10): 23, (10, 18): 23, (19, 1): 0,
         (1, 19): 0, (19, 2): 0, (2, 19): 0, (19, 3): 66, (3, 19): 66,
         (19, 4): 0, (4, 19): 0, (19, 5): 0, (5, 19): 0, (19, 6): 151,
         (6, 19): 151, (19, 7): 0, (7, 19): 0, (19, 8): 0, (8, 19): 0,
         (19, 9): 0, (9, 19): 0, (19, 10): 0, (10, 19): 0, (20, 1): 0,
         (1, 20): 0, (20, 2): 50, (2, 20): 50, (20, 3): 61, (3, 20): 61,
         (20, 4): 0, (4, 20): 0, (20, 5): 0, (5, 20): 0, (20, 6): 0, (6, 20): 0,
         (20, 7): 0, (7, 20): 0, (20, 8): 0, (8, 20): 0, (20, 9): 0, (9, 20): 0,
         (20, 10): 0, (10, 20): 0},
        20, 10, 283,
    ),
]

failed = False

for prices, w, h, answer in tests:
    student = sheet_cutting(w, h, prices)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True
        print(f"""
Koden feilet for følgende instans:
w: {w}
h: {h}
prices:
{prices}

Ditt svar: {student}
Riktig svar: {answer}
        """)

if use_extra_tests:
    with open("tests_sheet_cutting.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            w, h, price_string, answer = line.strip().split(" | ")
            w, h, answer = int(w), int(h), int(answer)
            prices = {}
            for data_point in price_string.split(","):
                i, j, price = map(int, data_point.split(":"))
                prices[i, j] = price

            extra_tests.append((prices, w, h, answer))

    n_failed = 0
    for prices, w, h, answer in extra_tests:
        student = sheet_cutting(w, h, prices)
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
w: {w}
h: {h}
prices:
{prices}

Ditt svar: {student}
Riktig svar: {answer}
                """)
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
