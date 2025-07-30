# Hidden Markov Model (HMM)

## Dataset

- The input text file is found in the data folder.
- It is named hmm.in

## Task

The goal of the exercise is to implement the Hidden Markov Model (HMM) program that would utilize the dataset. The output should be the probabilities in the found in hmm.in

## Input

At the start of the program, it reads the text file hmm.in

- The input file named hmm.in has the following format:
- 2 no. of string considered
- STSSTSSSTT string sequence 1
- TSSSSSTTSS string sequence 2
- S T possible values for each state in the Markov chain (MC)
- E F possible observable measurement values for each state in the MC
- P(E|S) P(F|S) pair values for P(E|S) and P(F|S), respectively
- P(E|T) P(F|T) pair values for P(E|T) and P(F|T), respectively
- 3 no of cases to be considered for the strings
- S1 given E1 compute for P(S1|E1)
- T3 given F3 compute for P(T3|F3)
- S2 given F2 compute for P(S2|F2)

## Required Output

The output of the program should be a textfile containing the probabilities of the cases considered. The output must be a textfile named "hmm.out".
