"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""


from data import warehouse1, warehouse2
import time
import sys
from art import *
import os


# YOUR CODE STARTS HERE
def main_logo():
    os.system('clear')
    print('')
    tprint("WMS")
    print('Warehouse management system')
    print('')
    print('copyright luca.Inc 2022 all rights are reserved')
    print('-----------------------------------------------')
    print('')
    print('')

global app_run
app_run = True

main_logo()

mylist = ["Initializing application", "Loading user interface",
          "Accessing database", ".", "..", "...", "Finished"]
checkout_cred = ["Receive credentials"]
checkout_anim = [".", "..", "..-", " .-`", "  -``", "   ``-", "    `-.",
                 "     -._", "      ._.", "       _.", "        .", "                    "]


def loading_screen():
    def init_app(fname):
        for char in fname:
            time.sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()

    for i in range(0, 7):
        init_app(mylist[i])
        print('')

    for x in range(0, 5):
        b = "Loading" + "." * x
        print(b, end="\r")
        time.sleep(0.5)

loading_screen()


# variables
buyout = False

# Get the user name
user_name = input('Please provide your name: ')
print('')


def clear_screen():
    os.system('clear')
    main_logo()


clear_screen()
# Greet the user
print('Welcome', user_name)
print('')


time.sleep(0.1)


def checkout_loading():

    for x in range(0, 12):
        b = checkout_anim[x]
        print(b, end="\r")
        time.sleep(.05)


def checkout_process():
    sending = 'sendind data...'
    rc = 'Received credentials.'
    cc = 'Checking connection.'
    ct = 'Transfering money.'
    cf = 'Purchase completed.'

    def anim_check(cname):
        for char in cname:
            time.sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
    anim_check(sending)
    print('')
    checkout_loading()
    print('')
    anim_check(rc)
    print('')
    checkout_loading()
    print('')
    anim_check(cc)
    print('')
    checkout_loading()
    print('')
    anim_check(ct)
    print('')
    checkout_loading()
    print('')
    anim_check(cf)

    print('')
    print('-----------------------')
    print(user_name, ', thanks for the purchase! Your delivery is ready to be picked up!')
    print('-----------------------')
    global buyout
    buyout = False


def menu_1():
    print('----------------------------')
    print('Warehouse 1 items: ', len(warehouse1), '\n')

    w_len = len(warehouse1)
    for i in range(0, w_len):
        print('-', warehouse1[i])
    print('')
    print('Warehouse 2 items: ', len(warehouse2), '\n')
    w_len = len(warehouse2)
    for i in range(0, w_len):
        print('-', warehouse2[i])
    print('Back to the menu - Press enter!')
    input('')
    global app_run
    app_run = True


def menu_2():

    item = input('What is the name of the item?: ')
    if item in warehouse1 or item in warehouse2:
        print('')
        print(item, 'was found')
        maximum_ava = ''
        maximum_count = 0
        item_amount1 = warehouse1.count(item)
        item_amount2 = warehouse2.count(item)
        total_amount = item_amount1 + item_amount2
        print('Total amount:', item_amount1 + item_amount2)
        if item_amount1 >= 1 and item_amount2 >= 1:
            print('Location: Both warehouses')
            if item_amount1 > item_amount2:
                maximum_ava = 'Warehouse 1'
                maximum_count = warehouse1.count(item)
            elif item_amount1 < item_amount2:
                maximum_ava = 'Warehouse 2'
                maximum_count = warehouse2.count(item)
        elif item_amount1 >= 1 and item_amount2 == 0:
            print('Location: Warehouse 1')
            maximum_ava = 'Warehouse 1'
            maximum_count = warehouse1.count(item)
        elif item_amount2 >= 1 and item_amount1 == 0:
            print('Location: Warehouse 2')
            maximum_ava = 'Warehouse 2'
            maximum_count = warehouse2.count(item)

        if item_amount1 == item_amount2:
            print('Maximum availability: ', warehouse1.count(
                item), 'in both warehouses')
            maximum_ava = 'Both warehouses'
        else:
            print('Maximum availability: ', maximum_count, 'in', maximum_ava)
        print('----------------------------')
        amount_is_valid = False
        order = False
        while order == False:
            print('Would you like to order this item?(y/n) - Item:', item)

            order_check = input('')
            if order_check == 'y':
                order = True
            elif order_check == 'n':
                order = True
                amount_is_valid=True
        clear_screen()

        

        while amount_is_valid == False:
            amount = int(input('Enter amount: '))
            if amount <= total_amount:
                clear_screen()
                print('Checkout overview')
                print('-')
                print('\nItem:', item, '\nAmount:', amount,
                      '\nPick-Up-Location:', maximum_ava)
                print('-')
                
                buyout = input('Proceed to checkout?(y/n):')
                
                  
                print('----------------------------')
                if buyout == 'y':
                    clear_screen()
                    amount_is_valid = True
                    buyout = True
                    checkout_process()
                elif buyout == 'n':
                    print('Sad... but understandable. Till next time')
                    amount_is_valid = True
                    global app_run
                    app_run = True
            elif amount > total_amount:
                print('Bro, we aint having that much stuff. Try again..')
                amount_is_valid = False
    else:
        print('')
        print(item, 'was not found. Check your spelling, there might be a typo')


def menu_3():
    print('Thanks for stopping by. I hope you bought something or ill rm -rf you next time')
    global app_run
    app_run = False

# Show the menu and ask to pick a choice


def option_menu():
    print(user_name, ', please choose an option: \n \n- 1. List items by warehouse \n- 2. Search an item and place an order \n- 3. Quit \n \n: ')
    global menu
    try:
        menu = int(input('Enter 1,2 or 3: '))
    except:
        print('')
        clear_screen()
        print('failed to enter numerical characters from 1 - 3. Try again dude')
while app_run == True:
    option_menu()

    try:
        # If they pick 1
        if menu == 1:
            clear_screen()
            menu_1()

        # Else, if they pick 2
        elif menu == 2:
            clear_screen()
            menu_2()

        # Else, if they pick 3
        elif menu == 3:
            clear_screen()
            menu_3()
    except:
        print('')

#
# Else



