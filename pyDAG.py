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
xArray = []
yArray = []
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
    dag.dictionary = { dag.i : dag.array }
    dag.i = dag.i + 1 

def rng():
    a = 1
    b = 200#max range must be > or = to loadDAG limit
    return random.randint(a, b)

def checkDirection(data, kind):
    k = 0
    while k < 1:
        if kind == 'x':
            if data in xArray:
                data = rng()
            else:
                break
        elif kind == 'y':
            if data in yArray:
                data = rng()
            else:
                break
    return data

def loadDAG(limit):
    for i in range(limit):
        newX = checkDirection(rng(), 'x')
        newY = checkDirection(rng(), 'y')
        newData = rng()
        xArray.append(newX)
        yArray.append(newY)
        dataArray.append(newData)
        addEdge(newX, newY, dag.i,  newData)
        print(dag.dictionary)
        
loadDAG(199)#loadDAG limit must be < or = max rng




