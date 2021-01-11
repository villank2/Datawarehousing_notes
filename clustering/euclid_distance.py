import sys
import math
def euclid_dist(x,y):
    assert(len(x)==len(y))
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

def agglohi_cluster(li):
    '''takes in a list of list of form [id,attr1,attr2,etc]
    check if an item in the main list is a cluster meaning 
    it is a list of lists'''
    item_list = []
    for item in li:
        x = Item(item)
        item_list.append(x)
    
    for item in item_list:
        print(item.id)
        

class Item():

    def __init__(self,li):
        self.id = li[0]
        self.atrrs = li[1:]
            
if __name__ == "__main__":
    a1 =[1,1,1,1]
    a10 = [3,1,1,2]
    a24 = [3,2,2,2]
    li = [[3,2,2,1]]
    for x in li:

        print(euclid_dist(x,a1),euclid_dist(x,a10),euclid_dist(x,a24))
        print()
        