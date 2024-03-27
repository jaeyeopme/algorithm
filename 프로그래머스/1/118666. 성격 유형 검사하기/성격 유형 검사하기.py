def solution(survey, choices):
    s_dict = {
        "R" : 0, 
        "T" : 0, 
        "C" : 0, 
        "F" : 0, 
        "J" : 0, 
        "M" : 0, 
        "A" : 0,
        "N" : 0
    }
    
    for i, s in enumerate(survey):
        if choices[i] < 4:
            s_dict[s[0]] += ((choices[i] * -1) + 4)
        elif choices[i] > 4:
            s_dict[s[1]] += (choices[i] - 4)
    
    answer = ""
    
    if s_dict["R"] >= s_dict["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if s_dict["C"] >= s_dict["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if s_dict["J"] >= s_dict["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if s_dict["A"] >= s_dict["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer