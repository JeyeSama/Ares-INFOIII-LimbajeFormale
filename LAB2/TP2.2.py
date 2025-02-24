def detectare_cat(text):
    """Verifica daca textul contine cuvantul 'cat' folosind un automat finit"""
    stare = 'q0'
    tranzitii = {
        ('q0', 'c'): 'q1', ('q0', '_'): 'q0',
        ('q1', 'a'): 'q2', ('q1', 'c'): 'q1', ('q1', '_'): 'q0',
        ('q2', 't'): 'q3', ('q2', 'c'): 'q1', ('q2', '_'): 'q0',
        ('q3', '_'): 'q3'  # Odata ce am gasit "cat", ramane in stare finala
    }

    for caracter in text:
        if caracter not in "abcdefghijklmnopqrstuvwxyz":
            caracter = "_"  # Orice caracter necunoscut duce la resetare (spatiu, numere etc.)
        stare = tranzitii.get((stare, caracter), 'q0')

        if stare == 'q3':
            return True  # Am detectat "cat"

    return False  # Nu am gasit "cat"

# Exemplu de rulare
text = "the little cat is sleeping"
print(f"Contine 'cat'? {detectare_cat(text)}")
