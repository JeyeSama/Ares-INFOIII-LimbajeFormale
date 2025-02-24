import itertools

alfabet = {'a', 'b', 'c', 'd'}

def generare_limbaj():
    """Genereaza cuvinte cu exact 3 litere dublate si lungime maxim 6"""
    limbaj = []
    for perm in itertools.permutations(alfabet, 3):  # choose 3 litere diferite
        cuvant = ''.join([litera * 2 for litera in perm])  # Double fiecare litera
        if len(cuvant) <= 6:
            limbaj.append(cuvant)
    return limbaj

def verifica_cuvant(cuvant):
    """Verifica daca un cuvant apartine limbajului generat"""
    return cuvant in generare_limbaj()

# Generam limbajul
L = generare_limbaj()
print("Limbaj generat:", L)

# Testam cateva cuvinte
cuvinte_test = ["aabbcc", "aaa", "bbbaac"]
for cuvant in cuvinte_test:
    print(f"Cuvant: {cuvant}, Acceptat: {verifica_cuvant(cuvant)}")
