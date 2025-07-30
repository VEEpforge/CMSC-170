# Linear Classification using Perceptrons

## Background

A perceptron is a form of simple neural network, consisting of a single neuron that takes a feature vector with n coordinates, assigns each coordinate with a corresponding weight, and outputs the feature vector’s classification based on a threshold function. The perceptron algorithm was conceptualized by Frank Rosenblatt in 1957, and it was one of the first neural networks to be implemented.

Perceptron only works on linearly separable data. If the training data is not linearly separable, the perceptron algorithm will not converge

## Task

Create a program that will take compute for the weights need to classify using Perceptrons.

## Input

Sample input is provided. Test cases are also given with the desired number of iterations and final weight
The format of the input should be the following:

```
0.1 -Learning rate
0.5 -Threshold
1	-Bias
0 0 0 -x0, x1, z
0 1 1
1 0 1
1 1 1
```

note that the number of columns for x values should not be restrained to 2 only.

## Required Output

The output of the program is a text file named output.out which shows the step by step computation per iteration
example:

```
Iteration 1:
         x0      x1      b       w0      w1      wb      a       y       z
         0       0       1.0     0       0       0       0.0     0       0
         0       1       1.0     0.0     0.0     0.0     0.0     0       1
         1       0       1.0     0.0     0.1     0.1     0.1     0       1
         1       1       1.0     0.1     0.1     0.2     0.4     0       1
Iteration 2:
         x0      x1      b       w0      w1      wb      a       y       z
         0       0       1.0     0.2     0.2     0.3     0.3     0       0
         0       1       1.0     0.2     0.2     0.3     0.5     0       1
         1       0       1.0     0.2     0.3     0.4     0.6     1       1
         1       1       1.0     0.2     0.3     0.4     0.9     1       1
Iteration 3:
         x0      x1      b       w0      w1      wb      a       y       z
         0       0       1.0     0.2     0.3     0.4     0.4     0       0
         0       1       1.0     0.2     0.3     0.4     0.7     1       1
         1       0       1.0     0.2     0.3     0.4     0.6     1       1
         1       1       1.0     0.2     0.3     0.4     0.9     1       1
```
