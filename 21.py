n1, n2 = 1, 1
for a in range(1,40000):
    print(n1)
    nth= n1 + n2
    n1=n2
    n2=nth
    if(n1>4000000 or n2>4000000 or nth>4000000):
        break