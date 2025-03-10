class AutomatBauturi:
    def __init__(self):
        """Initializare automatul cu starile si tranzitiile sale."""
        self.stare = "q0"  # Starea initiala
        self.tranzitii = {
            ("q0", "C"): "q1",  #  cafea
            ("q0", "T"): "q2",  #  ceai
            ("q0", "A"): "q3",  #  cappuccino
            ("q1", "OK"): "q4",  # Confirm cafea
            ("q2", "OK"): "q4",  # Confirm ceai
            ("q3", "OK"): "q4",  # Confirm cappuccino
            ("q4", "OK"): "q0",  # Return la starea initiala
        }

    def tranzitie(self, simbol):
        """Tranzitie pe baza simbolului de intrare."""
        if (self.stare, simbol) in self.tranzitii:
            self.stare = self.tranzitii[(self.stare, simbol)]
            print(f"Tranzitie efectuata: {simbol} -> Stare curenta: {self.stare}")
        else:
            print(f"Comanda '{simbol}' invalida in starea {self.stare}.") # Pe scurt, daca apasam pe C, cat timp suntem in q0, trecem la q1 (cafea)

    def ruleaza(self):
        """Simuleaza automatul"""
        print("Introduceti: C (cafea), T (ceai), A (cappuccino), OK (confirmare)")
        while True:
            comanda = input(">> ").strip().upper()
            if comanda == "EXIT":
                print("Inchidere automat.")
                break
            self.tranzitie(comanda)


# Rulare automat
automat = AutomatBauturi()
automat.ruleaza()
