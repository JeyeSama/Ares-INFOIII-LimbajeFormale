# moore
tranzitii = {
    's1': {'a': 's1', 'b': 's2'},
    's2': {'a': 's1', 'b': 's2'}
}

output = {
    's1': 'o1',
    's2': 'o2'
}


stare = 's1'

# Cuvantul de test
text = 'aaabbbbaaabba'

# check every character from cuvinte
for caracter in text:
    if caracter in tranzitii[stare]:
        print(output[stare])
        stare = tranzitii[stare][caracter]  # go next
