h = "hei jeg er en robot"
print(h)

brett = [[0,0,0],[0,0,0],[0,0,0]]



while True:
    svar = input("skriv et tall fra 1-9, 'q' stopper\n")
    if svar == "q":
        break
    elif svar == "1":
        brett[0][0] = 1
    elif svar == "2":
        brett[0][1] = 1
    elif svar == "3":
        brett[0][2] = 1
    elif svar == "4":
        brett[1][0] = 1
    elif svar == "5":
        brett[1][1] = 1
    elif svar == "6":
        brett[1][2] = 1
    elif svar == "7":
        brett[2][0] = 1
    elif svar == "8":
        brett[2][1] = 1
    elif svar == "9":
        brett[2][2] = 1
    for row in brett:
        strRow = ""
        for num in row:    
            strRow += str(num) + " "
        print(strRow)
    