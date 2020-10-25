# kNearestNeighbors
This repository contains the implementation of k-nearest neighbors algorithm (k-NN) with python 3. 
The algorithm have 5 inputs: 
    1) urlData: takes the url of training files. I have put a training file (Iris.csv) so the urlData is './Iris.csv' in this example.
    2) label: this input specifies the label(class) of the training data. In our training data (Iris.csv) the label(class) is 'Species'
    3)IrrelevantAttributes: this input specifies an array of irrelevant attributes, which does not help us in the classification process. In our example, the irrelevant attributes is Id.
    4) k: the number Of nearest neighbors.
    5) test: an array that contains the data test, in which we want to get the nearest neighbors.
 
I have put in the knn.py file an example of input data (line 67 to line 71), so just click on run and it will show you the result.
The result shows the first nearest neighbors with row number (features) and the distance between this features and data test, and also the class of features.
So the result is a majority vote of the labels.

If you wana try another example, just modify (urlData, label, irrelevantAttributes, k and test)
