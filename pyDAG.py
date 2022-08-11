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

a = 1
b = 20
xArray = []
yArray = []
dataArray = []

def checkDirection(data, kind):
    if kind == 'x':
        for x in xArray:
            if x == data:
                data = random.randint(a, b)
            else:
                break
        return data

def loadDAG(limit):
    for i in range(limit):
        newX = checkDirection(random.randint(a, b), 'x')
        newY = random.randint(a, b)
        newData = random.randint(a, b)
        xArray.append(newX)
        yArray.append(newY)
        dataArray.append(newData)
        addEdge(newX, newY, dag.i,  newData)
        print(dag.dictionary)
        
loadDAG(5)




