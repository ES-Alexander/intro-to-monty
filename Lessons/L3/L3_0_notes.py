################################################################################
#                                                                              #
#                                   Lesson 3                                   #
#                     Data Storage, Iteration, and Keywords                    #
#                                                                              #
################################################################################




#-------------------------------- DATA STORAGE --------------------------------#
'''
    In Python, as in many other programming languages, data sets can be stored
    in a variety of data structures; namely, lists, tuples, and dictionaries.
    While it is also possible to create customised versions of these, custom
    data structures ("classes") will be covered in greater depth in later
    aspects of the course.

    Once data has been stored in one of these variable types, to retrieve it
    requires indexing, which, in Python, is performed using square brackets.
    Both lists and tuples use numerical indexing, where items are stored in a
    specific order, and referenced by their place within that order.

    Dictionaries instead form a form of data map, whereby each value in the
    dictionary is referenced by a specified key. Keys can be of any data type
    which can't be changed*, but each key can appear at most once in a
    dictionary. Values are free to be repeated as desired.

    It is worth considering what happens when attempting to reference an index
    or key which is outside the range of a given variable. In this case Python
    will throw an error, which ordinarily stops the running of your code. To
    avoid this, it is worth checking beforehand that the specified index is
    within the list/tuple (if <index> < len(list_name): ...), or that the
    specified key is in fact registered in the dictionary (if <key> in
    dict_name: ...). Additionally it is possible to use the mod (%) operator
    to simply start the count again from the other end of the list.

    Definition examples of all three data types were provided in lesson 1, but
    with the exception of tuples it's possible to add additional data after the
    initial definition. For lists this is done using
        list_name += [<list of items>],
    and for dictionaries this is done using
        dict_name[<key>] = <value>.
    Individual elements of a list can also be changed using
        list_name[<index>] = <value>,
    but ONLY if the index is within the existing length of the list.

    Additional useful commands for lists and dictionaries can be accessed using
    the 'help' function, or by searching online. 
    

    * These data-types are known as 'immutable', and consist of Strings,
        integers, floats, booleans, and tuples. Once these are defined, they
        cannot be changed or altered.
'''



# Defining a list, adding a value, and safely accessing an item at an index
my_list = [1, 'test', 6]
my_list += ['tree', ['does','this','work?'], 'yes']
if 5 < len(my_list):
    my_list[5] = 'does it really?'
    # print a string version of element 4 of my_list
    print(str(my_list[4]))
# alternatively,
print(str(my_list[5 % len(my_list)]))

# Defining a dictionary and a tuple, using the tuple as a key and value, and
# accessing a value
my_dict = {'key' : 'value',
           1 : 'test',
           2.3 : 34}
my_tuple = ('1 string', True, 5, 3,2)
my_dict[my_tuple] = 'tuple_key_value'
print(str(my_dict[2.3]) + ', ' + str(my_dict.get('key')))
           



# ----- NOTE: Numerical Indexing ----- #
'''
    Numerical indexing in the majority of programming languages begins at 0, so
    the first element of a list is accessed using list_name[0], with subsequent
    items referenced with higher numbers. 
'''

# ----- NOTE: Item Ordering ----- #
'''
    While items in lists and tuples are explicitly ordered due to their
    indexing, the mapping of dictionaries does not guarantee any specific
    ordering of the keys and/or values - just that each key matches its
    specified value. This means that accessing all of a dictionary's keys or
    values using dict_name.keys() or dict_name.values() may result in lists that
    are not in the order you put the key-value pairs into the dictionary. As
    such, if ordered accessing is required, it can be worth making a separate
    list/tuple containing the dictionary's keys in the desired order.
    Alternatively the keys can be made as some specific type which can by
    process of counting or similar yield the desired order.
'''




#---------------------------------- ITERATION ---------------------------------#
'''
    Once a data storage variable has been created, a logical extension of that
    is accessing all or some subset of it and applying code based on that. To
    do this we iterate over the variable, via loops.

    The two main types of loops in programming are called 'for' and 'while'
    loops. A for loop continues for the duration of some specified condition,
    and can iterate using individual stored elements, whereas while loops
    iterate until some end condition, and the iteration process does not involve
    keeping track of any particular variables other than in checking if the
    end state is satisfied.

    For loops tend to be more appropriate for iterating over a specific object,
    or when the desired number of loops is known, whereas while loops are
    generally more applicable for a specified end condition which depends on
    potentially unknown changes occurring within the loop. Any loop which can
    be created as a for loop is technically also able to be created with an
    equivalent while loop, and vice versa, so use whichever loop type seems
    most appropriate and easiest to implement for the task at hand.
'''

# A simple for loop iterating over a list
my_list = [1,2,3,4,5]
for item in my_list:
    print(str(item))

# A more advanced for loop, keeping track of items and their indices
my_list = [1,2,3,4,5]
for index, item in enumerate(my_list):
    print('Index: ' + str(index) + ', Item: ' + str(item))

# A for loop iterating over a count
stop_value_plus_one
for count in range(stop_value_plus_one):
    print(count)

# An equivalent while loop
count = 0
while count < 5:
    print(count)
    count += 1

# A while loop based off some other condition
changing_variable = 36
while (changing_variable > 0) or (changing_variable < -30):
    changing_variable = -1.8*(changing_variable/2)
    print(changing_variable)
    

# ----- NOTE: Infinite Loops ----- #
'''
    It is very common in programming to accidentally create an issue with a
    loop such that it never reaches its end condition (an infinite loop). In
    these cases the program can usually be stopped by pressing CTRL+C on the
    keyboard (same on PC and Mac), or if necessary by closing the application
    entirely and reopening it.

    This is highly undesirable, so wherever possible infinite loops should be
    avoided, unless the programmer is certain that that's the desired behaviour.
'''




#---------------------------------- KEYWORDS ----------------------------------#
'''
    Along with a number of inbuilt functions, python comes with a set of
    keywords used to help perform a number of desired coding solutions. Keywords
    come up as orange in the default IDLE colour settings, and you may have
    noticed some already as we've used a number up to this point. The more
    common of these are listed below, with a basic explanation as to when
    they're used and why. Additional keywords can be found by searching online,
    or by importing the 'keyword' library, and printing 'keyword.kwlist'.
    
        - Boolean values ('True', 'False')
            Used to specify booleans
        - A non-existent value ('None')
            Often used as a filler when values don't exist
        - Logical operators ('or', 'and', 'not')
            Used in conditional specifications
        - Conditional specifiers ('if', 'elif', 'else')
            Used to specify the start of a conditional block (of code)
        - Data checkers ('in', 'is')
            'in': checks if a container object contains a value which == the
                checked value (before the word in)
            'is': checks if two objects are literally two references pointing
                to the same place in memory (not necessarily just a == b)
        - Iteration specifiers ('for', 'while')
            Used to specify the start of a loop or iterable block
        - Loop modifiers ('break', 'continue')
            'break': exits the current loop block (only one layer in a nested
                loop)
            'continue': skips to the end of the current loop in a loop block
        - Importing words ('import', 'from', 'as')
            Used to import libraries and data/variables from other files
        - Exception words ('try', 'except', 'finally')
            Used in dealing with exceptions thrown while the program is running
        - Defining words ('def', 'class')
            Used to defined functions and classes respectively
        - Function returning ('return')
            Used to immediately end a function, optionally returning a value
        - Blank filler ('pass')
            Used as a filler for when an indented block is required but no
                effect is desired. Nothing occurs when 'pass' is run.
'''

