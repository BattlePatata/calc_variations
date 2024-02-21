print('-----' * 10)
first_input = int(input("Enter first number: "))
print('-----' * 10)
second_input = int(input("Enter second number: "))

menu = input(
'''==================================================
Choose your operator:
1: +
2: -             
3: *             
4: /                          
==================================================
Enter here: ''')

print('-----' * 10)

if menu == "1": 
    print(f"{first_input} + {second_input} = {first_input + second_input}")
    print('=====' * 10)
elif menu == "2":
    print(f"{first_input} - {second_input} = {first_input - second_input}")
    print('=====' * 10)
elif menu == "3":
    print(f"{first_input} * {second_input} = {first_input * second_input}")
    print('=====' * 10)
elif menu == "4":
    print(f"{first_input} / {second_input} = {first_input / second_input}")
    print('=====' * 10)
else:
    print("Wrong operator, please enter proper operator.")
    print('=====' * 10)
