

summations = {}
inputList = []
count = 0
slidingWindow = []
nextWindowIndex = 0
filename="input.txt"

with open(filename, "r") as f:
    inputList = f.readlines()


def updateSlidingWindow(i):
    print(f"updateSlidingWindow: {i}")
    global slidingWindow
    global nextWindowIndex 
    global alphabet 
    global inputList
    if len(slidingWindow) == 0:
        slidingWindow.append( nextWindowIndex  )
        nextWindowIndex += 1
    elif len(slidingWindow) == 1:
        slidingWindow.append( nextWindowIndex  )
        nextWindowIndex += 1
    elif len(slidingWindow) == 2:
        if i < len(inputList)-2:
            print('rotating...')
            slidingWindow.append( nextWindowIndex  )
            nextWindowIndex += 1
        else:
            print('popping 1...')
            slidingWindow.pop( 0 )

    elif len(slidingWindow) == 3:
        if i < len(inputList)-2:
            print('rotating...')
            slidingWindow.pop( 0 )
            slidingWindow.append( nextWindowIndex  )
            nextWindowIndex += 1
        elif i == len(inputList)-2:
            print('popping 2...')
            slidingWindow.pop( 0 )


for i in range(len(inputList)):
    a = inputList[ i ]
    a = int(a[ 0 : len(a) - 1 ])
    updateSlidingWindow(i)
    for window in slidingWindow:
        v = summations.setdefault( window, 0 )
        v += a 
        summations[ window ] = v

index = 0
prevNum = -1
increases = 0
for k in summations:
    sum_k = summations[k]
    print(f"{sum_k}")
    if index == 0:
        prevNum = sum_k
    else:
        if sum_k > prevNum:
            increases += 1
        prevNum = sum_k
    index += 1

print(f"{increases}")
