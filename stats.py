def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def get_num_value(e):
    return e['num']
        
def sort_list_words(chars):
    char_dicts = []
    for e in chars:
        new_dict = {"char": e, "num": chars[e]}
        char_dicts.append(new_dict)
    char_dicts.sort(key=get_num_value, reverse=True)

    return char_dicts