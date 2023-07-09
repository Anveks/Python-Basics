from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f'What would you like to order?({options})\n').lower()
  if choice == 'report':
    coffee_machine.report()
  elif choice == 'off':
    is_on = False
    print('Turning off...')  
  else:
    selected_coffee = menu.find_drink(choice)
    if coffee_machine.is_resource_sufficient(selected_coffee):
      if money_machine.make_payment(selected_coffee.cost):
        coffee_machine.make_coffee(selected_coffee)
    
    