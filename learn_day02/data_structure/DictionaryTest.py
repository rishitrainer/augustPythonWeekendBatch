sampleDictionary = {
    "model" : "Ertiga VXI CNG",
    "year" : 2021,
    "make" : "Maruti",
    "BS"    : "BSVI",
    "VIN"   : "JH03 AS1244",
}
print(sampleDictionary)
print(sampleDictionary["model"])
print(sampleDictionary.get("year"))
# Add new element
sampleDictionary["color"] = "Grey"
print(sampleDictionary)
# update
sampleDictionary["year"] = 2020
print(sampleDictionary)

sampleDictionary.popitem()
print(sampleDictionary)
sampleDictionary.pop("VIN")
print(sampleDictionary)

for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))

for key, value in sampleDictionary.items():
    print(key, value)

for eachValue in sampleDictionary.values():
    print(eachValue)


if "make" in sampleDictionary:
    print("make is present")

if "Maruti" in sampleDictionary.values():
    print("Maruti is present")

sampleDictionary.clear()
