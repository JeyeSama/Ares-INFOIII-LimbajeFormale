tranzitii = {
    'S0': {'00': 'S0', '01': 'S1', '10': 'S0', '11': 'S1'},
    'S1': {'00': 'S1', '01': 'S1', '10': 'S0', '11': 'S0'}
}

output = {
    'S0': {'00': 0, '01': 1, '10': 0, '11': 1},
    'S1': {'00': 1, '01': 1, '10': 0, '11': 0}
}

state = 'S0'

while True:
    intrare = input("baga semnal (ex: 00, 01, 10, 11): ").strip()

    if intrare not in tranzitii[state]:
        print("Eroare: Semnal invalid. Try again, bucko.")
        continue
    
    state = tranzitii[state][intrare]
    iesire = output[state][intrare]

    print(f"Stare curenta: {state}")
    print("A Verde, B Rosu." if iesire == 0 else "A Rosu, B Verde.")
