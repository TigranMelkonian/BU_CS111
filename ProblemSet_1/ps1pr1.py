#
# ps1pr1.py - Problem Set 1, Problem 1
#
# Indexing and slicing puzzles


#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]

# Creating the list [2, 7]  from pi and e
answer1 = e[0:2]
# Creating the list [5, 4, 3] from pi and e
answer2 = pi[-2::-2]
# Creating the list  [3, 5, 7] from pi and e
answer3 = [pi[0]] + [pi[4]] + [e[1]]
# Creating the list [1, 2, 3, 4, 5] from pi and e
answer4 = [e[2]] + [e[0]] + [pi[0]] + [pi[2]] + [pi[4]]

print(answer0)
print(answer1)
print(answer2)
print(answer3)
print(answer4)


#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

# Creating the string 'universe'
answer6 = u[0:7] + u[4]

# Creating the string 'roster'
answer7 = t[2] + b[1:3] + t[0:3]

# Creating the string 'biosterous'
answer8 = b[0] + t[4] + b[1:3] + t[0:3] + b[1] + u[0::6]

# Creating the string 'yesyesyes'
answer9 = (u[-1::-5] + t[-1])*3

# Creating the string 'trist'
answer10 = b[3] + t[3:5] + b[2:4]

print(answer5)
print(answer6)
print(answer7)
print(answer8)
print(answer9)
print(answer10)
print()
