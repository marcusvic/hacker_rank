# as per the challenge at https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

from collections import Counter


def minion_game(s: str):
    vowels = "AEIOU"
    s = s.upper()

    def gets_substrings(string):
        """given a string, returns all substrings in a generator"""
        gen = ((
            string[pos_init:x]
            for x in range(pos_init+1, len(string)+1)
        )
            for pos_init in range(len(string)))

        for it in gen:
            for element in it:
                yield element

    def count_substring(string, substring, counter):
        for position in range(len(string)):
            if string[position:position+len(substring)] == substring:
                counter[substring] += 1

    kevin = Counter()
    stuart = Counter()

    seen = set()
    for substring in gets_substrings(s):
        if substring not in seen:
            if substring[0] in vowels:
                count_substring(substring=substring,
                                string=s, counter=kevin)
            else:
                count_substring(substring=substring,
                                string=s, counter=stuart)
        seen.add(substring)

    if kevin.total() > stuart.total():
        print(f"Kevin {kevin.total()}")
    elif stuart.total() > kevin.total():
        print(f"Stuart {stuart.total()}")
    else:
        print("Draw")


my_string = "banana"
minion_game(my_string)

# I could solve it, but could not solve it with O(N), one-pass.
# Racker Hank's test cases were great because they tested for performance, for example with a 10k long string consisting only of "V"s
# I didn't succeed in these cases.
# Some solutions at hacker rank:


def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

# or:


def minion_game(string):
    s = "AEIOU"
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if s.find(string[i]) != -1:
            Kevin = len(string[i:])+Kevin
        else:
            Stuart = len(string[i:])+Stuart
    if Kevin > Stuart:
        print("Kevin", Kevin)
    elif Kevin < Stuart:
        print("Stuart", Stuart)
    else:
        print("Draw")
