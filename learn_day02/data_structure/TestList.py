# Lists are written with square brackets.
sampleList = ["apple", "grapes", "bananas",]
# Access Items: sampleList[1]
print(sampleList)
print(sampleList[1])
# Add Element: sampleList.append("newItem")
sampleList.append("strawberry")
sampleList.append("strawberry")
print(sampleList)
# Sorting: sampleList.sort()
sampleList.sort()
print("Sorting" , sampleList)

# Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1, "blueberry")
print(sampleList)
# Remove Element: sampleList.remove("item")
sampleList.remove("grapes")
print(sampleList)
# Remove Indexed Element: sampleList.pop(1)
sampleList.pop(4)
print(sampleList)
# Using Delete function: del sampleList[0]
del sampleList[0]
print(sampleList)
#Check the Length: len(sampleList)
print(len(sampleList))

for eachValue in sampleList:
    print(eachValue)

if "bananas" in sampleList:
    print("bananas present")

#Clear List: sampleList.clear()
sampleList.clear()
print(sampleList)
# Clear List: sampleList.clear()
del sampleList
#print(sampleList)


data = [1,2,3,4,5,6,7,8,9,10]
sublist = data[::-1]
print(sublist)
