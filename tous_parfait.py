def tous_positif(L):
    for i in L:
        if i < 0:      
          return True
   
    else:
        return False
print(tous_positif([1,8]))
