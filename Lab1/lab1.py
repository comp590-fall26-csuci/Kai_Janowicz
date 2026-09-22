def fibit(k,num_list=None):
    if num_list == None:
        num_list = []
    if k <= 0:
        return num_list
    
    length = len(num_list)
    if length == 0:
        num_list.append(0)
        return fibit(k-1,num_list)
    if length == 1:
        num_list.append(1)
        return fibit(k-1, num_list)
    num_list.append(num_list[length - 1] + num_list[length - 2])
    return fibit(k-1, num_list)

    
def outputToFile(x):
    with open("output/fib.txt", "w") as f:
        print(x, file=f)

outputToFile(fibit(25))
