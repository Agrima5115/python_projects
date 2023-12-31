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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def update_resources(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


def check_resource(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough =  False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25    #1 quarter = 25 cents
    total += int(input("How many dimes?: ")) * 0.1        #1 dime = 10 cents
    total += int(input("How many nickels?: ")) * 0.05     #1 nickel = 5 cents
    total += int(input("How many pennies?: ")) * 0.01     #1 Penny = 1 cent
    return total

def check_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change, ${change}")
        global profit
        profit = profit +  drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_success(payment, drink["cost"]):
                update_resources(choice, drink["ingredients"])