def triple_six_exact(ch):
    n=len(ch)
    if ch[0:3]=="666" and (n<=3 or ch[3]!="6"):
        return True
    if ch[n-3:n]=="666" and ch[n-3] != '6':
        return True
    for k in range (1,n-3):
     if ch[k:k+3]=="666" and  ch[k-1] != 6 and ch[k+3] != 6:
        return True
    return False
print(triple_six_exact('6666'))
