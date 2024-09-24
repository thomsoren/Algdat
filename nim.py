import random
def take_pieces(n_pieces):
   
    for i in range(1,8):
        # returner antall fyrstikker som må fjernes får å få motstanderen i< tapende posisjon
        if (n_pieces - i) % 8 == 1:
            return i
   
    return random.randint(1, 7)

print(take_pieces(5))
print(take_pieces(32))
