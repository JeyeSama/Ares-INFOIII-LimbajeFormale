def generate_grammar_words(max_length=4):
    """Genereaza toate sirurile 'a...b...' de lungime maximă max_length."""
    words = []
    
    for a_count in range(max_length + 1):  # Same as before, trebe +1 ca sa includa si 4
        for b_count in range(max_length + 1):
            word = 'a' * a_count + 'b' * b_count  # Generam sirurile conform gramaticii
            words.append(word)  # Append = adauga la sfarsit de lista
    
    return words

# Printam toate cuvintele generate
grammar_words = generate_grammar_words()
print(grammar_words)  # Afisam rezultatul
