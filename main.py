inventory = {}

inventory['33.5 Pronto'] = 100

# Main loop that runs the program
while True:
    print()
    print('Enter x to exit program.')
    print('Enter 1 to View Inventory')
    print('Enter 2 to add Inventory Item')
    print('Enter 3 to Check if there is Enough Inventory for a Job')

    user_input = input('Enter Choice: ')
    print()

# This Exits the program
    if user_input.lower() == 'x':
        print('Exiting the program!')
        break

# Displays total inventory
    elif user_input == '1':
        print(inventory)
        continue

# Asks user to create new inventory item and the amount and places it in inventory
    elif user_input == '2':
        inventory_item = input('Enter the New Inventory Item Description: ').lower()
        item_quantity = int(input('Enter the Amount of the Item: '))

        inventory[inventory_item] = item_quantity
        continue

# Checks to see if the Item is in inventory
    elif user_input == '3':
        check_item = input('What is the name of the Item you are checking?: ').lower()

# Checks to see if there is enough in inventory
        if check_item in inventory:
            check_amount = int(input('How many do you need to produce the job?: '))

            if check_amount <= inventory[check_item]:
                print('There is enough in inventory to produce a job!')

            else:
                print('There is not enough to produce a job! You will need to order more!')

        else:
            print('Item is not in Inventory! Job is not Possible!')

        continue

# Catches invalid options from the user
    else:
        print('Invalid Input!')
        continue
