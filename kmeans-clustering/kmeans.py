from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import csv
import random
import math
from decimal import *
import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

label = []
dataset = []
centroid = []
clusters = []
k = 2
x_index = 0
y_index = 0
figure = plt.Figure()
scpfgr = 0


def loadDataset():
    with open('data/Wine.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        count = 0
        for row in csv_reader:
            # if count == 50 : break
            data = []
            for i in row:
                if count == 0 : label.append(i)
                else : data.append(float(i))
            if count != 0 : dataset.append(data)
            count += 1
    print(label)

def collectData():
    global x_index, y_index, k, clusters
    clusters.clear()
    centroid.clear()
    
    valid = True
    attribute_1 = attr_1.get()
    attribute_2 = attr_2.get()
    k = int(n_sb.get())
    
    if attribute_1 == attribute_2 :
        showerror(
            title='Error',
            message=f'Attribute 1 and Attribute 2 should not be the same.'
        )
        valid = False
    
    if valid :
        x_index = label.index(attribute_1)
        y_index = label.index(attribute_2)
        kmeansClusterring()
    
def kmeansClusterring():
    randomCentroid()
    clusterPoints()
    # printCluster()

    while True:
        adjustCentroid()
        # print(centroid)
        clusterPoints()
        # printCluster()
        if centroidNoChange():
            updateTextBox()
            drawScatterPlot()
            fileOutput()
            break
        
    # print(centroid[-1][1][0])

def randomCentroid():
    global centroid
    centroid.clear()

    indeces = random.sample(range(0,len(dataset)),k)

    cntrd = []
    for i in indeces:
        xy = []
        xy.append(dataset[i][x_index])
        xy.append(dataset[i][y_index])
        cntrd.append(xy)
    centroid.append(cntrd)
    # print(centroid)

def clusterPoints():
    global clusters
    clusters.clear()
    #compute distance for each centroid
    for d in range(len(dataset)):
        for c in range(k): #used index for clustering
            distance = 0.0
            distance = distance + ((dataset[d][x_index] - centroid[-1][c][0])**2)
            distance = distance + ((dataset[d][y_index] - centroid[-1][c][1])**2)
            if distance > 0.0 : distance = round(math.sqrt(distance),4)
            
            if c == 0 : clusters.append([distance,c])
            else :
                # if distance == 0.0 :
                #     clusters[d][0] = distance
                #     clusters[d][1] = c
                
                if clusters[d][0] > distance :
                    clusters[d][0] = distance
                    clusters[d][1] = c
                else : pass
        # print(str(clusters[d][0]) + " : " + str(clusters[d][1]))

def printCluster():
    for c in range(k):  #for c in range(len(centroids))
        print("Cluster " + str(c))
        for i in range(len(clusters)):
            if clusters[i][1] == c:
                print("[" + str(dataset[i][x_index]) + " , " + str(dataset[i][y_index]) + "]")

def adjustCentroid():
    new_centroids = []

    for c in range(k):
        x = Decimal('0.0')
        y = Decimal('0.0')
        count = 0

        for i in range(len(clusters)):
            if clusters[i][1] == c:
                x = x + Decimal(str(dataset[i][x_index]))
                y = y + Decimal(str(dataset[i][y_index]))
                count = count + 1
        
        #DIVISION BY ZERO error
        x_ = float(Decimal(str(x)) / Decimal(str(count)))
        y_ = float(Decimal(str(y)) / Decimal(str(count)))

        new_centroids.append([x_,y_])
    centroid.append(new_centroids)

def centroidNoChange():
    trueBa = True

    for c in range(k):
        if collections.Counter(centroid[-1][c]) != collections.Counter(centroid[-2][c]) :
            trueBa = False
            break
    
    return trueBa

def updateTextBox():
    text_box.configure(state='normal')
    text_box.delete('1.0', END)

    for c in range(k):  #for c in range(len(centroids))
        text_box.insert(END, "Centroid " + str(c) + ": ( " + str(centroid[-1][c][0]) + "," + str(centroid[-1][c][1]) + " )\n")
        for i in range(len(clusters)):
            if clusters[i][1] == c:
                text_box.insert(END, "\t[ " + str(dataset[i][x_index]) + "\t" + str(dataset[i][y_index]) + " ]\n")
    
    text_box.configure(state='disabled')

def drawScatterPlot():
    global scpfgr, figure
    # colors=["red","blue","yellow","green","violet","orange","pink","purple","cyan","magenta"]
    # colors = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]

    figure = plt.Figure(figsize=(4.5,4.3), dpi=100)
    scp = figure.add_subplot(111)

    for c in range(k):
        x = []
        y = []
        for i in range(len(clusters)):
            if clusters[i][1] == c:
                x.append(dataset[i][x_index])
                y.append(dataset[i][y_index])    
        scp.scatter(x,y,cmap='paired')
    scp.set_xlabel(label[x_index])
    scp.set_ylabel(label[y_index])
    scpfgr = FigureCanvasTkAgg(figure, window)
    scpfgr.get_tk_widget().place(x=520,y=50)

def resetCommand():
    global clusters, centroid, scpfgr
    clusters.clear()
    centroid.clear()

    text_box.configure(state='normal')
    text_box.delete('1.0', END)
    text_box.configure(state='disabled')
    attr_1.current(0)
    attr_2.current(1)
    # scpfgr.delete(scpfgr.get_tk_widget().find_all())

    for item in scpfgr.get_tk_widget().find_all():
       scpfgr.get_tk_widget().delete(item)


def fileOutput():
    with open('output.csv', mode='w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",", quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["Attribute 1: " + label[x_index]])
        csv_writer.writerow(["Attribute 2: " + label[y_index]])
        csv_writer.writerow(["n: " + str(k)])

        for c in range(len(centroid)):
            row = []
            if c == 0 : row.append("1st Randomized: ")
            elif c == 1 : row.append("2nd Centroids: ")
            elif c == 2 : row.append("3rd Centroids: ")
            else : row.append(str(c+1) + "th Centroids: ")
            
            for i in centroid[c]:
                row.append("[ " + str(i[0]) + "," + str(i[1]) + " ]")
            csv_writer.writerow(row)
        
        for c in range(k):
            csv_writer.writerow(["Centroid " + str(c) + ": ", "[ " + str(centroid[-1][c][0]) + " , " + str(centroid[-1][c][1]) + "]"])
            for i in range(len(clusters)):
                if clusters[i][1] == c:
                    csv_writer.writerow(["[ " + str(dataset[i][x_index]) + " , " + str(dataset[i][y_index]) + " ]"])
                    

               


loadDataset()
# print(dataset)

#TKINTER UI

window = Tk()
window.title("Kmeans Clustering")
window.geometry("1000x500")
window.resizable(False, False)
window.config(background = "#222222")

Label(window,
    text='Select Attribute 1:',
    font="Helvetica",
    bg="#222222",
    fg="white"
).place(x=20,y=25)

attr_1sv = StringVar()
attr_1 = ttk.Combobox(window,
    width = 20,
    font="Helvetica",
    textvariable = attr_1sv,
    state = "readonly")
attr_1['values'] = label
attr_1.place(x=160, y=25)
attr_1.current(0)

Label(window,
    text='Select Attribute 2:',
    font="Helvetica",
    bg="#222222",
    fg="white"
).place(x=20,y=75)

attr_2sv = StringVar()
attr_2 = ttk.Combobox(window,
    width = 20,
    font="Helvetica",
    textvariable = attr_2sv,
    state = "readonly")
attr_2['values'] = label
attr_2.place(x=160, y=75)
attr_2.current(1)

Label(window,
    text='Enter N Clusters:',
    font="Helvetica",
    bg="#222222",
    fg="white"
).place(x=20,y=125)

nvalue_spinbox = StringVar()
n_sb = Spinbox(window,
    width = 5,
    font="Helvetica",
    from_ = 2,
    to = 10,
    textvariable=nvalue_spinbox,
    state="readonly")
n_sb.place(x=160, y=125)

run_btn = Button(window,
    text = "RUN",
    font="Helvetica",
    width="6",
    bg="#509bb9",
    fg="white",
    activeforeground="white",
    activebackground="#222222",
    highlightbackground="#509bb9",
    relief="flat",
    command=collectData
    )
run_btn.place(x=400, y=20)

reset_btn = Button(window,
    text = "RESET",
    font="Helvetica",
    bg="#509bb9",
    fg="white",
    activeforeground="white",
    activebackground="#222222",
    highlightbackground="#509bb9",
    relief="flat",
    command=resetCommand
    )
reset_btn.place(x=400, y=70)

Label(window,
    text='Centroids &\nClusters:',
    font="Helvetica",
    bg="#222222",
    fg="white"
).place(x=20,y=175)

text_frame = Frame(window, bg="#eeeeee")
text_frame.place(x=160, y=200)

text_box = Text(text_frame, width=38, height=16)
text_box.pack(side=LEFT)

scrllbr = Scrollbar(text_frame, orient=VERTICAL, bg="#509bb9")
scrllbr.pack(side=RIGHT, fill=Y)
text_box.config(yscrollcommand=scrllbr.set)
scrllbr.config(command=text_box.yview)

separator = ttk.Separator(window, orient='vertical')
separator.place(x=500, y=20, height = 460)

Label(window,
    text='Kmeans Scatter Plot:',
    font="Helvetica",
    bg="#222222",
    fg="white"
).place(x=520,y=25)

window.mainloop()