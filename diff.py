# adding something
def rec(a):
    if a==0:
        return 1
    return a*rec(a-1)
print(rec(8))