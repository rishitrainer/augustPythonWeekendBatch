print("Hello World")
'''
while condition:
    block of code will iterate condition is true
    condition modifier
Addition of 1 to 10
'''
count = 1
total = 0
while count <= 10:
    if count == 6:
        print("Exiting with break")
        break
    total = total + count
    print("Count Value", count)
    count = count + 1

print("Total" , total)

