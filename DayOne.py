file_path = "C:/Users/BT_4N2_18/PycharmProjects/adventDayOne/input.txt"

with open(file_path, "r") as f:
    content = f.read()
array = []
index = 0
partialArray = ""
for i in content:
    if i != " ":
        partialArray += i
        if len(partialArray) == 5:
            array += partialArray

    else:
        partialArray = []


for i in array:
    print(i)
    print(' ')