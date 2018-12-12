# Lesson formatter

files = ['L9'] # The files to make notes from this run


HASHES = ''
BLANK = ' '
TOPIC = 'T:'
EXAMPLE = 'E:'
NOTE = 'N:'
LIST = 'L:'
END_LIST = 'EL:'

def make_lesson_notes_from_file(filename):
    ''' Reads filename and parses into formatted lesson notes.

    Format includes a hash-bordered file-header, along with topic headings,
        example headings, and note headings, with 4, 3, and 3 line spaces
        preceding each respectively.
    Notes and examples have single-line spaces between consequent sets of the
        same type.
        
    make_lesson_notes_from_file(filename.txt) -> str

    '''
    try:
        input_file = open(filename+'.txt','r')
    except Exception:
        input_file = open(filename,'r')
    decoded_file = input_file
    lesson_number = int(decoded_file.readline()[1:-1])
    topics = decoded_file.readline().strip().split(', ')
    notes = decoded_file.read().split('\n')
    format_lesson_notes(lesson_number, topics, notes)
    input_file.close()

def replace_apostrophies(text):
    ''' Returns a string of 'text' with all apostrophes replaced with ASCII.

    replace_apostrophies(str) -> str

    '''
    text = text.replace('‘', '\'')
    text = text.replace('’', '\'')
    return text

def format_lesson_notes(lesson_number, topics, notes):
    ''' Generates a file with the formatted lesson notes.

    format_lesson_notes(int, list[str], list[str]) -> LN_0_notes.py

    '''
    output = open('L{0}_0_notes.py'.format(lesson_number), 'w')
    output.write(lesson_header(lesson_number, topics))
    output.write(format_notes(notes))
    output.close()

def lesson_header(lesson_number, topics):
    ''' Returns a lesson header string from the given parameters.

    Formats to fit in 80 characters width.

    lesson_header(int, list[str]) -> str

    '''
    header_string = hash_line(HASHES)
    header_string += hash_line(BLANK)
    header_string += hash_line('Lesson {0}'.format(lesson_number))
    header_string += hash_line(topics)
    header_string += hash_line(BLANK)
    header_string += hash_line(HASHES)
    return header_string

def hash_line(information):
    ''' Generates a hash-bordered line containing the given information.

    Information can also optionally be HASHES for a full line of hashes, or
        BLANK, for a blank line, or a list of values. List lines longer than 80
        characters long are split to fit within the 80 character limit.

    hash_line(str/list) -> str

    '''
    line = '#'
    if information == HASHES:
        for x in range(79):
            line += '#'
    elif information == BLANK:
        for x in range(78):
            line += ' '
        line += '#'
    elif isinstance(information, str):
        line += center_string(information, 78, ' ') + '#'
    elif isinstance(information, list):
        line = hash_border_list(information)
    else:
        raise TypeError('hash_line only accepts arguments of type str or list.')
    return line + '\n'

def center_string(string, length, symbol):
    ''' Returns the given string with even symbols on either side.

    Preferentially has one additional space before the string, for string of odd
        length.

    space_string(str, int, str) -> str

    '''
    output = ' ' + string + ' '
    symbols = length - len(output)
    if symbols % 2 == 0:
        symbol_string = gen_symbol_string(symbols // 2, symbol)
        return symbol_string + output + symbol_string
    else:
        before_string = gen_symbol_string((symbols // 2) + 1, symbol)
        after_string = gen_symbol_string(symbols // 2, symbol)
        return before_string + output + after_string

def hash_border_list(info_list):
    ''' Returns the formatted list of information in hash-bordered lines.

    Maintains the 80 character width limit.

    topics_line(list[str]) -> str

    '''
    line = '#'
    index = 0
    prev_list_string = ''
    new_list_string = ''
    while(len(new_list_string) < 74 and index < len(info_list)):
        prev_list_string = new_list_string
        new_list_string += ', ' + info_list[index]
        if index == 0:
            new_list_string = new_list_string[2:]
        index += 1
    if len(new_list_string) < 76 and index >= len(info_list):
        # line completely finished
        return line + center_string(new_list_string, 78, BLANK) + '#'
    else:
        # line overflow -> recursive fix
        line += center_string(prev_list_string + ',', 78, BLANK) + '#\n'
        # run again for remainder of the list, until entire list is formatted
        line += hash_border_list(info_list[(index - 1):])
        return line

def gen_symbol_string(num_symbols, symbol):
    ''' Returns a string of symbols with length 'num_symbols'.

    gen_symbol_string(int) -> str

    '''
    symbol_string = ''
    for i in range(num_symbols):
        symbol_string += symbol
    return symbol_string

def format_notes(notes):
    ''' Returns a string of formatted notes, within 80 characters wide.

    format_notes(list[str]) -> str

    '''
    formatted_notes = ''
    previous_status = None
    current_status = None
    for line in notes:
        if line.startswith((TOPIC, EXAMPLE, NOTE, LIST)):
            previous_status = current_status
            if previous_status is not None:
                formatted_notes = formatted_notes.rstrip() + '\n'
                if previous_status is not EXAMPLE and not line.startswith(LIST):
                    formatted_notes += "'''\n"
            

        # skip checks if line is empty outside an example line
        if current_status != EXAMPLE and not line.strip():
            continue
            
        if line.startswith(TOPIC):
            current_status = TOPIC
            formatted_notes += blank_lines(4) + topic_heading(line[2:].strip())
        elif line.startswith(EXAMPLE):
            if current_status != EXAMPLE:
                formatted_notes += blank_lines(3)
            else:
                formatted_notes += blank_lines(2)
            current_status = EXAMPLE
            formatted_notes += example_heading(line[2:].strip())
        elif line.startswith(NOTE):
            if current_status == NOTE:
                formatted_notes += blank_lines(1)
            else:
                formatted_notes += blank_lines(2)
            current_status = NOTE
            formatted_notes += note_heading(line[2:].strip())
        elif line.startswith(LIST):
            current_status = LIST
            formatted_notes = formatted_notes[0:-4]
            formatted_notes += format_text(line[2:].strip(), 2)
        elif line.startswith(END_LIST):
            current_status = previous_status
            previous_status = LIST
            continue
        elif current_status == EXAMPLE:
            count = 0
            for char in line:
                if char == ' ':
                    count += 1
                else:
                    break
            formatted_notes += format_text(line.lstrip(), count//4)
        elif current_status == LIST:
            formatted_notes += format_text(line.strip(), 2)
        else:
            formatted_notes += "\n" + format_text(line, 1)
        if line.startswith((TOPIC, NOTE)):
            formatted_notes += "\n'''"
        else:
            formatted_notes += '\n'
    return formatted_notes

def blank_lines(num):
    ''' Returns a string of new-line characters, num long.

    blank_lines(int) -> str

    '''
    result = ''
    for x in range(num):
        result += '\n'
    return result

def format_text(text, tabs):
    ''' Returns a string of formatted text, within 80 characters wide.

    Text is left-aligned, and leading tabs are maintained. Input is either a
        string of text, or a list of words.

    format_text(str/list, int) -> str

    '''
    tab_text = ''
    for x in range(tabs):
        for x in range(4):
            tab_text += ' '

    text_list = text
    if isinstance(text, str):
        text_list = text.split()
    line = tab_text
    index = 0
    prev_list_string = ''
    new_list_string = ''
    while(len(new_list_string) < (80 - 4*tabs) and index < len(text_list)):
        prev_list_string = new_list_string
        new_list_string += ' ' + text_list[index]
        if index == 0:
            new_list_string = new_list_string[1:]
        index += 1
    if len(new_list_string) <= (80 - 4*tabs) and index >= len(text_list):
        # line completely finished
        return line + new_list_string
    else:
        # line overflow -> recursive fix
        line += prev_list_string + '\n'
        # run again for remainder of the list, until entire list is formatted
        line += format_text(text_list[(index - 1):], tabs)
        return line

def topic_heading(title):
    ''' Returns an appropriate string for a topic heading.

    topic_heading(str) -> str

    '''
    return '#' + center_string(title.upper(), 78, '-') + '#'
    

def example_heading(title):
    ''' Returns an appropriate string for an example heading.

    example_heading(str) -> str

    '''
    return '# ' + title

def note_heading(title):
    ''' Returns an appropriate string for a note heading.

    note_heading(str) -> str

    '''
    return '# ----- NOTE: ' + title + ' ----- #'


if __name__ == '__main__':
    for file in files:
        make_lesson_notes_from_file(file)
    
