
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True


def check_resources(available, needed):
    if 'water' in needed and available['water'] < needed['water']:
        result = {'not_enough': True, 'message': 'Sorry, not enough water.'}
        return result
    elif 'milk' in needed and available['milk'] < needed['milk']:
        result = {'not_enough': True, 'message': 'Sorry, not enough milk.'}
        return result
    elif 'coffee' in needed and available['coffee'] < needed['coffee']:
        result = {'not_enough': True, 'message': 'Sorry, not enough coffee.'}
        return result
    else:
        result = {'not_enough': False}
        return result


def get_money():
    pennies = int(input('How many pennies do you want to insert?\n'))
    nickels = int(input('How many nickels do you want to insert?\n'))
    dimes = int(input('How many dimes do you want to insert?\n'))
    quarters = int(input('How many quarters do you want to insert?\n'))

    money = {
        'pennies': pennies,
        'nickels': nickels,
        'dimes': dimes,
        'quarters': quarters
    }
    return (money['pennies'] * 00.1) + (money['nickels'] * 0.05) + (money['dimes'] * 0.10) + (money['quarters'] * 0.25)


def make_coffee(coffee):
    coffee = MENU[coffee]['ingredients']
    if 'water' in coffee: resources['water'] -= coffee['water']
    if 'milk' in coffee: resources['milk'] -= coffee['milk']
    if 'coffee' in coffee: resources['coffee'] -= coffee['coffee']


continue_coffee = True

while continue_coffee:
    choice = input('What would you like?\n').lower()

    if choice == 'report':
        print(resources)
    elif choice != 'report' and choice != 'off':
        selected_coffee = choice
        money = get_money()
        if MENU[selected_coffee]['cost'] > money:
            print('Sorry, not enough money. Money refunded.')
        else:
            check_result = check_resources(resources, MENU[selected_coffee]['ingredients'])
            if check_result['not_enough']:
                print(check_result['message'])
            else:
                make_coffee(selected_coffee)
                if 'money' not in resources:
                    resources['money'] = 0
                    resources['money'] += MENU[selected_coffee]['cost']
                else:
                    resources['money'] += MENU[selected_coffee]['cost']
                change = int(money - MENU[selected_coffee]['cost'])
                print(resources)
                if change != 0:
                    print(f'Enjoy your {selected_coffee} and come back soon! Your change is: {change} $')
                    to_continue = input('Do you want another coffee?\n').lower()
                    if to_continue != 'no':
                        continue
                    else:
                        continue_coffee = False
                else:
                    print(f'Enjoy your {selected_coffee} and come back soon!')
                    to_continue = input('Do you want another coffee?\n').lower()
                    if to_continue != 'no':
                        continue
                    else:
                        continue_coffee = False
    elif choice == 'off':
        print('Turning off...')
        is_on = False

