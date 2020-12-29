import pandas as pd

def binary_dissimilarity(i,j):
    '''takes in two lists, of format (identifier,binary_attributes[])
    compare both object following the assymetric bianry dissimiliraty formula
    d(i,j) = (r+s)/p
    where i and j are the identifiers 
    r is the number of attributes where attrᵢ = 1 and attrⱼ = 0
    s is the number of attributes where  attrᵢ = 0 and attrⱼ = 1
    q is the number of attributes where attrᵢ = 1 and attrⱼ = 1
    and p = sum(r,s,q)'''

    ones = "py" #positive , yes
    zeros = "n" #negative, no
    cols = ["id"]
    for index_ in range(1,len(i[1:])+1):
        cols.append("attr{}".format(index_))
    df = pd.DataFrame([i,j],columns=cols)
    
    df = df.replace("n",0)
    df = df.replace("y",1)
    df = df.replace("p",1)
    
    q,r,s = 0,0,0

    for col in df.columns:
        if col == "id":
            continue

        val = list(df[col].values)
        if val == [1,1]:
            q+=1
        elif val == [1,0]:
            r+=1
        elif val == [0,1]:
            s+=1

    p = q + r + s
    diss = (r+s)/p
    print(diss)   
    
if __name__ == "__main__":
    i = ["p1","y","n","n","p"]
    j = ["p2","y","n","y","n"]

    binary_dissimilarity(i,j)
    