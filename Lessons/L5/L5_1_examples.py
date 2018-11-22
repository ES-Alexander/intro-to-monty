'''
    Write a function which opens and reads a text file of questions, as well as
    opens and writes to a log file, also of txt format, recording the questions
    and answers. These files should be accepted as filenames, as parameters to
    your function. The first questions to be asked should always be "What is
    your name?", and "How old are you?", values for which should be stored as
    appropriate variables, with a formatted string printed after these two
    questions stating 'Your name is __ and you are __ years old.'

    After this, questions can be selected at random from the list of questions.
    Random selection can be accomplished by reading the question file into a
    list (each line is one question), and using the random module to determine
    which index of the list is accessed. No question should be asked more than
    once, and you can assume the question file will not include duplicate
    questions.
'''


def question_asker(question_file, log_file):

    ''' Asks questions found in question file and records answers in log file.

    Asks name and age, then prints a formatted string containing this
    information. Then questions are read from the user-defined question file
    and asked in random order. Questions and answers are written into a log
    file with a user-defined name.

    Both input files are of .txt format.
    '''

    # Ask opening questions; name and age.
    qu1 = 'What is your name?\n'
    name = input(qu1)
    
    qu2 = 'How old are you?\n'
    age = input(qu2)

    print('your name is {} and you are {} years old.\n'.format(name, age))

    
    # Record questions and answers in log file
    write_file = open(log_file, 'w')
    write_file.writelines([qu1, ' :', name, '\n', qu2, ' :', age, '\n'])
    write_file.close()

    # Generate list of other questions
    read_file = open(question_file, 'r')
    list_questions = read_file.readlines()
    read_file.close()

    # Randomly access questions from list, removing the question once asked.
    import random
    write_file = open(log_file, 'a')
    while len(list_questions) > 0:
        index = random.randint(0, len(list_questions) -1)
        qu_ = list_questions[index]

        answer = input(qu_)
        write_file.writelines([qu_, ' :', answer, '\n'])    #record answer

        list_questions.remove(qu_)
    
    write_file.close()
