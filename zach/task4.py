import os
from cgitb import reset


def read_file():
    nums = []
    r_file = os.path.join('data', "fraction.txt")
    if not os.path.isfile(r_file):
        print("Файл fraction.txt не существует")
        exit()
    with open(r_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            if line[-1] == '\n':
                line = line[0:-1]
            nums.append(line.split('/'))
    return nums

def sum_pr(sum_or_pr, nums):
    res = 0
    if sum_or_pr == 1:
        for el in nums:
            res += int(el[0])/int(el[1])
    else:
        res=1
        for el in nums:
            res *= int(el[0])/int(el[1])
    return res
num = read_file()
print(sum_pr(0, num))