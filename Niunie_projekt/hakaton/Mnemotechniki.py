
# Funkcja zwraca listę ze stringami słów, których kolor trzeba zmienić na szary
# zmienić last i first word na 2 lub 3

def szare_konce(lista):
    first_last_words = ''
    class TextTransformer:
        def __init__(self):
            pass

        def transform_text(self, text):
            lines = text.split("\n")
            new_lines = []
            first_last_words = []
            for line in lines:
                words = line.split()
                if len(words) < 5:
                    new_lines.append(line)
                else:
                    first_word = words[:2]
                    last_word = words[-2:]
                    middle_words = words[2:-2]
                    new_line = f"{first_word} {' '.join(middle_words)} {last_word}"
                    new_lines.append(new_line)
                    first_last_words.append(f"{first_word} {last_word}")
            print(first_last_words)
            return "\n".join(new_lines)
    
    pisak=""
    stopword=""

    while True:
        text = input()
        if text.strip() == stopword:
            break
        pisak += "%s\n" % text


    transformer = TextTransformer()
    transformed_text = transformer.transform_text(pisak)


    first_last_words.split()
    print(first_last_words)



# Słowa klucze zwraca listę indeksów w których znajdują się poniższe słowa do wyszukania w inpucie. 
# Trzeba te słowa z tych indeksów jakoś wyróżnić na tle innych


def slowa_klucze(my_list):
    text=""
    stopword=""

    while True:
        inp = input()
        if inp.strip() == stopword:
            break
        text += "%s\n" % inp
    print(text)
    textsplot = text.split()


    words_to_find = ["dlatego", "ponieważ", "gdyż", "zatem", "szczególnie", "istotne", "podobnie", "bo", "natomiast", "również"]


    indices = []
    for i, item in enumerate(textsplot):
        if item in words_to_find:
            indices.append(i)

    print(f"{indices}")


