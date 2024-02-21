def mini_calc(first_input, second_input, operator):    
    calc_arr = []
    print("\n============= Welcome to mini calc! ==============")
    print("\n=================== Numbers ======================")
    
    calc_arr.append(int(first_input))
    print(first_input)
    print("-----" * 10)
    calc_arr.append(int(second_input))
    print(second_input)
    print("=====" * 10)
    print()
    
    while calc_arr[0] == 0 or calc_arr[1] == 0:
        calc_arr.pop(0)
        print("==================== Error =======================")
        print("You didn't entered number!")
        print("-----" * 10)
        calc_arr.append(int(input("Enter number: ")))
        print("=====" * 10)
        print()
    if operator == "-" or operator == "+" or operator == "*" or operator == "/":
        if operator == "1" or operator == "-" or operator == "(-)" or operator == "(1)":
            print("=================== Numbers ======================")
            print(calc_arr[0])
            print("-----" * 10)
            print(calc_arr[1])
            print("=====" * 10)
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} - {calc_arr[1]} = {calc_arr[0] - calc_arr[1]}")
            print('=====' * 10)
        elif operator == "2" or operator == "+" or operator == "(+)" or operator == "(2)":
            print("=================== Numbers ======================")
            print(calc_arr[0])
            print("-----" * 10)
            print(calc_arr[1])
            print("=====" * 10)
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} + {calc_arr[1]} = {calc_arr[0] + calc_arr[1]}")
            print('=====' * 10)  
        elif operator == "3" or operator == "*" or operator == "(*)" or operator == "(3)":
            print("=================== Numbers ======================")
            print(calc_arr[0])
            print("-----" * 10)
            print(calc_arr[1])
            print("=====" * 10)
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} * {calc_arr[1]} = {calc_arr[0] * calc_arr[1]}")
            print('=====' * 10)
        elif operator == "4" or operator == "/" or operator == "(/)" or operator == "(4)":
            print("=================== Numbers ======================")
            print(calc_arr[0])
            print("-----" * 10)
            print(calc_arr[1])
            print("=====" * 10)
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} / {calc_arr[1]} = {calc_arr[0] / calc_arr[1]}")
            print('=====' * 10)

    if operator != "-" and operator != "+" and operator != "*" and operator != "/":
        print("=================== Options ======================")
        user_input = input(
                """Please choose one option below.
--------------------------------------------------
1: -
2: +
3: *
4: /
--------------------------------------------------
Enter one option above: """) 
        print("=====" * 10)
        if user_input == "1" or user_input == "-" or user_input == "(-)" or user_input == "(1)":
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} - {calc_arr[1]} = {calc_arr[0] - calc_arr[1]}")
            print('=====' * 10)
        elif user_input == "2" or user_input == "+" or user_input == "(+)" or user_input == "(2)":
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} + {calc_arr[1]} = {calc_arr[0] + calc_arr[1]}")
            print('=====' * 10)
        elif user_input == "3" or user_input == "*" or user_input == "(*)" or user_input == "(3)":
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} * {calc_arr[1]} = {calc_arr[0] * calc_arr[1]}")
            print('=====' * 10)
        elif user_input == "4" or user_input == "/" or user_input == "(/)" or user_input == "(4)":
            print("\n=================== Output =======================")
            print(f"{calc_arr[0]} / {calc_arr[1]} = {calc_arr[0] / calc_arr[1]}")
            print('=====' * 10)
        else:
            print("\n=================== Output =======================")
            print("-----" * 10)
            print("==================== Error =======================")
            print("You didn't choose proper option above!")
            print("=====" * 10)
            print()
mini_calc("35", 0, "+")
