tranzitii = {
    'q0': {'ε': {'q1', 'q10'}},
    'q1': {'b': {'q2'}},
    'q2': {'ε': {'q3', 'q4'}},
    'q3': {'a': {'q5'}},
    'q4': {'b': {'q6'}},
    'q5': {'ε': {'q7'}},
    'q6': {'ε': {'q7'}},
    'q7': {'ε': {'q8'}},
    'q8': {'ε': {'q9'}},
    'q9': {'ε': {'q11', 'q17'}},
    'q10': {'a': {'q18'}},
    'q11': {'ε': {'q12', 'q13'}},
    'q12': {'a': {'q14'}},
    'q13': {'b': {'q15'}},
    'q14': {'ε': {'q16'}},
    'q15': {'ε': {'q16'}},
    'q16': {'ε': {'q11', 'q17'}},
    'q17': {'ε': {'q19'}},
    'q18': {'ε': {'q19'}},
    'q19': {'ε': {'q20'}},
    'q20': {}
}

# Starea initiala si finale
stare_initiala = 'q0'
stari_finale = {'q20'}

# Cuvantul de verificat
text = 'bbaaaaaaaabb'


def epsilon_closure(stari, tranzitii):
    """
    Determina inchiderile epsilon pentru un set de stari.
    """
    stari_rezultate = set(stari)
    procesare = list(stari)
    
    while procesare:
        stare_curenta = procesare.pop(0)
        for urm_stare in tranzitii.get(stare_curenta, {}).get('ε', set()):
            if urm_stare not in stari_rezultate:
                stari_rezultate.add(urm_stare)
                procesare.append(urm_stare)
    
    return stari_rezultate

# Determina starile accesibile initial
stari_curente = epsilon_closure({stare_initiala}, tranzitii)

# same as previous, try every character in text
for caracter in text:
    stari_urmatoare = set()
    
    for stare in stari_curente:
        stari_urmatoare.update(tranzitii.get(stare, {}).get(caracter, set()))
    
    stari_curente = epsilon_closure(stari_urmatoare, tranzitii)

# check if at least one or two states are met
if any(stare in stari_finale for stare in stari_curente):
    print(f"{text} apartine")
else:
    print(f"{text} nu apartine")
