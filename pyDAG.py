#class MyClass:
#    x = 5
#newobject = MyClass()
#print(newobject.x)

#array = [1, 2, 3]
#print(array)
#dictionary = { 1: array  }
#print(dictionary)

class DAG:
    i = 0
    x = 0
    y = 0
    data = 0
    array = [x, y, data]
    dictionary = {}

dag = DAG()

def update(i, array):
    dag.array = array
    #dag.i = i
    dag.dictionary = { dag.i : dag.array }
    dag.i = dag.i + 1

def addEdge(x, y, i, data):
    dag.x = x
    dag.y = y
    dag.i = i
    dag.data = data
    new_edge = [x, y, data]



update(dag.i, dag.array)
print(dag.dictionary)
addEdge(4, 5)
print("dagx = ",dag.x)
print(dag.dictionary)
update(dag.i, dag.array)
print(dag.dictionary)
update(dag.i, dag.array)
print(dag.dictionary)
