# Exercise for Kmeans Clustering

## Task

Create a program that will classify the datapoints from Wine.csv by choosing two attributes or columns.

## Input

The program must read the data from the data folder named Wine.csv. Wine.csv contains the data for kmeans clustering. It has columns of Alcohol,Malic_Acid,Ash,Ash_Alcanity,Magnesium,Total_Phenols,Flavanoids,Nonflavanoid_Phenols,Proanthocyanins,Color_Intensity,Hue,OD280,Proline,Customer_Segment. You need to ask the user two columns of data which will be used to classify the points into k clusters. The number of clusters must also be asked to the user.

The dataset is taken from this site: https://www.kaggle.com/xvivancos/tutorial-clustering-wines-with-k-means/data
You are NOT ALLOWED to use built in kmeans clustering algorithms. You must implement them all by scratch.

## Required Output

The output of the program is a text file named output.csv and a scatterplot graph. Output.csv contains the centroids and the points under each centroid. For the scatterplot, each color signifying a cluster and maximum of 10 clusters. It must also output the centroids and the points under it in a scrollable list box.

Example Output (output.csv):

Centroid: 0 (16.98586956521739, 1.9304347826086963)
[15.6, 1.71]

[11.2, 1.78]

[18.6, 2.36]

[16.8, 1.95]

[15.2, 1.76]

[14.6, 1.87]

[17.6, 2.15]

[14.0, 1.64]

[16.0, 1.35]

Centroid: 1 (22.179069767441863, 2.770581395348837)

[21.0, 2.59]

[20.0, 1.92]

[20.0, 1.57]

[20.0, 1.81]

[25.0, 2.05]

[22.5, 1.5]

[20.5, 1.81]

[20.5, 1.73]

[20.4, 1.61]

![image]([https://github.com/VEEpforge/CMSC-170/blob/main/kmeans-clustering/kmeans.PNG?raw=true])
