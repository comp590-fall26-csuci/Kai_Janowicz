def fibit(k):
    if k == 0:
        outputToFile([])
        return
    if k == 1:
        outputToFile([0])
        return
    if k == 2: 
        outputToFile([0,1])
    out_list = [0,1,1]
    x = 1 
    y = 1
    while len(out_list) < k:
        tempy = x 
        x = x + y
        y = tempy
        out_list.append(x)
    outputToFile(out_list)
    return
def outputToFile(x):
    with open("output/fib.txt", "w") as f:
        print(x, file=f)

fibit(25)
