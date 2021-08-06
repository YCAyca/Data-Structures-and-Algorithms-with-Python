"""
checkIfDuplicates : the function to check if base set containes duplicate elements
 
best_match : during adding the subsets to Col, if the subset sum is bigger than best_match and 
             smaller than target, we take this subset as the best_subset_added until now.
             When we come to the end of algorithm, its enough to return this "best_subset_added" subset
             as the result
 
"""
def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def subset_sum(s, target):
    if checkIfDuplicates(s):
        raise ValueError('The list contains duplicates please use set')
    if len(s) == 0 :
        raise ValueError('The set is empty, subset cant be calculated') 
    elif len(s) == 1 and sum(s) > target:
        raise ValueError('Being 1 value list, its element is higher than target, subset cant be calculated')     
    if target >= sum(s) : # no need to calculate, we return the whole set directly
        return s    
   
    best_match = 0
    Col = {tuple()}
    for x in s:
        for L in Col.copy(): 
            if L == ():
                subset_sum = x
            else:
                subset_sum = sum(L) + x
            if  subset_sum == target:
                return L + tuple({x})
            if subset_sum < target :
                if L == ():
                    Col.add(tuple({x}))
                    if subset_sum > best_match:
                        best_match = subset_sum
                        best_subset_added = tuple({x})
                else:    
                    Col.add(L + tuple({x}))
                    if subset_sum > best_match:
                        best_match = subset_sum
                        best_subset_added = L + tuple({x})
    return best_subset_added       






    




     
    