class AutomatFinit:
    def __init__(self, stari, alfabet, tranzitii, stare_initiala, stari_finale):
        self.stari = stari  # Multimea/Amountul starilor
        self.alfabet = alfabet  # Alfabetul de intrare
        self.tranzitii = tranzitii  # Dictionar cu tranzitiile
        self.stare_initiala = stare_initiala  # Starea initiala
        self.stari_finale = stari_finale  # Multimea starilor finale

    def tranzitie(self, stare, caracter):
        """Returneaza urmatoarea stare in functie de caracterul citit"""
        return self.tranzitii.get((stare, caracter), None)

    def verificare_cuvant(self, cuvant):
        """Verifica daca un cuvant este acceptat de automat"""
        stare_curenta = self.stare_initiala
        for caracter in cuvant:
            stare_curenta = self.tranzitie(stare_curenta, caracter)
            if stare_curenta is None:  # Daca nu exista o tranzitie valida
                return False
        return stare_curenta in self.stari_finale  # Verificam daca suntem in stare finala


# Definim automatul finit
stari = {'q0', 'q1', 'q2', 'q3'}
alfabet = {'a', 'b', 'c', 'd'}
tranzitii = {
    ('q0', 'a'): 'q1', ('q0', 'b'): 'q0', ('q0', 'c'): 'q0', ('q0', 'd'): 'q0',
    ('q1', 'a'): 'q1', ('q1', 'b'): 'q2', ('q1', 'c'): 'q1', ('q1', 'd'): 'q1',
    ('q2', 'a'): 'q2', ('q2', 'b'): 'q2', ('q2', 'c'): 'q2', ('q2', 'd'): 'q3',
    ('q3', 'a'): 'q3', ('q3', 'b'): 'q3', ('q3', 'c'): 'q3', ('q3', 'd'): 'q3'
}
stare_initiala = 'q0'
stari_finale = {'q3'}

# Testare: Cream amount, test cuvant
automat = AutomatFinit(stari, alfabet, tranzitii, stare_initiala, stari_finale)

cuvinte_test = ["aabbcc", "aaa", "bbbaac"]
for cuvant in cuvinte_test:
    print(f"Cuvant: {cuvant}, Acceptat: {automat.verificare_cuvant(cuvant)}")
