
def positif(L):
    E =0
    for i in L:
       if i >= 0:
          E +=1
    return E
print(positif([2, -1, 3, 4, -6, 0, 6]))
