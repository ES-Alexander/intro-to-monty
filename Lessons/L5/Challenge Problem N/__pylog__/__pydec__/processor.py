# Processor File

def increment(line, amount):
    """Returns a new, coded string based off given inputs.

    Increments each letter in a given string by "amount" (alphabetically).

    increment(str, int) -> str
    """
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z']
    punctuation = ["'",'.','}','"','(',',','{',';','[',':','!',']',')',
                   '/','&','$','|','%','^','#','@','*','-','_','=','+',
                   '<','>','\t']
    new_line = ""
    for char in line:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + amount) % len(alphabet)
            new_line += alphabet[new_index]
        elif char in punctuation:
            index = punctuation.index(char)
            new_index = (index + amount) % len(punctuation)
            new_line += punctuation[new_index]
        else:
            new_line += char
    return new_line

def swap(line, index_swap):
    """Returns a new, coded string based off given inputs.

    Swaps the indicated indices in a string, if they exist.
        Otherwise returns the original line.

    swap(str, (int,int)) -> str
    """
    new_line = ""
    if (index_swap[0] < len(line) - 1) & (index_swap[1] < len(line) - 1):
        index0 = index_swap[0]
        index1 = index_swap[1]
        for index, element in enumerate(line):
            if (index != index0) & (index != index1):
                new_line += line[index]
            elif index == index0:
                new_line += line[index1]
            elif index == index1:
                new_line += line[index0]
        return new_line
    return line
