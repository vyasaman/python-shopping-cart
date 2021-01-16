import time
import os


def showCart():
    os.system('cls')
    kart = open('cart.txt', 'r')
    sno = 1
    print('\n\n')
    for i in kart:
        print(str(sno)+'.', i)
        sno += 1
    print('\n\n')
    kart.close()


def checkout():
    process = 10
    for i in range(11):
        time.sleep(0.5)
        os.system('cls')
        print(str(process*i)+'%. completed')

    print('\n\nBill Generated.\n')
    time.sleep(2.0)

    print('-------- Shopping Cart --------\n\t Bill Invoice\n')
    f = open('cart.txt', 'r+')
    sum = 0
    file2 = []
    file = f.read().split('\n')
    for i in file:
        file2.append(i.split(' - '))
    del file2[-1]

    for i in range(len(file2)-1):
        if file2[i][1].isdigit():
            file2[i][1] = int(file2[i][1])
            sum += file2[i][1]

    for j in range(len(file2)):

        print(file2[j][0], '\t\t', file2[j][1], 'Rs')

    print('-------------------------------\nTotal amt:-\t\t', int(sum), 'Rs\n\n')
    f.truncate(0)

    f.close()
