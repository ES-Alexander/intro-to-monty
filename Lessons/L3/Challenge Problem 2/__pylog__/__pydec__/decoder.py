# Decoder File
from coded.__pydec__.processor import swap, increment

def decoder(file, decoded_name):
    """Returns a decoded file, coded using the "coder" function.

    Creates a new decoded file called "decoded.txt".

    decoder(file(.txt/.py)) -> decoded_name(.txt/.py)
    """
    # opens the file to decode, and overwrites (or creates) the decoded file
    original = open(file, 'r')
    decoded = open(decoded_name,'w')
    # iterates over all lines in the file to decode, noting the line indices
    for index, line in enumerate(original):
        # decoding info found in first line, so treat separately
        if index == 0:
            # set first line as decode_info
            decode_info = line
            # incr is increment used in imported increment function
            # extra_info is the remaining decoding information
            extra_info, incr = decode_info.split(']')
            incr = int(incr.strip())
            extra_info = extra_info.split('(')
            # initialise an empty list for storing swap function tuple pairs
            extra_list = []
            # extract tuple pairs for usage in swap letter function
            for item in extra_info:
                # ignore the split string '['
                if '[' not in item:
                    # remainder of items are in form 'n1, n2), '
                    # strip trailing space, and split by central space
                    # n1 = 'n1,', n2 = 'n2),'
                    n1, n2 = item.strip().split(' ')
                    # split n1 into 'n1', '', and discard empty string
                    n1, waste = n1.split(',')
                    # split n2 into 'n2', ',', and discard comma
                    n2, waste = n2.split(')')
                    # typecase n1 and n2 to integers, and add tuple to list
                    extra_list += [(int(n1),int(n2))]
        # remaining lines can be decoded using info from first line
        else:
            # decode each line stripped of leading and trailing whitespace
            new_line = decode(line, incr, extra_list)
            # add decoded line to 'decoded.txt' file
            decoded.write(new_line)
    # following good practice, close any opened files
    original.close()
    decoded.close()

def decode(line, incr, extra_list):
    """Returns a decoded line using the info in "decode_info"

    decode(str, str) -> str
    """
    # take copy of inputted line (not strictly necessary)
    new_line = line[:]
    # perform relevant swaps from list of swaps, in reverse order to coder
    for i in range(len(extra_list)):
        new_line = swap(new_line, extra_list[len(extra_list)-i-1])
    # perform reversed increments from initial coding function
    new_line = increment(new_line, -(incr*incr*5) - incr)
    # return decoded line with a newline character to finish
    return new_line
