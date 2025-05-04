import string
mystring = 'oi tudo bem'

# My solution:

# new = mystring.split()


# def upper_first_letter(word):
#     return word[0].upper()+word[1:]


# result = upper_first_letter(new[0])

# for i in new[1:]:
#     result += " " + upper_first_letter(i)


# print(result)

# HackerRank solution:
s = mystring
for x in s.split():
    s = s.replace(x, x.capitalize())
print(s)

# OR
a_string = mystring.split(' ')
print(' '.join((word.capitalize() for word in a_string)))

# In the first line a string is transformed to a mutable list
# split() with a specified separator doesn't group consecutive whitespaces (please kindly refer to split() doc)

# OR
#import string
print(string.capwords(mystring, ' '))
