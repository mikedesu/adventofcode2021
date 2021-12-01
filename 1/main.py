inputList = []
count = 0
with open("input.txt", "r") as f:
    inputList = f.readlines()
for i in range(1,len(inputList)):
    if int(inputList[i]) > int(inputList[i-1]):
        count += 1
print(count)
