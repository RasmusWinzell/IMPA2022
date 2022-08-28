# 12646 -  Zero or One
# https://onlinejudge.org/external/126/12646.pdf

from sys import stdin
PLAYERS = ['A', 'B', 'C']

def zero_or_one(test_case):
    values = test_case.split(' ')
    for i, value in enumerate(values):
        if values.count(value) == 1:
            print(PLAYERS[i])
            return
    print('*')


for line in stdin:
        test_case = line.strip()
        if test_case:
            zero_or_one(test_case)