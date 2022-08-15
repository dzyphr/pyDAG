#class MyClass:
#    x = 5
#newobject = MyClass()
#print(newobject.x)

#array = [1, 2, 3]
#print(array)
#dictionary = { 1: array  }
#print(dictionary)
#localint = ord('7') + ord('3') + ord('2')
#print(localint)
#bytes_val = localint.to_bytes(2, 'little')
#print(bytes_val)
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
    maxRange = 16
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

def findNumActive(num, arg):
    found = False;
    def checkAll():
        if num == dag.array[0] or num == dag.array[1] or num == dag.array[2]:
           found = True
        else:
            found = False
        return found
    def checkX():
        if num == dag.array[0]:
            found = True
        else:
            found = False
        return found
    def checkY():
        if num == dag.array[1]:
            found = True
        else:
            found = False
        return found
    def checkData():
        if num == dag.array[2]:
            found = True
        else:
            found = False
        return found
    switcher = {
            'all': checkAll(),
            'x': checkX(),
            'y': checkY(),
            'data': checkData()
    }
    return switcher.get(arg)

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
        found = False
        found  = findNumActive(7, 'y')
        print(dag.dictionary[i+1], found)
        
loadDAG(64) # load limit can be 4x the max range of the rng



