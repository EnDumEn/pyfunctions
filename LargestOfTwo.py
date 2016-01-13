"""
Silly way to pick out the largest of two numbers

Input example
5465 456456
12312 6546
8798 65465
132 98789

Output
456456, 12312, 65465, 98789
"""

listA = []
listB = []

num_lines = sum(1 for line in open("text.txt"))

answer = []

for line in open("text.txt"):
    line = line.split()
    listA.append(line[0])
    listB.append(line[1])

for i in range(1,num_lines):
    if listA[i] > listB[i]:
        answer.append(listA[i])
    else:
        answer.append(listB[i])

print answer
