'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def words():
    strng = input('Enter a sentence: ')
    print(f'"{strng}" entered.')
    LongestWordLength(strng)
    return strng


def LongestWordLength(strng2):
    n = len(strng2)
    res = 0
    curr_len = 0

    for i in range(0, n):
        if (str[i] != ' '):
            curr_len += 1
        else:
            res = max(res, curr_len)
            curr_len = 0
    print(max(res, curr_len))
    return max(res, curr_len)


words()
