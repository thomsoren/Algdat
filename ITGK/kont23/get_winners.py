import math

def get_winners(user_data, sort_by, letter):
    if sort_by == "quickest":
        quickest = ""
        highscore = float('inf')
    elif sort_by == "most":
        high_tries = 0
        tried_most = ""

    for key, value in user_data.items():
        letter_values = letter_value(value, letter)
        high_tries_person = -1
        for value in letter_values:
            if sort_by == "quickest" and value < highscore:
                highscore = value
                quickest = key
            elif sort_by == "most":
                high_tries_person +=1
        if high_tries_person > high_tries:
            high_tries = high_tries_person
            tried_most = key
        elif high_tries_person == high_tries:



    if sort_by = "quickest":
        return f"Raskest for {letter} er {tried_most},"


        
    
