# Trying to solve question nested list to flat list from saral 
# recursion. NOt a correct code but kept it as i have doubt as to 
# why on terminal i can use type function but here error is coming

def list_expansion(l):
    expanded_l = []
    length_of_list = len(l)
    if length_of_list == 1 and type(list[0]) == int:
        expanded_l.append(l[0])
    elif length_of_list == 1 and type(list[0]) != int:
        list_expansion(list[0])

    else :
        list_expansion(l[1:])

    return expanded_l

p = [1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]

print(list_expansion(p))
