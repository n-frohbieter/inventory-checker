inventory = {}

# Main loop that runs the program
while True:
    print()
    print('Enter x to exit program.')

    user_input = input('Enter Choice: ')
    print()

    if user_input.lower() == 'x':
        print('Exiting the program!')
        break

    else:
        print('Invalid Input!')
        continue
