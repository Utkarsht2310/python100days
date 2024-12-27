def cube(x):
    return x*x*x

l = [1,2,3,4,5,6,7,8]
#now if we want to create a list which contains cube of each elelemt "l" has:-
# newl = []
# for i in l:
#     newl.append(cube(i))
#
# print(newl)

#Doing with Map function:- map function use if you want to apply any function on  each sequence or element.
# newl = list(map(cube,l))
# print(newl)
#
# # Fileter() :- it takes two arguments, first a function which returns boolean value and second the iterable.
# def filter_function(a):
#     return a>3
# newl = list(filter(filter_function,l))
# print(newl) # prints values only greater than 3.

# Reduce function:- it applies function onn first two elements tan the result and the other element till last element.

# from functools import reduce
# num = [1,2,3,4,5]
#
# #calculate the sum of elements using reduce:-
# def mysum(x,y):
#     return x+y
#
# sum = reduce(mysum,num)
# print(sum)

