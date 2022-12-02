while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter Operation(+,-,*,/,^,%,#,$): ")
    print(choice)

    def select_op(choice):
        if choice == "+" or choice == '-' or choice == "*" or choice == '/' or choice == "^" or choice == '%':
            return 1
        elif choice == "$":
            return 0
        elif choice == "#":
            return -1
        else:
            return 2

    def calculation(num_1, num_2):
        if choice == '+':
            result = float(num_1+num_2)
            print(num_1, choice, num_2, '=', result)

        elif choice == '-':
            result = float(num_1-num_2)
            print(num_1, choice, num_2, '=', result)
        elif choice == '*':
            result = float(num_1-num_2)
            print(num_1, choice, num_2, '=', result)
        elif choice == '*':
            result = float(num_1-num_2)
            print(num_1, choice, num_2, '=', result)
        elif choice == '/':
            if num_2 == 0:
                print('float division by zero')
                print(num_1, choice, num_2, '= None')
            else:
                result = float(num_1/num_2)
                print(num_1, choice, num_2, '=', result)
        elif choice == '^':
            result = float(num_1**num_2)
            print(num_1, choice, num_2, '=', result)
        elif choice == '%':
            result = float(num_1 % num_2)
            print(num_1, choice, num_2, '=', result)
    if (select_op(choice) == 1):
        num_1 = input('Enter first number: ')
        print(num_1)
        if '$' in num_1:
            continue
        elif num_1 == '#':
            print("Done. Terminating")
            exit()
        elif not num_1.isnumeric():
            print('Not a valid number,please enter again')
            continue
        num_2 = input('Enter second number: ')
        print(num_2)
        if '$' in num_2:
            continue
        elif num_2 == '#':
            print("Done. Terminating")
            exit()
        elif not num_2.isnumeric():
            print('Not a valid number,please enter again')
            continue
        num_1 = float(num_1)
        num_2 = float(num_2)
        calculation(num_1, num_2)
    if (select_op(choice)) == 2:
        print('Unrecognized operation')
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
