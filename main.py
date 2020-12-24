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

def report_show():
  water = resources["water"]
  milk = resources["milk"]
  coffee = resources["coffee"]
  return f"Water : {water}ml\nMilk : {milk}ml\nCoffee : {coffee}g\nMoney : ${profit}\n"

def is_resource_sufficient(drink):
  for item in drink["ingredients"]:
    if drink["ingredients"][item] > resources[item]:
      print(f"​Sorry there is not enough {item}.")
      return False
  return True

def make_coffee(choice):
  drink = MENU[choice]
  if is_resource_sufficient(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {choice} ☕️. Enjoy!")


def process_money():
  print("Please insert coins.")
  total = int(input("how many quarters?: ")) * 0.25
  total += int(input("how many dimes?: ")) * 0.1
  total += int(input("how many nickles?: ")) * 0.05
  total += int(input("how many pennies?: ")) * 0.01
  return total

def process_transaction(money,choice):
  drink_cost = float(MENU[choice]["cost"])
  if float(money) >= drink_cost:
    print(f"Here is ${round((money -drink_cost),2)} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

is_on = True

while is_on:
  choice = input(" What would you like? (espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    print(report_show())
  elif is_resource_sufficient(MENU[choice]):
    money_received = process_money()
    if process_transaction(money_received,choice):
      make_coffee(choice)