# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# Author:           wangkun
# Created:          2021/4/18
# Description:      this file contains edit distance algorithm
# ------------------------------------------------------------------

def levenshtein_distance(a, b):
    """
    Calculate edit distance between two strings
    edit distance means the minmum step to change a to b
    Args:
        a & b ->str
    Return:
        dis -> int: distance 
    """
    a_len, b_len = len(a), len(b)
    if a_len * b_len == 0:
        return a_len + b_len
    dy_map = [[0 for j in range(b_len + 1)] for i in range(a_len + 1)]
    for i in range(a_len + 1):
        dy_map[i][0] = i
    for j in range(b_len + 1):
        dy_map[0][j] = j
    for idx, item in enumerate(a):
        for jdx, jtem in enumerate(b):
            left = dy_map[idx][jdx + 1] + 1
            top = dy_map[idx + 1][jdx] + 1
            if item == jtem:
                left_top = dy_map[idx][jdx]
            else:
                left_top = dy_map[idx][jdx] + 1
            dy_map[idx + 1][jdx + 1] = min(left, top, left_top)
    return dy_map[a_len][b_len]


if __name__ == "__main__":
    print(levenshtein_distance("sikking", "kitting"))

