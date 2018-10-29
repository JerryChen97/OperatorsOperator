# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:51:04 2018

@author: chenyushao
"""

from collections import Counter



"""
Here we use simply one string to be replaced and one list for all the terms to replace
"""
oldString = 'px'
newStrings = ['xp','']

"""
A function for flattening the nested lists
"""
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

"""
Calculate any single string, and return a list for new ones
"""
def operatorCalculate(operatorString):
    
    """
    find the position of the first substring required to be replaced
    """
    firstEncounterIndex = operatorString.find('px')
    
    if firstEncounterIndex == -1:
        return operatorString
    
    newOperatorStringList = []
    for string in newStrings:
        newString = operatorString[0:firstEncounterIndex] + string + operatorString[firstEncounterIndex+2:]
        newOperatorStringList.append(newString)
    
    return newOperatorStringList

"""

"""
def operatorCalculateRecursively(operatorString):
    """
    The terminating condition for the recursion
    """
    if operatorString.find('px') == -1:
        return operatorString
    
    newOperatorList = operatorCalculate(operatorString)
    newOperator1 = newOperatorList[0]
    newOperator2 = newOperatorList[1]
    result = [operatorCalculateRecursively(newOperator1), operatorCalculateRecursively(newOperator2)]
    result = flatten(result)
    
    return result

def test():
    """ Some primary testing codes
    term1 = Term({'a':1})
    term2 = Term({'a':2,'n':1})
    term1.add(term2).output()
    """
    testString = 'ppxx'
    output = operatorCalculateRecursively(testString)
    output = dict(Counter(output))
    print('The expansion of '+testString + ' is')
    print(output)
    pass

test()
            
    