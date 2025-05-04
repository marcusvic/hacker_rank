# # As per Hacker Rank's problem: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

# def merge_the_tools(string, k):
#     n = len(string)
#     substrings = []
#     counter = 0
#     # for each substring in the n/k substrings:
#     for substring in range(n//k):
#         substrings.append(string[(counter*k):((substring+1)*k)])
#         counter += 1
#     final_list = []
#     for substring in substrings:
#         finalstring = ""
#         for letter in substring:
#             if letter not in finalstring:
#                 finalstring += letter
#         final_list.append(finalstring)

#     print(*final_list, sep="\n")

# hacker rank solution:
import textwrap


def merge_the_tools(string, k):
    wrapper = textwrap.TextWrapper(width=k)
    word_list = wrapper.wrap(text=string)
    for x in word_list:
        # for each word in the word, build a dictionary and print the keys together
        print("".join(dict.fromkeys(x)))


if __name__ == '__main__':
    string, k = "AABCADWHS", int(3)
    merge_the_tools(string, k)
