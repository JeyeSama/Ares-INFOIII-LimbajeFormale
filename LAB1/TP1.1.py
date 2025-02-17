import itertools  # itertools.product genereaza combinatii posibile


def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)  # Inlocuieste toate aparitiile lui 'a' cu 'b' 

def lungime(s):
    return len(s)


A = ['a', 'b', 'c']
B = ['x', 'y', 'z']
C = ['1', '2', '3']

# Generare all combos posibile de cate un simbol din fiecare alfabet
combinations = itertools.product(A, B, C)

# Printam fiecare cuvant generat si aplicam operatiile definite
for combo in combinations:
    word = ''.join(combo)  # string din combinatie
    print(f"Original: {word}")
    print(f"  - Concatenat cu 'yz': {concatenate(word, 'yz')}")
    print(f"  - Inversat: {invers(word)}")
    print(f"  - Substituie '{word[0]}' cu 'x': {substituie(word, word[0], 'x')}")
    print(f"  - Lungime: {lungime(word)}")
    print()
