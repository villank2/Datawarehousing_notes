import pandas as pd
import math
def euclid_distance(obj1,obj2):
    '''accepts list of format (attributes[])'''
    '''calculate the square root of the sum of the attributes differences squared
    such as ((x1-x2)² + (y1-y2)²)¹/²'''

    assert(len(obj1) == len(obj2))

    ed_value = 0
    for i in range(0,len(obj1)):
        x1 = obj1[i]
        x2 = obj2[i]
        squared_diff = (x1 - x2)**2
        ed_value += squared_diff

    return math.sqrt(ed_value)

def kmeans(li,centroids,k=3):
    '''accepts a list of objects of format (id,attributes[])
    argument k which is the number of clusters
    and argument centroids which is a list of centroids
    whose length must equal k'''

    assert(len(centroids) == k)
    

    cols = ["id"]
    for i in range(1,len(li[0][1:])+1):
        cols.append("attr{}".format(i))

    df = pd.DataFrame(li,columns=cols)

    #create clusters

    cluster_list = [[]] * k
    
    rows = df.shape[0]
    for i in range(0,rows+1):
        print(df)

if __name__ == "__main__":
    a = ['a',1,2]
    b = ['b',2,5]
    li = [a,b]
    k = 1
    centroids = [(3,4)]
    kmeans(li,centroids=centroids,k=k)