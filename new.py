def prime(a):
    if a<=1:
        print('invaild')
    for i in range(2,a):
        if a%i==0:
            print(f'{a} it is not prime')
            break
    else:
        print(f'{a} it is prime')

prime(3)
def sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
print(sort([1,5,8,9,2,3,4]))
# recursion
def rec(a):
    for 
    return
print(rec())