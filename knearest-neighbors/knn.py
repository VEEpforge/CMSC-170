import csv
import math

#data structure: LIST
dataset = []
inputs = []
k = 5

#csv file reading; all data converted to float
def loadDataset():
    with open('data/diabetes.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        
        for row in csv_reader:
            data = []
            for i in row:
                data.append(i)
            
            #last col is for the storage of the computed distance (varies depends on the input)
            data.append(0.0)
            dataset.append(data)

#file reader for the inputs
def loadInput():
    input_reader = open('data/input.in', 'r')

    for row in input_reader:
        row = row.strip().split(",")
        
        data = []
        for i in row:
            data.append(float(i))

        inputs.append(data)

    input_reader.close()

#compute the Euclidean distance
def computeEdistance(index):
    for i in range(len(dataset)):
        distance = 0.0
        for j in range(len(inputs[index])):
            #summation
            distance = distance + ((dataset[i][j] - inputs[index][j])**2)
        #answer is truncated to 4 decimal places
        distance = round(math.sqrt(distance),4)
        dataset[i][-1] = distance   #answers store in the last col of dataset

#find the KNN classes
def findKNNclass():
    #for changing purpose
    maX = max(row[-1] for row in dataset)
    knn_class = [0,0]   #index[0] for 0 counter; index[1] for 1 counter

    for i in range(k):
        #find the index of the min value to access the class
        min_pos = [row[-1] for row in dataset].index(min(row[-1] for row in dataset))
        #update knn_class counter
        if (dataset[min_pos][-2] == 0.0): knn_class[0] += 1
        else: knn_class[1] += 1
        
        #change min value to max value to access the next min number
        dataset[min_pos][-1] = maX
    #returns the index since class is only 0 and 1
    return knn_class.index(max(knn_class))

def classifyInput():
    for i in range(len(inputs)):
        computeEdistance(i)
        claSS_ = findKNNclass()
        if claSS_ == 0 : inputs[i].append('Non-diabetic')
        else : inputs[i].append('Diabetic')

def fileOutput():
    fileWriter = open('output.txt', 'w')

    for row in inputs:
        for i in row:
            if i == row[-1]: fileWriter.write(i + "\n")
            else: fileWriter.write(str(i) + ",")
    
    fileWriter.close()

loadInput()
loadDataset()
classifyInput()
fileOutput()