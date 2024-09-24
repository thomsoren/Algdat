
def solution(forth):
    visited = []
    x = 0
    y = 0

    # registrer noder tatt
    for letter in forth:
        if letter == "N": # når north
            y += 1  
        elif letter == "E": #når east
            x += 1   
        else: #når west
            x -= 1
        visited.append([x,y])   

    start = [x, y]

    # finner korteste rute
    path = ""
    while y != 0:
        if y > 0:
            if [x,y - 1] not in visited:
                y -= 1
                path += "S"
            elif [x-1,y] not in visited and [x-1,y-1] not in visited:
                x -= 1
                path += "W"
            else: 
                x += 1
                path += "E"
            visited.append([x,y]) 
    
    while x != 0:
        if x > 0:
            x -= 1
            path += "W"
        else:
            x += 1
            path += "E"
        visited.append([x,y])   

    print(path)
    # vi skal til 0,0, nå er vi i 2,2
    return path

solution("NNENWN")

solution("NWNENWNEN")

solution("NENENWWWWN")