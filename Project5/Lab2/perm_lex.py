#Lab 2
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

#Input a string of 'n' characters and then recursively generate all permutations
#str --> list of all permutations
def perm_lex(str):    

    if len(str) == 0:
       return([])
    
    if len(str) == 1:
       return([str])
     
    else:
       permutation_list = []
       for i in range(len(str)): 
           new_permutation = perm_lex(str[:i] + str[i+1:])
           for x in new_permutation:
               permutation_list.append(str[i] + x)
    return permutation_list
