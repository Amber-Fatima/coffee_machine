MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
choice = True
def enough_resource(r,u):
    if u == "espresso" or u == "latte" or u == "cappuccino":
        if r["water"] < MENU[u]["ingredients"]["water"]:
            print('Sorry there is not enough water.')
            return False

        if r["milk"] < MENU[u]["ingredients"]["milk"]:
            print('Sorry there is not enough milk.')
            return False
        if r["coffee"] < MENU[u]["ingredients"]["coffee"]:
            print('Sorry there is not enough coffe.')
            return False
        else:
            return True
    else:
        print(f"{u} is not available in our machine")
        return False
def  process_coins():
    quarters=int(input("how many quarters?: "))*0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters+dimes+nickels+pennies

def enough_money(money,u):
    if money>MENU[u]["cost"] :
        print("Here is your latte ☕️. Enjoy!")
        global profit
        profit+=MENU[u]["cost"]
        #make coffee
        resources['milk']-=MENU[u]["ingredients"]['milk']
        resources['water'] -= MENU[u]["ingredients"]['water']
        resources['coffee'] -= MENU[u]["ingredients"]['coffee']

        return money-MENU[u]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")


while choice:
    user = input('What would you like? (espresso/latte/cappuccino):')
    if user == 'off':
        choice = False
    elif user == 'report':
        for i in resources:
            print(f'{i.title()}: {resources[i]}')
        print(f'Money: {profit}')
    else:
        if  enough_resource(resources,user)     :
            print("Please insert coins")
            user_money = process_coins()
            change=enough_money(user_money,user)
            print(f"Here is ${change} in change.")



