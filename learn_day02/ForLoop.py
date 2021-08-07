'''
Add 1 to 10
for eachValue in Collection:
    block of code for iteration
'''

# range (start, end, step)
for eachLine in range(1,10):
    if eachLine == 6:
        print("Executing continue")
        continue
    print(eachLine)



for eachValue in range(-11,11,3):
     print(eachValue)

data = ['H','e','l', 'l']
sample = "Hello World"
print(sample[0])

for eachValue in sample:
    print(eachValue)
else:
    print("Processing Complete")