import random

stadii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lista = ["nuca", "galeata", "liliac", "iasomnie"]

# TODO-1 - alegerea random a unui cuvant
cuvant = random.choice(lista)
print(cuvant) # pt testare
lungime_cuvant = len(cuvant)

# TODO-2 - facem o lista care contine fiecare litera a cuvantului
lista = list(cuvant)
print(lista) # pt testare

# TODO-3 - in lista noua o sa punem spatiile libere
lista_noua = []
for _ in range(lungime_cuvant):
    lista_noua.append("_")
print(" ".join(lista_noua))

# -------------------------------------asta o sa se repete,  gen

game_over = False
stadiu_principal = 0
print(stadii[stadiu_principal])
while not game_over:

    # TODO-4 - Verificare dacă litera aleasă de user coincide cu vreo literă din cuvânt
    litera = input("Alege o litera: ").lower()

    if litera in cuvant:
        for i, char in enumerate(cuvant):
            if char == litera:
                lista_noua[i] = litera
    else:
        # Incrementăm stadiul doar dacă litera nu este în cuvânt
        stadiu_principal += 1
        print(stadii[stadiu_principal])

    print(" ".join(lista_noua))

    # Verificăm dacă jocul este câștigat
    if '_' not in lista_noua:
        game_over = True
        print("You win!")

    # Verificăm dacă jocul este pierdut (ultimul stadiu de spânzurătoare)
    if stadiu_principal == len(stadii) - 1:
        game_over = True
        print(f"You lose! The word was: {cuvant}")