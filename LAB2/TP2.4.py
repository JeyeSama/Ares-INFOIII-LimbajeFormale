import re

def verifica_factura(nume_fisier):
    """Verifica daca un fisier respecta formatul unei facturi si ofera detalii despre erori."""
    with open(nume_fisier, 'r', encoding="utf-8") as f:
        continut = f.read().strip()  # get rid of extra spaces

    # Expresie regulata (regex) pentru validare completa/full
    factura_regex = r"""
    ^Factura\s+Nr:\s+(\d+)\s*  # Nr. factura
    Client:\s+([A-Za-z ]+)\s*  # Client (letters & spaces)
    Produse:\s+(.+)\s*         # Produse (anything text)
    Pret:\s+(\d+\.\d{2})\s*    # Pret (format ###.##)
    TVA:\s+(\d+)%\s*           # TVA (ex: 19%)
    Cantitate:\s+(\d+)$        # Cantitate (nr. intreg)
    """

    pattern = re.compile(factura_regex, re.MULTILINE | re.VERBOSE)

    match = pattern.match(continut)

    if match:
        print("Factura este valida!")
        return True
    else:
        print("Factura NU este valida. Verificam detaliile...\n")

        # Verificare individuala pentru fiecare sectiune
        erori = []

        # Verificam existenta si formatul fiecarui camp separat
        if not re.search(r"Factura\s+Nr:\s+\d+", continut):
            erori.append(" 'Factura Nr' lipseste sau are format gresit. (Ex: 'Factura Nr: 1234')")

        if not re.search(r"Client:\s+[A-Za-z ]+", continut):
            erori.append(" 'Client' lipseste sau are format gresit. (Ex: 'Client: Andrei Pop')")

        if not re.search(r"Produse:\s+.+", continut):
            erori.append(" 'Produse' lipseste sau are format gresit. (Ex: 'Produse: Laptop, Telefon')")

        if not re.search(r"Pret:\s+\d+\.\d{2}", continut):
            erori.append(" 'Pret' lipseste sau are format gresit. (Ex: 'Pret: 1250.99')")

        if not re.search(r"TVA:\s+\d+%", continut):
            erori.append(" 'TVA' lipseste sau are format gresit. (Ex: 'TVA: 19%')")

        if not re.search(r"Cantitate:\s+\d+", continut):
            erori.append(" 'Cantitate' lipseste sau are format gresit. (Ex: 'Cantitate: 2')")

        # 2️⃣ Afisam erorile gasite
        if erori:
            for eroare in erori:
                print(eroare)
        else:
            print(" Format aproape corect, dar factura tot nu trece validarea.")

        return False

# testing/exemplu attempt
nume_fisier = input("Introduceti numele fisierului de verificat: ")
verifica_factura(nume_fisier)
