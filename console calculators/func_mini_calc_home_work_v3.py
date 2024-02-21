def mini_calc(first_input, second_input, operator):  # working operand + - * /  
    calc_arr = []
           
    print("\n============= Welcome to mini calc! ==============")
    print("\n=================== Numbers ======================")
    
    calc_arr.append(int(first_input))
    print(first_input)
    print("-----" * 10)
    calc_arr.append(int(second_input))
    print(second_input)
    print("=====" * 10)
    
    if calc_arr[0] == 0 and calc_arr[1] == 0:
        print("\n==================== Error =======================")
        print("You didn't entered any number!")
        print("-----" * 10)
        calc_arr.pop()
        calc_arr.pop()
        calc_arr.append(int(input("Enter first number: ")))
        print("-----" * 10)
        calc_arr.append(int(input("Enter second number: ")))
        print("=====" * 10)

    option_op = {"-": (calc_arr[0]) - (calc_arr[1]),
                "+": (calc_arr[0]) + (calc_arr[1]),
                "*": (calc_arr[0]) * (calc_arr[1]),
                "/": (calc_arr[0]) / (calc_arr[1]),
            }

    if operator in option_op:
        print("\n=================== Numbers ======================")
        print(calc_arr[0])
        print("-----" * 10)
        print(calc_arr[1])
        print("=====" * 10)
        print("\n=================== Output =======================")
        print(f"{calc_arr[0]} {operator} {calc_arr[1]} = {option_op[operator]}")
        print('=====' * 10)        
    else:
        print("==================== Error =======================")
        print("You didn't choose proper option!")
        print("=====" * 10)
        print()
        
mini_calc("35", 34, "+")
