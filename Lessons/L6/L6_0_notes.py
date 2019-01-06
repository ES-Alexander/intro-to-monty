#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 6                                   #
#             Object Oriented Programming, Classes, Encapsulation,             #
#                    Class and Static Methods and Variables                    #
#                                                                              #
################################################################################




#------------------------- OBJECT ORIENTED PROGRAMMING ------------------------#
'''
    So far we've focused on the basic building blocks of a program, such as the
    data being stored and functions which take inputs and perform some action
    based on that data. Intuitively, the progression of these is to link data
    with functions intended to act on that data. This introduces the idea of
    programming with objects, whereby each object has its own properties, and
    those properties can be acted upon or retrieved using object-specific
    functions, called 'methods'. This style of programming is known as
    'object-oriented-programming' (OOP), and is increasingly popular due to its
    increased readability and ease of understanding, particularly in complex
    systems involving multiple parts, or even just copies of the same object.
'''



# A car
'''
    Take, for example, a simple car. A car may have some properties, such as a
    brand, distance travelled, age, colour, current speed, and so forth. From
    these, someone may wish to interact with the car, for example by
    accelerating to change the speed, or getting a paint job to change the
    colour. While it's possible to keep variables for each of these things in a
    particular file, and create relevant functions to change them, without some
    sort of linking structure it can be very easy to get confused, or end up
    with problems differentiating different vehicles. How can you tell which
    vehicle is which? Do you need a separate function for red_car_accelerate()
    and blue_car_accelerate()? What happens if you want to model thousands of
    cars, each with their own separate set of values for each property?

    Object-oriented programming enables the programmer to bypass these issues,
    and provides a definitive structure to answer the questions posed.
'''




#----------------------------------- CLASSES ----------------------------------#
'''
    Python's implementation of this is the 'class'. Linguistically this makes
    some sort of sense, since the differentiation between an object and a class
    of objects is when it's decided that the current level of detail, in terms
    of properties and methods, is as specific as desired. This leaves open the
    possibility for future extension, for example that from vehicle to cars,
    trucks, etc., which will be covered in greater depth in the 'inheritance'
    lesson. Each class can have an unspecified number of 'instances', and each
    instance has its own version of that class's properties, and the same
    methods, known as 'instance variables' and 'instance methods' respectively.
    This follows the fundamental programming mindset of only writing each piece
    of code once, particularly when using it in multiple occurrences.

    Of course, not all grouping of data and/or methods has to be understood as
    an object. Sometimes it's simply beneficial to have methods grouped
    together, or just a set of properties, and these are discussed more in the
    'Class and Static Methods' section below.
'''



# Instantiation
'''
    To begin with, using a class as an object requires that it be possible to
    create an instance of the class. This, in turn, requires what's called an
    'initialisation method', which python calls __init__. In the initialisation
    method, the programmer specifies any initialisation that needs to be run
    when a new instance of that object is created. This could include setting
    user-specified or default values of instance variables, or starting an
    input-checking function if the object requires regular input, and so on and
    so forth.

    All base-level classes in python are based off the 'object' class, and to
    start with all our classes will take the form of 'class ClassName(object)'.
    The ClassName is in upper-camel-case, with the start of each word
    capitalised. Take note of the comment structure, since this helps make
    classes understandable in terms of what they do, without necessarily
    needing to read or understand how they are actually implemented.

    The example below provides the instantiation code for a simple example
    class, and how to create an instance of it.
'''

class Example(object):
    ''' An example class. '''
    
    def __init__(self, param1, param2, etc):
        ''' The class used for providing an example of a class.

        Extra detail here.

        Constructor: ExampleClass(str, int, etc)
            
        '''
        self._param1 = param1 # instance variables (use inside instance methods)
        self._param2 = param2
        var1 = 1 # local variables (only accessible in this function)
        print(var1)


my_example_instance = ExampleClass('test', 3)


# ----- NOTE: Underscores ----- #
'''
    The double underscores of the __init__ function are important, and these,
    along with the '._' parameter prefixes will be covered in the Encapsulation
    section below.
'''

# ----- NOTE: 'self' Parameter ----- #
'''
    The 'self' parameter enables a class to have class-specific instance
    variables and methods, where an instance of a class knows that it is
    itself, and as such has access to any properties that are part of itself.
    Instance methods (those that have 'self' as the first argument of their
    definition) can then have access to all other instance methods and
    properties. Beyond this, if a class initialisation requires certain
    variables to not be accessible outside the initialisation, they can simply
    be named as normal variables, with the 'self' left off. This results in a
    locally-defined variable only defined within the initialisation function.
'''



# Representation
'''
    One of the most important aspects of debugging a piece of code is
    understanding what you're dealing with. In the case of OOPs, where it's
    possible to have multiple objects of the same type, but with different
    properties, the 'type' function is no longer sufficient to differentiate
    objects. It can still, however, provide a very quick overview of what kind
    of object something is, but no further information is given. To deal with
    this, it's important to implement a formal representation for any
    instantiable class, and beneficial to implement a human-readable string
    representation as well. This is done by defining the __repr__ and __str__
    methods, which can be accessed by simply entering an object into the
    console/IDLE, or printing it respectively.

    As an extension the the string formatting presented in lesson 5, using !r
    and !s as part of the format specifiers returns the __repr__ and __str__
    method of each variable specified as such. These should always be used in
    the __repr__ and __str__ methods you define, to make best use of existing
    class behaviours.

    Examples of each of these methods is provided below. Note the indentation,
    since these methods are within a class definition.
'''
    def __repr__(self):
        """ A formal representation of the class instance.

        Evaluating the returned string from a repr function should return a
            copy of the current class instance.

        self.__repr__() -> str

        """
        # A descriptive and functional repr format (param1 and param2 are
        # representative of the names of the inputs the class takes when
        # creating a new instance).
        return "ClassName(param1={0!r},param2={1!r})".format(self._param1,
                                                            self._param2)

    def __repr__(self):
        """ A formal representation of the class instance.

        self.__repr__() -> str

        """
        # A purely functional repr format
        return "ClassName({0!r},{1!r})".format(self._param1, self._param2)


    def __str__(self):
        """ A human-readable representation of the class.

        self.__str__() -> str

        """
        return "ClassName:\n\tParam 1: {0!s}\n\tParam 2: {1!s}".format(
            self._param1, self._param2)


# Equality
'''
    Another very common method to define in a class is the __eq__ method, which
    allows a programmer to check for equality between two objects. An entire
    lesson could be written just on how to check for equality, but the general
    requirements are to ensure both objects are of the same type, and that all
    the relevant instance variables are equal. Relevance here is defined by the
    programmer of the class, but in most cases any and all instance values are
    compared in an equality check. This helps to ensure that an equality check
    of two objects does not hold true if those objects are not effectively
    equal.
    
    Note the importance of checking the type first, since if the checked object
    is of a different type, attempting to check parameter equality may raise an
    error if a checked parameter is not present in the checked object.

    In terms of equality, 'this' refers to the object whose equality function
    is being called. 'obj' is the generally used reference for the object being
    compared to.

    Equality functions are callable using the '==' operator, with an example
    equality function presented below. Note that this is different to checking
    with the 'is' keyword, which explicitly checks if two objects are in the
    same place in memory, as opposed to checking if they are effectively the
    same. Additionally, it is worth noting that the '==' operator checks the
    __eq__ method for both 'this' and 'obj' in the comparison. These should
    ordinarily return the same thing, but occasionally with inheritance,
    discussed in the next lesson, the two equality functions can have different
    results, in which case it is generally preferable to be certain if the
    objects are not equal, rather than assuming they are if just one of the
    equality functions returns true.
'''

    def __eq__(self, obj):
        """ Returns True if this is equal to obj.

        self.__eq__(object) -> bool

        """
        if not instance(obj, type(self)):
            return False
        if self._param1 != obj._param1:
            return False
        if self._param2 != obj._param2:
            return False
        ...
        if self._paramN != obj._paramN:
            return False

        return True


# ----- NOTE: Not Equal ----- #
'''
    The specified function for the 'not equals' operator (!=) is __ne__, and is
    most commonly defined to return 'not self == obj', for both simplicity and
    consistency of definition.
'''




#-------------------------------- ENCAPSULATION -------------------------------#
'''
    Within any class it can be beneficial to have aspects which are hidden from
    the users and the external environment. This particularly applies to data
    which is necessary for the implementation, but which isn't intended to be
    directly accessible to programs using the class. Ordinarily no instance
    variables should be accessed directly, other than in testing. Instead,
    appropriate 'getter' and 'modifier' methods should be written (e.g.
    get_name(), set_colour()), which helps to ensure no 'illegal' or disallowed
    changes are made. This also proves beneficial in the logging of changes,
    since a change-log can be updated each time a modifier method is called,
    whereas direct changes to variables are much harder to track.

    In order to hide instance variables and methods, appropriate syntax is
    using a single underscore '_' as a prefix to the relevant variable or
    method names. This helps other programmers to understand that these
    variables are intended as for implementation-use only. It is worth noting,
    however, that these are still accessible as if they were normal variables
    and methods, and this hiding method relies solely on users understanding
    they're not intended to be directly accessed. The syntax in python to
    actually hide something is a double underscore '__' prefix, as in the
    standard methods mentioned earlier. Standard (builtin) methods used by
    python are denoted with both a prefix and suffix of double underscores, and
    these methods are inaccessible without using the appropriate calling method
    (e.g. == for the __eq__ method, and len(obj) for the __len__ method).

    As a security note, while double underscore prefixing hides variables and
    methods from users, technically they are still accessible at run-time,
    they're just internally renamed within the code (with a leading underscore
    followed by the class name). As such, using double underscore prefixing is
    insufficient to ensure actual data access restriction, and more
    sophisticated methods need to be employed in cases where security is
    required.
'''



# Privacy of Methods and Variables (in a Class)

class Example(object):
    ''' An example class. '''

    def __init__(self):
        ''' The class used for providing an example of a class.

        Extra detail here.

        Constructor: ExampleClass(str, int, etc)
            
        '''
        # Instance variables (specific to this instance)
        # Access using self.var_name from inside instance methods of the
        # class, and obj.var_name from outside the class, where obj is an
        # instance of the class.
        self.instance_var_1 = 'externally accessible instance variable'
        self._instance_var_2 = 'implementation instance variable'
        self.__instance_var_3 = 'private instance variable'

        local_var = 'local variable' # only exists within this function
        print(local_var)

    def func_1(self):
        ''' An externally accessible instance method.

        Access externally with obj.func_1(), where obj is an instance of
            Example.

        self.func_1() -> None

        '''
        return

    def _func_2(self):
        ''' An implementation instance method.

        self._func_2() -> None

        '''
        return

    def __func_3(self):
        ''' A private instance method.

        self.__func_3() -> None

        '''
        return




#--------------- CLASS AND STATIC METHODS (AND CLASS VARIABLES) ---------------#
'''
    Inevitably, grouping data and/or functions isn't always best performed
    using instances. Classes also allow for grouping data as library modules,
    or simply grouping a set of functions which logically fit well together.
    This introduces the concept of methods and data defined within or inherent
    to a particular class, but which can be accessed without an instance.

    There are two levels of this, known as 'class' and 'static' methods,
    denoted with '@classmethod' and '@staticmethod' before the relevant method
    definitions. Class methods are linked to the class, and have access to the
    class's internal state (class variables), but don't require an instance to
    be run. In order to have this internal access, class methods must take
    'cls' as an implicit definition, in the same way 'self' is in instance
    methods. Static methods are completely static from the class, and are
    essentially just there because it makes sense to group them with that
    class. As such, they take no implicit arguments such as 'self' or 'cls',
    and perform as a normal function, just called using the class (or an
    instance thereof).

    Class variables are just like instance variables, but with their values
    shared across all instances of the class. If a class variable is mutable,
    modifying it in one instance will modify it for all other instances.
    Usually this is not desirable behaviour, in which case you should use
    immutable values for your class variables, but at times it can be useful.

    The privacy and accessibility notes about underscores in naming (from
    above) also apply to class methods and variables, and static methods. It is
    worth noting that usually these methods and variables are intended to be
    user-accessible, so generally won't have preceding underscores in their
    names.
'''



# Defining Methods
class MyClass(object):
    ''' An example class with static and class methods. '''

    # Class variables (same for whole class/all instances).
    # Access with self.var_name from inside instance methods of the class,
    # cls.var_name from inside class methods of the class, and
    # ClassName.var_name from static methods or from outside the class.
    # Outside the class can also access with obj.var_name, where obj is an
    # instance of the class (if it's instantiable).
    class_var_1 = 'externally accessible class variable'
    _class_var_2 = 'implementation class variable'
    __class_var_3 = 'private class variable'

    @classmethod
    def my_class_method(cls, param1, param2, etc):
        ''' Returns something useful, potentially from the class.

        cls.my_class_method(param1_type, param2_type, etc) -> type

        '''
        pass

    @staticmethod
    def my_static_method(param1, param2, etc):
        ''' Returns something cool, independent of the class.

        MyClass.my_static_method(param1_type, param2_type, etc) -> type

        '''
        pass


# ----- NOTE: Instantiability ----- #
'''
    A class with all class and static methods is, by implication,
    non-instantiable, and as a result requires no __init__ method, which in
    turn implies no other default python class methods should be defined (e.g.
    __eq__, __repr__, __str__).
'''

# ----- NOTE: Calling Methods ----- #
'''
    While class and static methods, unlike instance methods, can be called
    directly from the class, it's also possible to call them from any subset of
    the class, including instances or subclasses.
'''



# Calling Methods
'''
    Consider an instantiable class 'MyClass', with some instance methods, and
    the above class and static methods. Examples of method calling are
    presented below.
'''

MyInstance = MyClass('default')

instance_result = MyInstance.instance_method('test')

class_method_result_1 = MyInstance.class_method('test')
class_method_result_2 = MyClass.class_method('test')

static_method_result_1 = MyInstance.static_method('test')
static_method_result_2 = MyClass.static_method('test')


# ----- NOTE: Class Variable Reassignment ----- #
'''
    Reassigning a class variable for a particular instance will not modify that
    variable for other instances - it will instead create an instance variable
    by the same name as the class variable, which makes the class variable no
    longer accessible to that instance without directly invoking the class
    name. This is explored in the following example.
'''



# Class Variable Modification vs Reassignment
class MyClass2(object):
    class_var = [1,2,3]
    def __init__(self, instance_var):
        self._instance_var = instance_var
    def print_current(self):
        print(self._instance_var, self.class_var, MyClass2.class_var)

M1 = MyClass2('M1')
M2 = MyClass2('M2')
M3 = MyClass2('M3')

M1.print_current() # prints M1 [1,2,3] [1,2,3]
M2.print_current() # prints M2 [1,2,3] [1,2,3]
M3.print_current() # prints M3 [1,2,3] [1,2,3]

M1.class_var[0] = 2
M3.class_var = [4,5,6]

M1.print_current() # prints M1 [2,2,3] [2,2,3]
M2.print_current() # prints M2 [2,2,3] [2,2,3]
M3.print_current() # prints M3 [4,5,6] [2,2,3]


