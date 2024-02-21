# First variation

def mini_calc():
    calc_arr = []
    print()
    print("============= Welcome to mini calc! ==============")
    print()
    print("=================== Numbers ======================")
    calc_arr.append(int(input("Enter first number: ")))
    print("-----" * 10)
    calc_arr.append(int(input("Enter second number: ")))
    print("=====" * 10)
    print()
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
        print()
        print("=================== Output =======================")
        print(f"{calc_arr[0]} - {calc_arr[1]} = {calc_arr[0] - calc_arr[1]}")
        print('=====' * 10)
    elif user_input == "2" or user_input == "+" or user_input == "(+)" or user_input == "(2)":
        print()
        print("=================== Output =======================")
        print(f"{calc_arr[0]} + {calc_arr[1]} = {calc_arr[0] + calc_arr[1]}")
        print('=====' * 10)
    elif user_input == "3" or user_input == "*" or user_input == "(*)" or user_input == "(3)":
        print()
        print("=================== Output =======================")
        print(f"{calc_arr[0]} * {calc_arr[1]} = {calc_arr[0] * calc_arr[1]}")
        print('=====' * 10)
    elif user_input == "4" or user_input == "/" or user_input == "(/)" or user_input == "(4)":
        print()
        print("=================== Output =======================")
        print(f"{calc_arr[0]} / {calc_arr[1]} = {calc_arr[0] / calc_arr[1]}")
        print('=====' * 10)
    else:
        print()
        print("==================== Error =======================")
        print("You didn't choose proper option above!")
        print("=====" * 10)

mini_calc()

