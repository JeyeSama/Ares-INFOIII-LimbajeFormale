class ParcareAutomata:
    def __init__(self, numar_locuri):
        """Initializare parcarea cu locuri libere si ocupate."""
        self.numar_locuri = numar_locuri
        self.locuri = ["liber"] * numar_locuri  # Initial, toate locurile sunt libere

    def afiseaza_stare(self):
        """Afiseaza starea curenta a parcarii."""
        print("\nStare parcare:")
        for i, loc in enumerate(self.locuri):
            print(f"Loc {i + 1}: {loc}")
        print()

    def parcheaza(self):
        """Gaseste un loc liber si parcheaza masina."""
        if "liber" not in self.locuri:
            print("Parcarea este plina!")
            return

        for i in range(self.numar_locuri):
            if self.locuri[i] == "liber":
                self.locuri[i] = "ocupat"
                print(f"Masina parcata la locul {i + 1}.")
                break

    def pleaca(self, loc):
        """Elibereaza un loc de parcare."""
        if 1 <= loc <= self.numar_locuri and self.locuri[loc - 1] == "ocupat":
            self.locuri[loc - 1] = "liber"
            print(f"Locul {loc} a fost eliberat.")
        else:
            print("Loc invalid sau deja liber.")

    def ruleaza(self):
        """Simuleaza interactiunea cu parcarea."""
        while True:
            self.afiseaza_stare()
            comanda = input("Introduceti comanda (PARCARE, PLECARE <nr>, EXIT): ").strip().upper()

            if comanda == "EXIT":
                print("Inchidere parcare.")
                break
            elif comanda == "PARCARE":
                self.parcheaza()
            elif comanda.startswith("PLECARE"):
                try:
                    loc = int(comanda.split()[1])
                    self.pleaca(loc)
                except:
                    print("Format invalid. Folositi: PLECARE <nr>")

# Rulare
parcare = ParcareAutomata(numar_locuri=5)
parcare.ruleaza()
