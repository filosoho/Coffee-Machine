from logo import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1200,
    "milk": 400,
    "coffee": 100,
}

profit = {"money": 0}


def report():
    """Prints a report of current resources and profit."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = profit["money"]
    print("==============================================================")
    print(f'''    Water: {water}ml
    Milk: {milk}ml
    Coffee: {coffee}g
    Money: ${money}''')
    print("==============================================================")


def check_resources(choice):
    """Returns True when order can be made, False if ingredients are insufficient."""
    water = MENU[choice]['ingredients']['water']
    coffee = MENU[choice]['ingredients']['coffee']
    if choice == 'espresso':
        if resources["water"] >= water and resources["coffee"] >= coffee:
            return True
        elif resources["water"] < water:
            print("==============================================================")
            print("     Sorry there is not enough water. 🫗")
            print("==============================================================")
            return False
        elif resources["coffee"] < coffee:
            print("==============================================================")
            print("     Sorry there is not enough coffee. (っ-,-)つ☕")
            print("==============================================================")
            return False
    elif choice == 'latte' or choice == 'cappuccino':
        milk = MENU[choice]['ingredients']['milk']
        if resources["water"] >= water and resources["milk"] >= milk and resources["coffee"] >= coffee:
            return True
        elif resources["water"] < water:
            print("==============================================================")
            print("     Sorry there is not enough water. 🫗")
            print("==============================================================")
            return False
        elif resources["milk"] < milk:
            print("==============================================================")
            print("     Sorry there is not enough milk. 🥛")
            print("==============================================================")
            return False
        elif resources["coffee"] < coffee:
            print("==============================================================")
            print("     Sorry there is not enough coffee. (っ-,-)つ☕")
            print("==============================================================")
            return False


def insert_coins(choice):
    """Returns the total calculated from coins inserted."""
    numbers = False
    while numbers == False:
        try:
            print("==============================================================")
            print("Please insert coins. 💰")
            print("==============================================================")
            quarters = float(input("how many quarters?: ")) * 0.25
            dimes = float(input("how many dimes?: ")) * 0.10
            nickles = float(input("how many nickles?: ")) * 0.05
            pennies = float(input("how many pennies?: ")) * 0.01
            total = quarters + dimes + nickles + pennies
            numbers = True
            return total
        except ValueError:
            print("\n---------------------------------------")
            print("Incorrect input. Please enter a number.")


def calculate_cost(choice):
    """Calculates if the money inserted is sufficient and prompts to make the coffee
    or/and prints relevant message to the user.
    """
    cost = MENU[choice]['cost']
    user_coins = insert_coins(choice)
    if user_coins == cost:
        make_coffee(choice)
    if user_coins > cost:
        change = round(user_coins - cost, 2)
        print("==============================================================")
        print(f"Here is ${change} in change. 👛")
        print("==============================================================")
        make_coffee(choice)
    elif user_coins < cost:
        print("==============================================================")
        print("Sorry that's not enough money. Money refunded. 💵")
        print("==============================================================")


def make_coffee(choice):
    """Deduct the required ingredients from the resources."""
    cost = MENU[choice]['cost']
    profit["money"] += cost
    water = MENU[choice]['ingredients']['water']
    coffee = MENU[choice]['ingredients']['coffee']
    if choice == 'espresso':
        resources["water"] -= water
        resources["coffee"] -= coffee
        print("""           
                     c[_]

    Here is your espresso (っ˘ڡ˘ς)☕️. Enjoy! 😋""")
    elif choice == 'latte':
        milk = MENU[choice]['ingredients']['milk']
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print("""               
                    ((((
                     ))))
                  _ .---.
                 ( |`---'|
                  \|     |
                  : .___, :
                   `-----'

    Here is your latte (っ˘ڡ˘ς)☕️. Enjoy! 😋""")
    if choice == 'cappuccino':
        milk = MENU[choice]['ingredients']['milk']
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print("""
                   _..,----,.._
                .-;'-.,____,.-';
               (( |            |
                `))            ;
                 ` \          /
                .-' `,.____.,' '-.
               (     '------'     )
                `-=..________..--'

    Here is your cappuccino (っ˘ڡ˘ς)☕️. Enjoy! 😋""")
    print("==============================================================")


def operate_coffee_machine():
    """Performs operations and checks required to order a coffe.
    Includes hidden option to print a report or turn the coffee machine off.
    """
    machine_on = True
    while machine_on == True:
        choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            if check_resources(choice):
                calculate_cost(choice)
        elif choice == 'report':
            report()
        elif choice == 'off':
            machine_on = False
        else:
            print("Incorrect input. Try again")


print(logo)
operate_coffee_machine()