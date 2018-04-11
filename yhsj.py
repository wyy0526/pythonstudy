def triangles():
    n =1
    while(1):
        if n == 1:
            listb = [1]
            yield listb
        if n > 1:
            lista = listb
            listb = []
            for i in range(n):
                #print('i:',i)
                if i == 0:
                    listb.append(1)
                if i >= 1 and  i < n-1:
                    listb.append(lista[i-1] + lista[i])
                if i == n-1:
                    listb.append(1)
            yield listb
        n = n + 1
    return


def main():
    n = 0
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break


main()