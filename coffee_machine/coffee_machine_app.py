from ingredients_menu import MENU, resources
from coffee_machine_logo import logo

profit = 0

def get_report():
    return resources

def make_coffee(user_input):
    style = MENU[user_input]
    if check_resources_sufficient(style['ingredients']):
        if transaction_successful(user_input):
            update_resources(style['ingredients'])
            print(f"☕Here is your {user_input}. Enjoy!")

def update_resources(ingredients):
    """Update the resources once the order is completed."""
    resources_left = get_report()
    if resources_left['water'] >= ingredients['water']:
        if resources_left['coffee'] >= ingredients['coffee']:
            water = resources_left['water'] - ingredients['water']
            coffee = resources_left['coffee'] - ingredients['coffee']
            resources['water']= water
            resources['coffee'] = coffee
            if 'milk' in ingredients:
                if resources_left['milk'] >= ingredients['milk']:
                    milk = resources_left['milk'] - ingredients['milk']
                    resources['milk'] = milk

def check_resources_sufficient(ingredients):
    """Returns True when order can be made. False if ingredients are insufficient"""
    resources_left = get_report()
    if resources_left['water'] >= ingredients['water']:
        if resources_left['coffee'] >= ingredients['coffee']:
            if 'milk' in ingredients:
                if resources_left['milk'] >= ingredients['milk']:
                    return True
                else:
                    print("Sorry, there is not enough milk")
            return True
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")
    return False

def process_coins():
    """Returns the total from coins inserted"""
    total_payment = 0
    valid_coins = { 25 : "Quarter", 10 : "Dime", 5 : "Nickel", 1 : "Penny"}
    flag = True
    print(f"{valid_coins}")
    for key in valid_coins.keys():
        while flag:
            try:
                coin_in_cents =  int(input(f"Please insert ({valid_coins[key]} in cents): "))
                if key == coin_in_cents:
                    how_many = int(input(f"How many {valid_coins[key]}s do you have? "))
                    total_payment += coin_in_cents * how_many
                    break
                else:
                    print(f"Invalid coin denomination. Please insert {key}.")
                    flag = True
            except ValueError:
                print("Please enter a valid number.")
                flag = True
    return total_payment / 100

def transaction_successful(user_input):
    """Returns True when payment is accepted. False if money is not sufficient."""
    global profit
    total_payment  = process_coins()
    if total_payment < MENU[user_input]['cost']:
        print(f"Sorry that's not enough money. Money refunded: ${total_payment}")
        return False
    elif total_payment > MENU[user_input]['cost']:
        change = round(total_payment - MENU[user_input]['cost'],2)
        profit += MENU[user_input]['cost']
        resources['Money'] = f"${profit}"
        print(f"Payment complete! Total inserted: ${total_payment}.")
        print(f"${total_payment} - ${MENU[user_input]['cost']} = ${change}")
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print(f"Payment complete! Total inserted: {total_payment} cents.")
        return  True

def coffee_machine_app():

    user_input = input("What would you like? (espresso/latte/cappuccino): or type 'off' to stop ")
    if user_input == 'off':
        quit()
    if user_input in ['espresso', 'latte', 'cappuccino']:
        make_coffee(user_input)
    else:
        coffee_machine_app()

    show_report = input("Would you want to see report? type 'report' ")
    if show_report == 'report':
        print(get_report())
    coffee_machine_app()

if __name__ == '__main__':
    print(logo)
    coffee_machine_app()