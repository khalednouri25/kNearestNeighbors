import pandas as pd
import numpy as np

#read and split input data into training data, and labels, and also delete irrelevant attributes based on user input 
def dataSplit(urlData, label, irrelevantAttributes):
    data = pd.read_csv(urlData)
    labels = data[label]
    trainingSet = data.drop([label], axis = 1)
    trainingSet = trainingSet.drop(irrelevantAttributes, axis = 1)
    return trainingSet, labels

#calculate manhaten distance
def manhatanDistance(row, test):
    dist = 0.0
    row = np.array(row)
    #delete index from row
    row = np.delete(row, 0)
    lenRow = len(row)
    lenTest = len(test)
    assert lenRow == lenTest
    for index, valueTest in enumerate(test):
        valueRow = row[index]
        if (isinstance(valueRow, (int ,float)) and type(valueRow)!= type(True)):
            if (isinstance(valueTest, (int, float)) and type(valueTest)!= type(True)):
                dist = dist + abs(valueRow - valueTest)
            else:
                raise Exception('Training values and testing values must have the same type!, Expected type '+ str(type(valueRow))+ ' detected type:' + str(type(valueTest)))
                
                
        elif (isinstance(valueRow, str)):
            assert(type(valueTest) == str)
            if (valueRow == valueTest):
                dist = dist + 0
            else:
                dist = dist + 1
        elif (type(valueRow) is bool):
            assert (type(valueTest) == bool)
            if (valueRow == valueTest):
                dist = dist + 0
            else:
                dist = dist + 1
        else: 
             raise Exception('The two values must have the same type (all numbers or all strings)')
        
    return dist 
       
def knn (trainingSet, k, labels, test):     
    result = dict() 
    for  row in trainingSet.itertuples(index = True, name=None):
        indexRow = row[0]
        result[indexRow] = manhatanDistance(row, test)
    #sorted the result by ascending 
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
    #take the k first nearest neighbors
    kNeighbors = {k: result[k] for k in list(result)[:k]}
    return kNeighbors
   
   
def showResult (kNeighbors, k, labels, test):
    print ('***** Result *****')
    print ('the '+ str(k) +' nearest neighbors for '+ str(test) + ' are: ')
    for key, value in kNeighbors.items():
        print ('Row  '+ str(key) + '  with distance =  ' + str(round(value, 2)) + " Label =>    " + labels[key] )     
    
    
 #User input   
urlData = './Iris.csv'
label = 'Species'
irrelevantAttributes = ['Id']
k =5
test =[1.7, 2.8, 5.0, 1.5]


trainingSet, labels = dataSplit(urlData, label, irrelevantAttributes)
kNeighbors = knn(trainingSet, k, labels, test)
showResult(kNeighbors, k, labels, test)

        
        
    
    