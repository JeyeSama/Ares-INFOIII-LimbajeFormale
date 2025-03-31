def verifica_an_bn(cuvant):
    """Verifica daca un cuvant respecta formatul a^n b^n."""
    num_a = num_b = 0
    found_b = False

    for caracter in cuvant:
        if caracter == 'a' and not found_b:
            num_a += 1
        elif caracter == 'b':
            found_b = True
            num_b += 1
        else:
            return False  # Caracter invalid

    return num_a == num_b and num_a > 0  # n trebuie sa fie cel putin 1

# Testare
cuvinte = ["aabb", "aaaabbbb", "abab", "aaabb", "bbb"]
for c in cuvinte:
    print(f"{c}: {verifica_an_bn(c)}")
