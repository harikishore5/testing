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
