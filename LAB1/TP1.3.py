import itertools  # itertools.product genereaza combinatii posibile

def generate_palindromes():
    """Genereaza palindroame de lungime 1-5 folosind cifrele 0,1,2."""
    alphabet = ['0', '1', '2']
    palindromes = {length: [] for length in range(1, 6)}

    for length in range(1, 6):
        for combo in itertools.product(alphabet, repeat=length):  # Generam toate combinatiile posibile
            word = ''.join(combo)  # Conversie intr-un string
            if word == word[::-1]:  # Verificam daca e palindrom
                palindromes[length].append(word)  # Append = adauga la sfarsit de lista

    return palindromes

# Print toate palindroamele generate
palindromes = generate_palindromes()
for length, words in palindromes.items():
    print(f"Lungime {length}: {words}")
