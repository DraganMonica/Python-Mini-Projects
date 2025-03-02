# importuri
from dictionaries import resources
from dictionaries import choices
from dictionaries import coin_operated

# methods
def report():
    """Prints a report of the current resources."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(user_choice):
    # mesajelul de dinainte
    """Check if there are enough resources for the drink."""
    if resources['water'] < user_choice['water']:
        print("Sorry, there is not enough water.")
        return False
    if resources['milk'] < user_choice['milk_quantity']:
        print("Sorry, there is not enough milk.")
        return False
    if resources['coffee'] < user_choice['coffee_quantity']:
        print("Sorry, there is not enough coffee.")
        return False
    return True


def process_coins():
    """Calculates the total amount of money inserted by the user."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * coin_operated["Quarter"]
    total += int(input("How many dimes? ")) * coin_operated["Dime"]
    total += int(input("How many nickels? ")) * coin_operated["Nickel"]
    total += int(input("How many pennies? ")) * coin_operated["Penny"]
    return total


def transaction_successful(payment, drink_cost):
    """Return True if the payment is accepted, False otherwise."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources['money'] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    """Deduct the required ingredients from the resources."""
    resources['water'] -= drink['water']
    resources['milk'] -= drink['milk_quantity']
    resources['coffee'] -= drink['coffee_quantity']
    print(f"Here is your {drink['name']}. Enjoy!")


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        print("Goodbye! Have a great day!")
        is_on = False
    elif user_choice == "report":
        report()
    else:
        drink = next((item for item in choices if item["name"] == user_choice), None)
        if drink:
            if check_resources(drink):
                payment = process_coins()
                if transaction_successful(payment, drink['money']):
                    make_coffee(drink)
        else:
            print("Invalid choice. Please select again.")






