# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# Author:           wangkun
# Created:          2021/4/18
# Description:      this file contains some classic string processing algorithm
# ------------------------------------------------------------------
from collections import defaultdict

def get_longest_substring(a, b):
    """
    This fuction is used to get the longest substring of two strings
    Args:
        a & b
    Return:
        c: longest substring
    """
    a_len, b_len = len(a), len(b)
    dy_map = [[0 for j in range(b_len + 1)] for i in range(a_len + 1)]
    longest = 0
    for idx, item in enumerate(a):
        for jdx, jtem in enumerate(b):
            if item == jtem:
                dy_map[idx + 1][jdx + 1] = dy_map[idx][jdx] + 1
                longest = max(longest, dy_map[idx + 1][jdx + 1]) 
    return longest


def get_longest_subsequence(a, b):
    """
    This function is used to get the longest subsequency of two strings
    c[i][j] = max(c[i-1][j], c[i][j-1]) if a[i]!=b[j] else c[i-1][j-1] + 1
    remind c[i][j] has one extra dimension
    Args:
        a & b
    Return:
        c: longgest subsequency(not continuos)
    """
    a_len, b_len = len(a), len(b)
    dy_map = [[0 for j in range(b_len + 1)] for i in range(a_len + 1)]
    for idx, item in enumerate(a):
        for jdx, jtem in enumerate(b):
            if item == jtem:
                dy_map[idx + 1][jdx + 1] = dy_map[idx][jdx] + 1
            else:
                dy_map[idx + 1][jdx + 1] = max(dy_map[idx][jdx + 1], dy_map[idx + 1][jdx]) 
    return dy_map[a_len][b_len]


def kmp(txt, pat):
    """
    This fuction is used to find p's position in s by kmp algorithm
    This implement is forked from geeksforgeeks
    Args:
        txt & pat
    Return:
        indexs: a list of postion index
    """
    M = len(pat)
    N = len(txt)
    indexs = []
  
    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            indexs.append(i - j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return indexs


def computeLPSArray(pat, M, lps):
    """
    This fuction is used to get longest prefix suffix
    Args:
        pat: pattern string
        M: pattern length
        lps: longest prefix suffix array
    """
    length = 0 # length of the previous longest prefix suffix
    i = 1
    # lps[0] is always 0 the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def horspool(txt, pat):
    """
    This fuction is used to find p's position in s by Horspool algorithm
    Args:
        txt & pat
    Return:
        first_appear_pos: first match postion index
    """
    table = shift_table(pat)
    index = len(pat) - 1
    while index <= len(txt) - 1:
        match_count = 0
        while match_count < len(pat) and pat[len(pat) - 1- match_count] == txt[index - match_count]:
            match_count += 1
        if match_count == len(pat):
            return index - match_count + 1
        else:
            index += table[txt[index]]


def shift_table(pattern):
    """
    get shift table of pattern
    Args:
        pattern
    Return:
        table: the shift table
    """
    table = defaultdict(lambda: len(pattern))
    for index in range(0, len(pattern) - 1):
        table[pattern[index]] = len(pattern) - 1 - index
    return table


if __name__ == "__main__":
    print(get_longest_subsequence("baaaabbba", "aaba"))
    print(get_longest_substring("baaaabbba", "aaba"))
    print(kmp("baaaabbbaaabbba", "aabbba"))
    print(Horspool("baaaabbbaaabbba", "aabbba"))
    