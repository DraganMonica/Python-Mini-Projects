def calculare(number1, number2, operation):
    total = 0
    if operation == "+":
        total = number1 + number2
    elif operation == "-":
        total = number1 - number2
    elif operation == "*":
        total = number1 * number2
    elif operation == "/":
        total = number1 / number2
    return total

while True:
    # Introducem primul număr
    first_number = float(input("What's the first number?: "))

    # Începem o altă buclă pentru a continua calculul cu rezultatul anterior
    continue_calculating = True

    while continue_calculating:
        # Afișăm opțiunile disponibile
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")

        # Introducem următorul număr
        next_number = float(input("What's the next number?: "))

        # Calculăm rezultatul
        result = calculare(number1=first_number, number2=next_number, operation=operation)
        print(f"Result: {result}")

        # Întrebăm utilizatorul dacă dorește să continue cu rezultatul precedent sau să înceapă de la zero
        continue_or_not = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'exit' to quit: ").lower()

        if continue_or_not == "y":
            first_number = result  # Folosim rezultatul ca primul număr pentru următoarea operație
        elif continue_or_not == "n":
            break  # Iesim din bucla curenta si incepem de la zero
        elif continue_or_not == "exit":
            print("Goodbye!")
            exit()
