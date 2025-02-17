def concatenate(s1, s2):
    return s1 + s2 

def invers(s):
    return s[::-1]  

def extract(s, i, j):
    return s[i:j+1]  # +1 ca sa includa si caracterul de la j

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)  # Replace numa prima aparitie

def process_l0_string(word):
    """Aplica operatiile cerute asupra unui cuvant din limbajul L."""
    results = {}

    # Aplicare operatii
    results["concatenare"] = concatenate(word, "xyz")
    results["repetare"] = word * 3  # S^n, se repeta de 3 ori
    results["inversare"] = invers(word)

    # Extractie (de la 2 la 4, daca sirul are destule caractere)
    if len(word) >= 5:
        results["extractie"] = extract(word, 2, 4)
    else:
        results["extractie"] = "String prea scurt"

    # Replace (prima aparitie a lui 'a' cu 'new')
    results["inlocuire"] = replace(word, "a", "new")

    return results

# Testing, testing, can you hear me?
word = "a3y2"  # Exemplu bun din E1, E2, E3
results = process_l0_string(word)
for op, res in results.items():
    print(f"{op}: {res}")  # Afisam operatia si rezultatul
