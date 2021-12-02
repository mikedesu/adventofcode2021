def main():
    inputLines = []
    filename = "input.txt"
    with open(filename,'r') as f:
        inputLines = f.readlines()
    x = 0
    y = 0
    for line in inputLines:
        splitLine = line.split(" ")
        command = splitLine[0]
        units = int(splitLine[1])
        if command == "up":
            y -= units
        elif command == "forward":
            x += units
        elif command == "down":
            y += units
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"x * y = {x * y}")

if __name__=='__main__':
    main()
