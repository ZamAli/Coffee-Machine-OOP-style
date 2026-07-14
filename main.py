from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

set_off = False
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while not set_off:
    user_pick = input("What would you like?: ")
    if user_pick == "menu":
        print(menu.get_items())
    elif user_pick == "latte" or user_pick == "cappuccino" or user_pick == "espresso":
        y = menu.find_drink(user_pick)
        if coffee_maker.is_resource_sufficient(y):
            money_rec = money_machine.make_payment(y.cost)
            if money_rec:
                coffee_maker.make_coffee(y)
    elif user_pick == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_pick == "off":
        set_off = True
    else:
        menu.find_drink(user_pick)
