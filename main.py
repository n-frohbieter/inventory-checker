import csv

# Checks user int input
def get_valid_int_input(prompt):
    while True:
        try:
            number_value = int(input(prompt))
            if number_value < 0 :
                print('Please Enter a Positive Number.\n')
                continue

            return number_value

        except ValueError:
            print('Please Enter a Valid Number.\n')

def save_inventory(inventory):
    with open('inventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for item, amount in inventory.items():
            writer.writerow([item, amount])

def load_inventory():
    inventory = {}

    try:
        with open('inventory.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                item = row[0]
                quantity = int(row[1])
                inventory[item] = quantity

    except FileNotFoundError:
        print('No Inventory File Found! Starting Fresh\n')

    return inventory

inventory = load_inventory()

# Main loop that runs the program
while True:
    print('\nEnter x to exit program.')
    print('Enter 1 to View Inventory')
    print('Enter 2 to add Inventory Item')
    print('Enter 3 to Check if there is Enough Inventory for a Job')

    user_input = input('Enter Choice: ')
    print()

# This Exits the program
    if user_input.lower() == 'x':
        while True:
            print('Would You Like to Save Your Inventory?')
            save_program = input('Enter 1 for Yes or 2 for No: ')

            if save_program == '1':
                save_inventory(inventory)
                print('Inventory Saved! Exiting the Program!')
                break

            elif save_program == '2':
                print('Exiting the Program!')
                break

            else:
                print('Invalid Input!\n')
                continue
        break

# Displays total inventory
    elif user_input == '1':
        if not inventory:
            print('Inventory is Empty.')
        else:
            for item, quantity in inventory.items():
                print(f'{item}: {quantity}')

        continue

# Asks user to create new inventory item and the amount and places it in inventory
    elif user_input == '2':
        inventory_item = input('Enter the New Inventory Item Description: ').lower()
        item_quantity = get_valid_int_input('Enter the Amount of the Item: ')

        inventory[inventory_item] = item_quantity
        continue

# Checks to see if the Item is in inventory
    elif user_input == '3':
        check_item = input('What is the name of the Item you are checking?: ').lower()

        if check_item in inventory:
            check_amount = get_valid_int_input('How many do you need to produce the job?: ')

            # Checks to see if there is enough in inventory
            if check_amount <= inventory[check_item]:
                print('There is enough in inventory to produce a job!')

                while True:
                    print('Would You Like to Process this Order?')
                    process_order = input('Enter 1 to Process Order or 2 to Cancel: ')

                    if process_order == '1':
                        inventory[check_item] -= check_amount
                        print('Order was Processed')
                        break

                    elif process_order == '2':
                        print('Order was not Processed!\n')
                        break

                    else:
                        print('Invalid Input!\n')
                        continue

            else:
                print('There is not enough to produce a job! You will need to order more!')

        else:
            print('Item is not in Inventory! Cannot Fulfill the Job!')

        continue

# Catches invalid options from the user
    else:
        print('Invalid Input!')