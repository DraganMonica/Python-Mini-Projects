# Coffee Machine Program
choices = [
    {
        'name': 'espresso',
        'water': 50,
        'coffee_quantity': 18,  # Changed 'quantity' to 'coffee_quantity'
        'milk_quantity': 0,
        'money': 1.5
    },
    {
        'name': 'latte',
        'water': 200,
        'coffee_quantity': 24,
        'milk_quantity': 150,
        'money': 2.5
    },
    {
        'name': 'cappuccino',
        'water': 200,
        'coffee_quantity': 24,
        'milk_quantity': 150,
        'money': 3.0
    },
]

# resources stock
resources = {
    'water': 300,
    'milk':  200,
    'coffee': 100,
    'money': 0
}

# coins
coin_operated = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.10,
    "Quarter": 0.25
}