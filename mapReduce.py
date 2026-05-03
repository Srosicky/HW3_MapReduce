'''
Date: 4/29/2026
Course: COMP 3351
Authors: Leyna Fougere + Sophia Rosicky
Assignment: Homework 3 - Higher Order Functions
'''

from functools import reduce


'''
Function: wcMap
Parameters: Text String
Returns: List of Tuples

This function splits the text into individual tokens, pairs each token with a count value, 
then adds the resulting tuple to a comprehensive list which is then returned.
'''
def wcMap(text):
    
    words = text.split()
    return list(map(lambda w: (w, 1), words))



'''
Function: groupByKey
Parameters: List of Tuples
Returns: List of Tuples

Given a list of tuples, this function creates a new list of tuples where all the corresponding
values of like keys are grouped in one tuple.
'''
def groupByKey(pairs):
    grouped = reduce(lambda acc, pair: {**acc, pair[0]: acc.get(pair[0], []) + [pair[1]]}, pairs, {})
    return list(grouped.items())



'''
Function: wcReduce
Parameters: List of Tuples
Returns: List of Tuples

Given a list of tuples, this function take the second value of each and reduces it to reflect the
total count for a given key.
'''
def wcReduce(groups):
    return list(map(lambda group: (group[0], reduce(lambda acc, x: acc + x, group[1])), groups))


#Test Code
text = "this is a test of python\nthis is only a test\ntest of python\n"
m = wcMap(text)
print("mapped:", m)
g = groupByKey(m)
print("grouped:", g)
r = wcReduce(g)
print("reduced:", r)



# Output from test run should look like this....

#mapped: [('this', 1), ('is', 1), ('a', 1), ('test', 1), ('of', 1), ('python', 1), ('this', 1), ('is', 1), ('only', 1), ('a', 1), ('test', 1), ('test', 1), ('of', 1), ('python', 1)]
#grouped: [('this', [1, 1]), ('is', [1, 1]), ('a', [1, 1]), ('test', [1, 1, 1]), ('of', [1, 1]), ('python', [1, 1]), ('only', [1])]
#reduced: [('this', 2), ('is', 2), ('a', 2), ('test', 3), ('of', 2), ('python', 2), ('only', 1)]
