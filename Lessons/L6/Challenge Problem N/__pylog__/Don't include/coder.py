# Coder File
from processor import swap, increment


def coder(file, coded_name, incr, extra_list=[]):
    """Creates a coded file based on the .txt input "file".

    Used to code an inputed file, including using values from extra_list
        to add additional complexity.

    coder(file.txt, str.txt/str.py, int, list<(int,int)>) -> None
    """
    original = open(file,'r')
    new = open(coded_name,'w')
    new.write(str(extra_list) + " " + str(incr) + "\n")
    for line in original:
        new_line = increment(line, incr)
        new_line = increment(new_line, incr*incr*5)
        for element in extra_list:
            new_line = swap(new_line, element)
        new.write(new_line)
    original.close()
    new.close()


if __name__ == '__main__':
    coder("coder.py", 'coded.txt', 3,
          [(8,6),(9,6),(10,6),(5,4),(25,40),(13,2),(12,7)])
