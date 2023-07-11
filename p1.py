q = int(input())
while q:
    q-=1
    #input strirng and list it and split it(removes spaces)
    a = input().split(' ')
    #for each string in list small case
    for i in range(len(a)):
        a[i] = a[i].capitalize()


    #output list
    print(a)