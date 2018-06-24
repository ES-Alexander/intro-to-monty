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

    All base-level classes in python are based off the 'Object' class, and to
    start with all our classes will take the form of 'class ClassName(Object)'.
    The ClassName is in upper-camel-case, with the start of each word
    capitalised. Take note of the comment structure, since this helps make
    classes understandable in terms of what they do, without necessarily
    needing to read or understand how they are actually implemented.

    The example below provides the instantiation code for an example class, and
    how to create an instance of it.
'''

class ExampleClass(Object):
    ''' An example class. '''
    
    # Class variables go outside of initialisation code - global to class.
    class_variable_1 = 'I am a class variable.'
    
    def __init__(self, param1, param2, etc):
        ''' The class used for providing an example of a class.

        Extra detail here.

        Constructor: ExampleClass(str, int, etc)
            
        '''
        self._param1 = param1
        self._param2 = param2


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
    variables, where an instance of a class knows that it is itself, and as
    such has access to any properties that are part of itself. This means these
    properties can be accessed in methods outside the initialisation method, as
    long as the 'self' parameter is also included in those methods. Beyond
    this, if a class initialisation requires certain variables to not be
    accessible outside the initialisation, they can simply be named as normal
    variables, with the 'self' left off. This results in a locally-defined
    variable only defined within the initialisation function.
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

    Examples of each of these methods is provided below. Note the indentation,
    since these methods are within a class definition.
'''

    def __repr__(self):
        """ A formal representation of the class instance.

        Executing the returned string should return a copy of the current
            class instance.

        ClassName.__repr__() -> str

        """
        return "ClassName({0},{1})".format(self._param1, self._param2)

    def __str__(self):
        """ A human-readable representation of the class.

        ClassName.__str__() -> str

        """
        return "ClassName:\n\tParam 1: {0}\n\tParam 2: {1}".format(
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
    equality functions returns true. If this is not the desired behaviour, it
    is possible (although ill advised) to directly call the __eq__ method of
    this, accepting obj as its input parameter.
'''

    def __eq__(self, obj):
        """ Returns True if this is equal to obj.

        ClassName.__eq__(object) -> bool

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
    most commonly defined to return 'not self.__eq__(obj)', for both simplicity
    and consistency of definition.
'''




#-------------------------------- ENCAPSULATION -------------------------------#
'''
    Within any class it can be beneficial to have aspects which are hidden from
    the users and the external environment. This particularly applies to data
    which is necessary for the implementation, but which isn't intended to be
    directly accessible to programs using the class. Ordinarily no instance
    variables should be accessed directly, other than in testing. Instead,
    appropriate 'getter' and 'modifier' methods should be written, which helps
    to ensure no 'illegal' or disallowed changes are made. This also proves
    beneficial in the logging of changes, since a change-log can be updated
    each time a modifier method is called, whereas direct changes to variables
    are much harder to track.

    In order to hide instance variables and methods, appropriate syntax is
    using a single underscore '_' as a prefix to the relevant variable or
    method names. This helps other programmers to understand that these
    variables are intended as for implementation-use only. It is worth noting,
    however, that these are still accessible as if they were normal variables
    and methods, and this hiding method relies solely on users understanding
    they're not intended to be directly accessed. The syntax in python to
    actually hide something is a double underscore '__' prefix, as in the
    standard methods mentioned earlier. Standard methods used by python are
    denoted with both a prefix and suffix of double underscores, and these
    methods are inaccessible without using the appropriate calling method (e.g.
    == for the __equals__ method, and len(obj) for the __len__ method).

    As a security note, while double underscore prefixing hides variables and
    methods from users, technically they are still accessible at run-time,
    they're just internally renamed within the code (with a leading underscore
    followed by the class name). As such, using double underscore prefixing is
    insufficient to ensure actual data access restriction, and more
    sophisticated methods need to be employed.
'''



# Class Private and Public Methods and Variables

    self.__private_var = 0 # Private instance variable
    self._implementation_var = 'me' # Instance implementation variable
    self.user_var = True # User accessible variable (uncommon)
    
    def __private_func():
        """ A private function. """
        pass

    def _implementation_func():
        """ An implementation function. """
        pass

    def user_accessible_function():
        """ A normal instance function, intended for outside access. """
        pass




#-------------------------- CLASS AND STATIC METHODS --------------------------#
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
'''



# Defining Methods
class MyClass(object):
    ''' An example class with static and class methods. '''
    @classmethod
    def my_class_method(cls, param1, param2, etc):
        ''' Returns something useful, potentially from the class.

        MyClass.my_class_method(param1_type, param2_type, etc) -> type

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
    turn implies no other default python class methods should be defined.
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

