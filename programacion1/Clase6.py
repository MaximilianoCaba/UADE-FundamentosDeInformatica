## ejercicio 9
"""
def generateSubString(string, cant_character_cut):
    cant_character = len(string)
    cut_init = cant_character - cant_character_cut
    cut_fin = cant_character + 1

    return string[cut_init: cut_fin]


string = generateSubString("hola como estas", 3)

print(string)
"""

## ejercicio 6
"""
def filtrar_palabras1(string, max_value_characters):
    words = string.split()
    result = ""

    for word in words:
        if len(word) >= max_value_characters:
            result = result + word + " "

    return result


def filtrar_palabras2(string, max_value_characters):
    words = [word for word in string.split() if len(word) >= max_value_characters]
    return " ".join(words)


string = filtrar_palabras1("hola como estas todo piola", 5)

string3 = filtrar_palabras2("hola como estas todo piola", 5)

print(string)
print(string3)
"""


## ejercicio 7
def is_valid_cut(string, position, cant_cut):
    len_string = len(string)
    if len_string >= position and len_string - position >= cant_cut:
        return True
    else:
        return False


def cut_string_slice(string, position, cant_cut):
    if is_valid_cut(string, position, cant_cut):
        string = string[position: position + cant_cut + 1]
        return string
    else:
        return string

def cut_string_not_slice(string, position, cant_cut):
    if is_valid_cut(string, position, cant_cut):
        string_list = [word for index, word in enumerate(string.split()) if position <= index < position + cant_cut + 1]
        return "".join(string_list)
    else:
        return string


string = cut_string_slice("hola que tal", 2, 2)
string2 = cut_string_slice("que contas", 25, 9)
print(string)
print(string2)



string3 = cut_string_not_slice("hola que tal", 2, 2)
string4 = cut_string_not_slice("que contas", 25, 9)
print(string3)
print(string4)