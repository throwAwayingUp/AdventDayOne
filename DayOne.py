file_path = "C:/Users/BT_4N2_18/PycharmProjects/adventDayOne/input.txt"

with open(file_path, "r") as f:
    content = f.read()
array = []
partArray = ""
indexTwo = 0
for i in content:
    if i != " " and i != "\n":
        if indexTwo == 5:
            array.append(partArray)
            partArray = ""
            indexTwo = 0
        partArray += i
        indexTwo += 1

for i in range(0, len(array)):
    array[i] = int(array[i])

array1 = []
array2 = []

for i in range(0, len(array)):
    if i % 2 == 0:
        array2.append(array[i])
    else:
        array1.append(array[i])

oneLow = array1[0]
indexOneLow = 0
twoLow = array2[0]
indexTwoLow = 0
diffrence = 0
for j in range(0, len(array)):
    for i in range(0, len(array1)):
        if oneLow > array1[i]:
            oneLow = array1[i]
            indexOneLow = i
    array1[indexOneLow] = 99999999999999999
    for b in range(0, len(array2)):
        if twoLow > array2[b]:
            twoLow = array2[b]
            indexTwoLow = b
    array2[indexTwoLow] = 99999999999999999
    diffrence += abs(oneLow - twoLow)
    oneLow = array1[0]
    indexOneLow = 0
    twoLow = array2[0]
    indexTwoLow = 0


print(diffrence)