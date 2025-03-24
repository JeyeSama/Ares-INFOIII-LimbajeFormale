tranzitii = {
    'q1': {'X': 'q2', 'Y': 'q1'},
    'q2': {'X': 'q1', 'Y': 'q2'}
}


output = {
    'q1': 'o1',
    'q2': 'o2'
}


stare = 'q1'

# Cuvantul de test
text = 'XXXYYYXXX'

for caracter in text:
    if caracter in tranzitii[stare]:
        print(output[stare]) 
        stare = tranzitii[stare][caracter]

