tranzitii = {
    'q0': {'a': {'q1'}},
    'q1': {'a': {'q1'}, 'ε': {'q2'}},
    'q2': {'b': {'q2', 'q3'}, 'a': {'q3'}},
    'q3': {'a': {'q3'}, 'b': {'q1'}, 'ε': {'q4'}},
    'q4': {}
}

# Starea initiala si starile finale
stare_initiala = 'q0'
stari_finale = {'q4'}

# test word
text = 'ab'


def epsilon_closure(stari, tranzitii):
    """Calculeaza multimea starilor accesibile prin epsilon-tranzitii."""
    stari_posibile = set(stari)
    proces = list(stari)

    while proces:
        stare = proces.pop(0)  # prima stare din lista de procesare
        for urm_stare in tranzitii.get(stare, {}).get('ε', set()):
            if urm_stare not in stari_posibile:
                stari_posibile.add(urm_stare)
                proces.append(urm_stare)

    return stari_posibile


# calcul multime stari accesibile from stare initiala
stari_posibile = epsilon_closure({stare_initiala}, tranzitii)

# fiecare character to word
for caracter in text:
    stari_noi = set()
    for stare in stari_posibile:
        stari_noi.update(tranzitii.get(stare, {}).get(caracter, set()))
    stari_posibile = epsilon_closure(stari_noi, tranzitii)

# check daca vreo stare e finala
if any(stare in stari_finale for stare in stari_posibile):
    print(f"Cuvantul '{text}' este acceptat de automat.")
else:
    print(f"Cuvantul '{text}' NU este acceptat de automat.")
