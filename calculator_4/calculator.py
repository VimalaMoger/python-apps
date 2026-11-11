from calculator_art import logo
import sys

# Math Operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return round(a*b, 2)
def div(a,b):
    return round(a/b, 2)

operations_dict = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div,
}
# Display Operation Menu:
calc_functions =[(i, operations_dict[i].__name__) for i in operations_dict]

def user_selected_option():
    option_type = input(
        "Choose from the following options: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 'exit' to quit: ")
    if option_type == 'exit':
        quit()
    while option_type not in operations_dict:
        option_type = input("Choose the valid option: ")
        if option_type == 'exit':
            sys.exit(0)
    return option_type

def user_input(answer):
    num1 = 0
    start_first_num_again = True
    previous_result = input("Do you want to continue working with the previous result as the first number? (y/n): ")
    while previous_result != 'y' and previous_result != 'n':
        previous_result = input("Please type: (y/n)")
    if previous_result == 'y':
        option_type = user_selected_option()
        num1 = answer
    else:
        option_type = user_selected_option()
        while start_first_num_again:
            num1 = input("Enter first number: ")
            if num1.isdigit():
                num1 = int(num1)
                start_first_num_again = False
            else:
                start_first_num_again = True
    return option_type, num1

def calculator():
    print(logo)
    print(calc_functions)
    should_continue = True
    operation_type = user_selected_option()

    try:
        num1 = float(input("Enter first number: "))
        while should_continue:
            try:
                num2 = float(input("Enter second number: "))
                if operation_type in operations_dict:
                    answer = operations_dict[operation_type](num1, num2)
                    print(f"{num1} {operations_dict[operation_type].__name__} {num2} = {answer}")

                    choice = input("Would you like to continue? (y/n): ")

                    while choice != "y" and choice != "n":
                        choice = input("Please type: (y/n): ")

                    if choice == "y":
                        option_type, num = user_input(answer)
                        operation_type = option_type
                        num1 = num

                    if choice == "n":
                        should_continue = False
            except ValueError:
                print("Please enter the right value")
    except ValueError:
        print("Please enter the right value")
    calculator()

if __name__ == '__main__':
    calculator()