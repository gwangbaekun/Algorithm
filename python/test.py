import sys

# sys.stdin = open("python.txt", "r")

num_alpha = sys.stdin.readline().strip()

count = 2 * len(num_alpha)

for i in num_alpha:
    if i == "A" or i == "B" or i == "C":
        count += 1
    elif i == "D" or i == "E" or i == "F":
        count += 2
    elif i == "G" or i == "H" or i == "I":
        count += 3
    elif i == "J" or i == "K" or i == "L":
        count += 4
    elif i == "M" or i == "N" or i == "O":
        count += 5
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        count += 6
    elif i == "T" or i == "U" or i == "V":
        count += 7
    else:
        count += 8
    
  
print(count)

# import sys
# num_alphabet = sys.stdin.readline()
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# count = 0
# for j in range(len(num_alphabet)):
#     for i in dial:
#         if num_alphabet[j] in i:
#             count += dial.index(i)+3

# print(count)