line1 = 20
line2 = 8
line3 = 4

if (line1 + line2 > line3) and (line1 + line3 > line2) and (line2+line3 > line1):
    print("You can form a Triangle")
else:
    print("You cannot for a Triangle")

'''
Truth table of and
S1  S2  S1 & S2
T   T   T
T   F   F
F   T   F
F   F   F
F = 0
& *
'''


'''
Truth table of OR
S1  S2  S1 | S2
T   T   T
T   F   T
F   T   T
F   F   F
F = 0
| +
'''
print(True or True)
print(True or False)
print(False or True)
print(False or False)

'''
negation not
'''
print("not True" , not True)
print("not False" , not False)