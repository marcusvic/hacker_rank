hospitals = ['Hospital A', 'Hospital B', 'Hospital C']
students = ['Student P', 'Student Q', 'Student R']
hospital_preferences = {
    'Hospital A': ['Student P', 'Student R', 'Student Q'],
    'Hospital B': ['Student P', 'Student Q', 'Student R'],  
    'Hospital C': ['Student P', 'Student R', 'Student Q']
}

student_preferences = {
    'Student P': ['Hospital B', 'Hospital C', 'Hospital A'],
    'Student Q': ['Hospital C', 'Hospital B', 'Hospital A'],
    'Student R': ['Hospital C', 'Hospital A', 'Hospital B']
}

# while a hospital h still has an offer:
    # set student k to hospital's top preference
        # if k prefers h than its current offer, k rejects it's current offer, and a match is made
        # else, k rejects h's offer, no match is made.
    # cross k from h's list

matches = {
    'Hospital A':"",
    'Hospital B':"",
    'Hospital C':"",
}

def is_free_places(matches: dict) -> bool:
    """true if there are still free places"""
    for each in matches:
        if matches[each] == "":
            return True
    return False

def hospital_in_match(student:str, matches:dict) -> str:
    """returns the hospital currently matched by a student"""
    for key, val in matches.items():
        if val == student:
            return key
    return None

def prefers_offer(h_offer: str, student: str, matches) -> bool:
    """Returns true if student prefers this offer"""
    offer_index = student_preferences[student].index(h_offer)
    current_index = student_preferences[student].index(hospital_in_match(student,matches))
    if offer_index < current_index:
        print (f"{student} prefers offer from {h_offer}")
        return True
    return False


while is_free_places(matches):
    for hospital in hospitals:
        if matches[hospital] != "":
            print (f"{hospital} already has a match: {matches[hospital]}")
            pass
        else:
            student = hospital_preferences[hospital][0]
            if student not in matches.values() or prefers_offer(hospital, student, matches): #if the student still doesn't have an offer or prefers the current offer:
                if hospital_in_match(student,matches) is not None:
                    matches[hospital_in_match(student,matches)] = ""
                matches[hospital] = student
                print (f"matched {student} to {hospital}")
        hospital_preferences[hospital].pop(0)
    #break 

print (matches)