☕ Coffee Machine Program

This is a simple console-based coffee machine simulation written in Python.

📂 Project Structure

- main.py: Contains the main logic of the program, including:
    - Displaying the menu.
    - Processing orders.
    - Checking resources.
    - Handling payments.
    - Dispensing drinks.
- dictionaries.py: Contains the data for:
    - Available drinks (ingredients and prices).
    - Initial stock of resources (water, milk, coffee, money).
    - Coin values (Penny, Nickel, Dime, Quarter).

 📝 Features

- User can order:
    - ☕ Espresso
    - ☕ Latte
    - ☕ Cappuccino
- Machine checks if there are enough resources for the selected drink.
- User inserts coins to pay.
- Machine checks if the payment is enough.
- If all checks pass, the drink is made and resources are updated.
- Admin command: `report` displays current resource levels.
- Admin command: `off` turns off the machine.


🚀 How to Run

Make sure both main.py and dictionaries.py are in the same folder, then run: main.py


EXEMPLE RUN:

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is your latte. Enjoy!

Requirements
Python 3.x
