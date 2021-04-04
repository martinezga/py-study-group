'''
Reversed Strings
https://www.codewars.com/kata/5168bb5dfe9a00b126000018

Complete the solution so that it reverses the string passed into it
'''

def solution(string):
    reversed_string = ''
    reversed_iterator = reversed(string)

    for letter in reversed_iterator:
        reversed_string += letter

    return reversed_string

# Other solution:
# def solution(string):
#     reversed_string = ''
#     reversed_iterator = reversed(string)

#     for letter in reversed_iterator:
#         reversed_string += letter

#     return reversed_string


# Solved by Gabriella Martinez. https://github.com/martinezga
