# from decimal import Decimal
# import math

#initial
r = 0   
t = 0
b = 0
mat = []
weights = []
a = []
y = []
z = []

def loadInput():
    global r, t, b

    fileReader = open("input.txt", "r")
    r = float(fileReader.readline().strip())
    t = float(fileReader.readline().strip())
    b = float(fileReader.readline().strip())

    line = []
    for line in fileReader:
        line = line.strip().split(" ")
        line = [float(i) for i in line]
        
        z.append(line[len(line)-1])
        line[len(line)-1] = b
        mat.append(line)
    fileReader.close()

def computeWeights():
    global weights
    row, col = (len(weights), len(weights[0]))
    # # print(weights)
    # a_cmltv = 0.0

    for i in range(row):
        for j in range(col):
            if i != 0 :
                weights[i][j] = round(weights[i-1][j] + (r * mat[i-1][j] * (z[i-1] - y[i-1])),4)
                
        if i != (row-1):
            a_cmltv = 0.0
            for k in range(col):
                a_cmltv = a_cmltv + (mat[i][k] * weights[i][k])
            a_cmltv = round(a_cmltv,4)
        
        if i != (row-1):
            a.append(a_cmltv)
            if a_cmltv >= t: y.append(1.0)
            else: y.append(0.0)
    # printTable()

def printTable():
    row, col = (len(weights)-1, len(weights[0]))

    for i in range(row):
        for k in range(len(mat[0])):
            print(float(mat[i][k]), end=" ")
        for j in range(col):
            print(float(weights[i][j]), end=" ")
        print(a[i], end=" ")
        print(y[i], end=" ")
        print(z[i], end=" ")
        print("\n")
    
    print(weights[len(weights)-1])

def initialWeights():
    global weights, a, z
    row, col = (len(weights), len(weights[0]))
    # weights = [[0]*col for _ in range (row-1)]
    # weights[0] = weights[row-1]
    for i in range(col):
        weights[0][i] = weights[row-1][i]
    
    for i in range(1,row):
        for j in range(col):
            weights[i][j] = 0.0
    
    a.clear()
    y.clear()

def isWeightConverge():
    row, col = (len(weights), len(weights[0]))

    trueBa = True
    for i in range(col):
        for j in range(1,row-1):
            if weights[j][i] != weights[row-1][i] : trueBa = False
    
    return trueBa

def writeOutput(count):
    if count == 1 : fileWriter = open("output.txt", "w")
    else : fileWriter = open("output.txt", "a")
    
    row, col = (len(weights)-1, len(weights[0]))

    fileWriter.write("Iteration " + str(count) + ":\n")

    for i in range(col-1):
        fileWriter.write("\t" + "x" + str(i))
    fileWriter.write("\t" + "b")
    for i in range(col-1):
        fileWriter.write("\t" + " w" + str(i))
    fileWriter.write("\t" + " wb")
    fileWriter.write("\t" + " a")
    fileWriter.write("\t" + "y")
    fileWriter.write("\t" + "z")
    fileWriter.write("\n")

    for i in range(row):
        for k in range(len(mat[0])):
            fileWriter.write("\t" + str(int(mat[i][k])))
        for j in range(col):
            fileWriter.write("\t" + str(float(weights[i][j])))
        fileWriter.write("\t" + str(a[i]))
        fileWriter.write("\t" + str(int(y[i])))
        fileWriter.write("\t" + str(int(z[i])))
        fileWriter.write("\n")

def writeNonConverging():
    fileWriter = open("output.txt", "w")
    fileWriter.write("Non Converging")

loadInput()
#initialize all weights to 0
row, col = (len(mat)+1, len(mat[0]))
weights = [[0]*col for _ in range (row)]


count = 1
while True :
    # print("Iteration ", count)
    computeWeights()
    writeOutput(count)
    
    trueBa = isWeightConverge()
    if (trueBa == False and count > 50):
        writeNonConverging()
        break
    elif (trueBa == False) : initialWeights()
    else : break
    count += 1