def addProducts():
    while True:

        file = open('products.txt', 'a')
        item_name = input('Enter Item Name :- ')
        item_price = input('Enter Item Price :- ')
        file.write('\n'+item_name+' - '+item_price)
        file.close()
        print('\n\nProduct Added.\n\n')
        a = input('Do You Want to Add More (Y/N) :- ')
        if a.upper() == 'Y':
            continue
        elif a.upper() == 'N':
            break
