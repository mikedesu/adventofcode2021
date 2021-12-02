def main():
    inputLines = []
    filename = "input.txt"
    with open(filename,'r') as f:
        inputLines = f.readlines()
    x = 0
    y = 0
    aim = 0
    for line in inputLines:
        splitLine = line.split(" ")
        command = splitLine[0]
        units = int(splitLine[1])
        if command == "up":
            aim -= units
        elif command == "forward":
            x += units
            y += ( aim * units )
        elif command == "down":
            aim += units
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"x * y = {x * y}")

if __name__=='__main__':
    main()
