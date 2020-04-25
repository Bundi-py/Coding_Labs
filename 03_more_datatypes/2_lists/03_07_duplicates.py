'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

list1 = set(list_)
list2 = list(list1)
print('Initial list:', list_)
print('The list with all duplicates removed:', list2)
