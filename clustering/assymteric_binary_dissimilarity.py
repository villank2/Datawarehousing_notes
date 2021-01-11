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

    assert(len(i) == len(j))
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
    
    if p != 0:
        diss = (r+s)/p
        print(df)
        print(df["id"].values)
        print(diss)   
    
if __name__ == "__main__":
    pA = ["patient 1"] + list("ynynny")
    pB = ["patient 2"] + list("yyynyy")
    pC = ["patient 3"] + list("nnynyy")
    pD = ["patient 4"] + list("yyynyn")
    pE = ["patient 5"] + list("nnynyn")
    pf = ["patient 6"] + list("yyyyyn")
    pg = ["patient 7"] + list("yynyyy")
    li = [pA,pB,pC,pD,pE,pf,pg]

    i = 0
    while i < len(li)-1:
        j = i + 1
        while j < len(li):
            i_obj = li[i]
            j_obj = li[j]
            binary_dissimilarity(i_obj,j_obj)
            j += 1
        i += 1