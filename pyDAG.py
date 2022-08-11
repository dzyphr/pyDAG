#class MyClass:
#    x = 5
#newobject = MyClass()
#print(newobject.x)

#array = [1, 2, 3]
#print(array)
#dictionary = { 1: array  }
#print(dictionary)
import random
class DAG:
    i = 0
    x = 0
    y = 0
    data = 0
    array = [x, y, data]
    dictionary = { i : array }

dag = DAG()
xyArray = []
dataArray = []

def addEdge(x, y, i, data):
    dag.x = x
    dag.y = y
    if dag.i == 0:
        i = 1
    dag.i = i
    dag.data = data
    new_edge = [x, y, data]
    dag.array = new_edge
    dag.dictionary[i] = dag.array 
    dag.i = dag.i + 1 

def rng():
    maxRange = 4
    return random.randint(1, maxRange)

def checkDirection(dataX, dataY):
    k = 0
    while k < 1:
        location = [dataX, dataY]
        if location in xyArray:
            dataX = rng()
            dataY = rng()
        else:
            break
    return dataX, dataY

def loadDAG(limit):
    for i in range(limit):
        newX = rng()
        newY = rng()
        newX, newY = checkDirection(newX, newY)
        newData = rng()
        location = [newX, newY]
        xyArray.append(location)
        dataArray.append(newData)
        addEdge(newX, newY, dag.i,  newData)
        print(dag.dictionary[i])
        
loadDAG(16) # load limit can be 4x the max range of the rng




