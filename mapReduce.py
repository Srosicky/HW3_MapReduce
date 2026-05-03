'''
Date: 4/29/2026
Course: COMP 3351
Authors: Leyna Fougere + Sophia Rosicky
Assignment: Homework 3 - Higher Order Functions
'''

# Permitted: recursion, map(), filter(), reduce() 
# Not Allowed: loops and most built-in functions (len, sort, sum, etc.)



#TODO: wcMap function



#TODO: groupByKey function



#TODO: wcReduce function



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
