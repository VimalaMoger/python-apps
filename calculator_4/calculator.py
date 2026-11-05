from asyncio import proactor_events

from calculator_art import logo

print(logo)

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
# Display operation menu:
myList =[i for i in operations_dict]
print(myList)

def calculator():
    should_continue = True
    operation_type = input("Pick an operation from the following options: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
    wrong_entry_count = -1

    while operation_type not in operations_dict:
        operation_type = input("Please enter a valid option: ")
        wrong_entry_count += 1
        if wrong_entry_count == 1:
            print("Try again later!")
            break

    if wrong_entry_count == -1:
        num1 = float(input("Enter first number: "))

        while should_continue:
                num2 = float(input("Enter second number: "))
                if operation_type in operations_dict:
                    answer = operations_dict[operation_type](num1, num2)
                    print(f"{num1} {operations_dict[operation_type].__name__} {num2} = {answer}")

                    choice = input("Would you like to continue? (y/n): ")
                    if choice == "y":
                        previous_result = input("Do you want to continue working with the previous result as the first number? (y/n): ")
                        if previous_result == "y":
                            operation_type = input(
                                "Pick an operation from the following options: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
                            num1 = answer
                        else:
                            operation_type = input(
                                "Pick an operation from the following options: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
                            num1 = int(input("Enter first number: "))
                    if choice == "n":
                        should_continue = False
    calculator()

calculator()