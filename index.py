import cart
import os
import productsList


def AddToCart(f):
    inp = int(input('Enter the Item No. :- '))
    data = open('cart.txt', 'a')
    data.write(str(f[inp][0]) + ' - ' + str(f[inp][1])+'\n')


def showProducts():
    sno = 1
    file = open('products.txt', 'r').read().split("\n")
    file2 = {}
    for i in file:
        file2[sno] = (i.split(" - "))
        sno += 1

    print('Item\t\t\t\t\tPrice\n--------------------------------------------')

    sno = 1
    for j in range(1, len(file2)+1):
        print(sno, '\t', file2[j][0], '\t\t\t', file2[j][1])
        sno += 1

    while True:
        inp = int(input('\n1.Add item to cart\n2.Return to Main Menu.'))
        if inp == 1:
            AddToCart(file2)
        elif inp == 2:
            break


def goToCart():
    while True:
        ch = int(input(
            'Choose an Option:-\n1.Show Cart\n2.Checkout\n3.Go Back to Previous Menu.\nEnter your choice:- '))
        if ch == 1:
            cart.showCart()
        elif ch == 2:
            cart.checkout()
        elif ch == 3:
            break
        else:
            print('invalid Input!')


print('-------------------- Welcome -------------------')
user = int(input('1. Retail User\n2. Co-orporate User\nEnter your choice:- '))
if user == 1:

    while True:
        print('\n1. Show Products\n2. Go to cart \n3. Exit')
        ch = int(input('Choose an Option from above (press 1,2 or 3):- '))
        if ch == 1:
            os.system('cls')
            showProducts()
        elif ch == 2:
            os.system('cls')
            goToCart()
        elif ch == 3:
            break
        else:
            print('Invalid Input!')

elif user == 2:
    while True:
        print('\n1. Show Products\n2. Add Products to list \n3. Exit')
        ch = int(input('Choose an Option from above (press 1,2 or 3):- '))
        if ch == 1:
            os.system('cls')
            showProducts()
        elif ch == 2:
            os.system('cls')
            productsList.addProducts()
        elif ch == 3:
            break
