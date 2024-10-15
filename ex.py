def triple_six_exact(ch1, ch2):
    if ch1 in ch2 or ch2 in ch1:
        return True
    else:
        return False
print(triple_six_exact("666","6666"))
