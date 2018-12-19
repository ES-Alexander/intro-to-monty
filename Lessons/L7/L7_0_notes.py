#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 7                                   #
#        Inheritance, Abstract Classes, Libraries/Packages, Polymorphism       #
#                                                                              #
################################################################################




#--------------------------------- INHERITANCE --------------------------------#
'''
    Object-oriented programming is made considerably more powerful by the usage
    of inheritance. In essence, classes can be based upon, or 'inherit' from
    one or more other classes, implementing and building upon their existing
    properties and methods. This allows for general class types to be created,
    which can then be expanded upon in a variety of different directions. If,
    at a later point, it's desired for two or more of these expansions to be
    combined, a further class can inherit from all the desired classes, and any
    others as well.

    The inheritance hierarchy is referred to using the words 'parent', or
    'superclass' and 'child', or 'subclass'. The former pair refers to the
    class or classes inherited from, and the latter to the inheriting class.
    Often it is desired for each class to inherit from one other class only,
    but sometimes it is beneficial to have multiple inheritance, which is
    direct inheritance from more than one parent class.

    Formally, any child class must at minimum implement everything in their
    parent class(es), so each existing property and method must exist. For
    consistency of use, it is best practice to uphold the specification of any
    parent class methods that are redefined in a child class. This means that
    redefining methods should only ever make their specification tighter,
    resulting in output behaviour that is a subset of the behaviour specified
    as allowable by the function definition in the parent. The major benefit of
    this is that child class instances can then be accepted in the place of a
    parent class instance without issue. In terms of python implementation,
    child classes will register as instances of parent classes, using the
    'isinstance(class, type)' command, so unless you are certain that a child
    class will never be used in the place of a parent, you should uphold
    specifications of all a class's parents in any and all child classes.

    If it is desired for a child class to build upon a parent class method,
    without following the requirements specified by the parent, a new method
    should be defined. This may make use of the existing parent method, but can
    also provide any desired additional functionality. This helps to prevent
    potential issues, and allows for unlimited expansion of class hierarchy.

    By default, any inheriting class automatically implements all methods of
    its parents, but, for instantiable classes, instance variables must be
    specified in the __init__ function. This means all instantiable subclasses
    must re-implement the __init__ function, but any methods which don't
    require changing do not have to be rewritten or redefined - they can just
    be used as they would in the parent class. (Example after next section).
'''




#-------------------- INSTANTIABLE CLASSES WITH INHERITANCE -------------------#
'''
    Inheritance can be applied to both instantiable and non-instantiable
    classes, but is almost exclusively used for the former. For
    non-instantiable classes, inheritance could potentially be used to extend
    someone else's library without having to edit the original.

    Given non-instantiable classes usually don't use inheritance, an example of
    only instantiable-class inheritance is displayed below. For
    non-instantiable classes, the behaviour is the same, but without the
    necessity for instance comparison or initialisation functions, such as
    __init__, or __eq__.
'''



# Single Inheritance:
'''
    This represents the most used case, where each class inherits from only one
    parent class. Note the tightening of specification of some of the parent
    class methods.
'''

class MyParentClass(object):
    ''' A representative parent class.
        All base classes inherit from object. '''
    def __init__(self, var):
        ''' A class for displaying superclass behaviour.
        
        'var' must be an integer greater than 0.
        
        Constructor: MyParentClass(int)

        '''
        self._var = var

    def get_var(self):
        ''' Returns the 'var' parameter of this.
        
        MyParentClass.get_var() -> int

        '''
        return var

    def is_var_valid(self):
        ''' Returns True if self._var is an integer greater than 0.

        MyParentClass.is_var_valid() -> bool

        '''
        return (isinstance(self._var, int) and self._var > 0)

    def __eq__(self, obj):
        ''' Returns True if obj is equal to this.

        MyParentClass.__eq__(obj) -> bool

        '''
        if not isinstance(obj, type(self)):
            return False
        if obj._var != self._var:
            return False
        return True

class MyChild(MyParentClass):
    ''' A representative child class. Inherits from MyParentClass. '''
    def __init__(self, var, var2, var3, *args, **kwargs):
        ''' A class for displaying subclass behaviour.

        'var' must be an integer between 0 and 10, exclusive.
        'var2' must be an instance of MyParentClass.
        
        Constructor: MyChild(int, object)

        '''
        # super and use of *args/**kwargs explained in notes below
        # Every class not inheriting directly from object should use super and
        # both *args and **kwargs in its __init__ method
        super().__init__(var, *args, **kwargs)
        self._var2 = var2
        self._var3 = var3

    def get_var2(self):
        ''' Returns the 'var2' parameter of this.

        MyChild.get_var2() -> object

        '''
        return var2

    def get_var3(self):
        ''' Returns the 'var3' parameter of this.

        MyChild.get_var3() -> object

        '''
        return var3

    def is_var_valid(self):
        ''' Returns True if var is an integer between 0 and 10, exclusive.

        MyChild.is_var_valid() -> bool

        '''
        return (super().is_var_valid() and self._var < 10)

    def is_var2_valid(self):
        ''' Returns True if var2 is an instance of MyParentClass.

        MyChild.is_var2_valid() -> bool

        '''
        return isinstance(var2, MyParentClass)

    def __eq__(self, obj):
        ''' Returns True if obj is equal to this.

        MyChild.__eq__(obj) -> bool

        '''
        if not isinstance(obj, type(self)):
            return False
        if obj._var != self._var:
            return False
        if obj._var2 != self._var2:
            return False
        if obj._var3 != self._var3:
            return False
        return True

class MyChildChild(MyChild):
    ''' Another representative child class. Inherits from MyChild. '''
    def __init__(self, var, var2, var3, *args, **kwargs):
        ''' A class for displaying subsubclass behaviour.

        'var' must be an integer between 0 and 10.
        'var2' must be an instance of MyChild.
        'var3' must be a boolean.
        
        Constructor: MyChild(int, object)

        '''
        super().__init__(var, var2, var3, *args, **kwargs)


    def is_var2_valid(self):
        ''' Returns True if var2 is an instance of MyChild.

        MyChildChild.is_var2_valid() -> bool

        '''
        return isinstance(self._var2, MyChild)

    def is_var3_valid(self):
        ''' Returns True if var3 is a boolean.

        MyChildChild.is_var3_valid() -> bool

        '''
        return isinstance(self._var3, bool)


# ----- NOTE: Implicit Definitions ----- #
'''
    Note that each successive class does not explicitly reimplement aspects of
    its superclass if they do not require modification. This allows significant
    efficiency improvements to creating classes, since each function need only
    be defined once within the inheritance chain to be used by all subclasses
    of the defining class.
'''

# ----- NOTE: Method 'super' ----- #
'''
    The 'super' method is used by a class to refer to its superclass(es). It
    informs python to not check the current instance/class for a specified
    method or property, and instead checks at the next level up. More generally
    if a function or property is not defined in the current instance, python
    will check up through the inheritance hierarchy until finding the first
    occurrence of it, or, if not at all present, raising an error. This is an
    important part of inheritance, since it allows superclass methods to be
    used within their redefinition in a subclass.

    The 'super' method can also be used for class and static methods, using
    additional parameters. Calling super(type).method(vars) checks for method
    starting at the next class from type in the inheritance hierarchy. This is
    an unbound call, which means it can be used for staticmethods, but can also
    be used for instance methods or class methods if self or a class are passed
    in as the first variable in vars. Using super(type, type2).method(vars)
    allows for calling classmethods of type2 (or higher in the hierarchy), but
    only works if type2 is a subclass of type. Finally, super(type,
    obj).method() (often used as super(type, self).method()) allows for
    checking instance methods but skipping to check from the specified class
    type (e.g. checking starting from a grandparent instead of a direct
    parent). In this case, obj must be an instance of type (or an instance of a
    subclass of type).

    Once a superclass method has been called, all variables and methods
    referenced within it are first checked for in the current instance, NOT the
    superclass. For example, consider a superclass which implements methods
    add_to_var, and update_var, where update_var calls add_to_var internally.
    If a subclass reimplements add_to_var, the subclass version of add_to_var
    will be used for any subclass object, even when calling
    super().update_var().

    Care must be taken in multi-inheritance situations, where a class has
    multiple direct parents, as explained below.
'''

# ----- NOTE: Multi-Inheritance + Method Resolution Order (MRO) ----- #
'''
    Multi-inheritance calls to super give preference in the inheritance
    hierarchy in the order parent classes are provided in the definition of a
    subclass. Where superclasses share a parent, the shared parent will be
    preferenced after the last parent class which has it as a parent (e.g. with
    classes A(object), B(A), C(A), D(object), E(B,C,D), the search preferencing
    order for a super call in E occurs as B,C,A,D,object). This is known as the
    Method Resolution Order (MRO), and defines the 'next level up' from each
    class, which technically forms the full inheritance hierarchy. Linking this
    to the super note, calling super() specifies to skip to checking from the
    next class in the MRO, and calling super(type) starts searching from the
    first class AFTER type. The search order can be checked by a class's
    __mro__ property, or in the Method Resolution Order section at the start of
    help(ClassName). The recombination in a subsubclass, of two or more
    subclasses inheriting from the same superclass can be visualised as a
    diamond, and is known as the diamond problem.
'''



# MRO + super
'''
    As with single-inheritance cases, if B or C override a method in their
    parent A, the method used will be the overriding method, the first detected
    in the MRO. If both B and C override the method in A, and also both call
    super(), then the super call in B will run the function from C, and the
    super call in C will run the function from A (following the MRO). This
    means a chain of methods can be formed, if super is used in all of them. It
    also means that if a method of the desired name is found, but does not call
    super, the super chain ends there. In the case where C calls super but B
    does not, the method in C will never be reached, and only the method found
    in B will be run.

    Note that *args is required for allowing additional arguments to be passed
    to later methods in the MRO. Generally if a method is intended to be part
    of a super chain, it should include *args and **kwargs to allow for other
    methods to pass variables through it.

    In the following example, for
    method1:
        E1 = E() [MRO = B,C,A,D]
        -> E1.method1('v1','v2','v3','v4','v5')
        -> super -> B.method1(v1,v2,v3,v4,v5)
            B takes 2 vars (v1, v2), and v3,v4,v5 are in *args
        -> super -> C.method1(v1,v3,v4,v5)
            C takes 2 vars (v1, v3), and v4,v5 are in *args
        -> super -> A.method1(v1,v4,v5)
            A takes 1 var (v1), and v4,v5 are in *args
        -> super -> D.method1(v4,v5)
        -> D prints: 'D: v4 v5'
            super call complete, return to A
        -> A prints: 'A: v1'
            super call complete, return to C
        -> C prints: 'C: v3'
            super call complete, return to B
        -> B prints 'B: v2'
            super call complete, return to E
        -> E1.method1 complete

    method2:
        E1 = E() [MRO = B,C,A,D]
        -> E1.method2('v1','v2','v3')
        -> super -> B.method2(v1,v2,v3)
            B takes two vars (v1, v2), v3 is in *args
        -> super(A,self) -> D.method2(v1,v3)
            D takes 1 var (v1), v3 is in *args (and ignored)
        -> D prints: 'D: v1'
            super call complete, return to B
        -> B prints: 'B: v2'
            super call complete, return to E
        -> E1.method2 complete
'''

class A(object):
    def method1(self, var1, *args):
        super().method1(*args)
        print('A:', var1)
    def method2(self, var1, *args):
        super().method2(*args)
        print('A:', var1)

class B(A):
    def method1(self, var1, var2, *args):
        super().method1(var1, *args)
        print('B:', var2)
    def method2(self, var1, var2, *args):
        super(A, self).method2(var1, *args)
        print('B:', var2)

class C(A):
    def method1(self, var1, var2, *args):
        super().method1(var1, *args)
        print('C:', var2)
    def method2(self, var1, *args):
        super().method2(*args)
        print(var1)

class D(object):
    def method1(self, var1, var2):
        print('D:', var1, var2)
    def method2(self, var1, *args):
        print('D:', var1)

class E(B,C,D):
    def method1(self, var1, var2, var3, var4, var5):
        super().method1(var1, var2, var3, var4, var5)
    def method2(self, var1, var2, var3):
        super().method2(var1, var2, var3)

'''
    Recall the above classes: A(object), B(A), C(A), D(object), and E(B,C,D).

    Note that if D had called super(), errors would have occurred due to the
    object class not implementing method1 or method2. This goes to show that
    super chains should end before object, which can be problematic if it's
    unknown which classes will be inherited from by a subclass. If E had not
    inherited from D, then A's calls to super would cause errors. Given D
    happened to also have a method1 and method2 though, the situation worked
    out. Generally, if a class inherits from object it should not call super()
    as there is no guarantee that another class will come after it in the MRO
    and also implement the required method(s).
'''


# ----- NOTE: Multi-Inheritance + Generations ----- #
'''
    Assuming proper subclass behaviour is defined, inheriting from a class and
    one of its subclasses is unnecessary, since the subclass will already fully
    implement the behaviour of its superclass. Beyond this, inheriting both
    subclass and superclass leads to some ambiguity as to which class's
    specification should be followed.
'''



# Specific Parents
'''
    In general, if two superclasses implement the same method, a subclass
    inheriting from both should, for consistency, implement both
    specifications. In cases where one specification is not fully encompassed
    by the other (e.g. two separate classes with a method of the same name),
    care must be taken to ensure the method of each superclass is only used
    explicitly from that class, to avoid ambiguity. This can be done using
    ClassName.method(self, vars). The class whose method has been used should
    be specified in the docstring of the method in the subclass using it.
'''

class A(object):
    def method1(self, var1):
        print(var1)

class B(object):
    def method1(self, var1):
        print(var1)
        print(var1)

class C(A,B):
    def method1(self, var1):
        ''' Implements class B's method1. '''
        B.method1(self, var1)
    def method2(self, var1):
        ''' Implements class A's method1. '''
        A.method1(self, var1)


# ----- NOTE: Multi-Inheritance and __init__ ----- #
'''
    For ease of multi-inheritance, __init__ method for all classes not
    inheriting from object should include *args and **kwargs as arguments,
    passed on via super. This allows for easier use of __init__ in a super
    chain, as discussed in the MRO + super example above.
'''




#------------------------------ ABSTRACT CLASSES ------------------------------#
'''
    Within the object oriented paradigm, it is sometimes beneficial to declare
    methods and their output specifications without actually implementing them.
    These are known as abstract classes, and they allow a general class
    specification to be formed while allowing the implementation and specific
    output and property values to be dealt with by the subsequent child
    classes. The keyword 'pass' can be used in Python to continue with the
    remainder of the program, and this is often used to allow for later
    implementation of some code.

    While it is possible to create abstract classes by simply specifying the
    abstract nature in the relevant documentation, there also exists an
    abstract class library, which can be downloaded and installed from online.
    This provides a formal set of tags and code which can specify a class as
    abstract, and gives some additional functionality similar to that found in
    languages such as Java for abstract class definitions.
'''



# Abstract Class - No Importing (Generic)
class AbstractExample(object):
    ''' An example abstract class. '''
    def __init__(self, var1):
        ''' An example class intended for building upon in subclasses.

        (constructor method here is not abstract)

        Constructor: AbstractExample(object)

        '''
        self._var1 = var1

    def method_1(self, var):
        ''' Returns and prints a value.

        'var' must be an integer satisfying the relation:
            12 <= var <= 123

        (Abstract method is specified but not implemented here)

        AbstractExample.method_1(int) -> int

        '''
        pass


# Abstract Class - w/ Import of Abstract Base Class (abc)
# import relevant aspects of library
from abc import ABC, abstractmethod

# class declared with ABC instead of object
class AbstractExample2(ABC):
    ''' An example abstract class with included usage checks. '''
    # Non-abstract methods are the same (see __init__ in previous example)
    # Abstract methods should use the @abstractmethod tag, but are
    # otherwise the same
    @abstractmethod
    def method_1(self, var):
        ''' Returns and prints a value.

        'var' must be an integer satisfying the relation:
            12 <= var <= 123

        (Abstract method is specified but not implemented here)

        AbstractExample2.method_1(int) -> int

        '''
        pass




#----------------------------- LIBRARIES/PACKAGES -----------------------------#
'''
    One of the significant benefits of using a popular programming language is
    the extensive amount of code which other programmers have already written
    and shared online. This allows for significant reduction of work for the
    vast majority of coding projects, and it is sometimes possible to find that
    almost the entirety of the code needed for a project is readily accessible
    from external sources. Given the benefits of accessing shared code, and in
    time sharing your own code, it makes sense to have an easy way to package
    code.

    Similar to the way libraries are collections of knowledge and information,
    of varying levels of utility, python has its own libraries of code. Some
    libraries are compiled using more efficient programming languages for the
    computer to read (low-level programming languages), and they exist as
    freestanding libraries of code which can be imported and used as desired.
    When python code is collected and distributed, however, it can be described
    as modules and packages.

    A module in python is technically any python file, although usually code is
    only referred to as a module if it is part of a package. Packages are
    essentially folders of python files, which can be nested inside one
    another, and allow for structured collections of code with similar
    functionality or purpose.

    To make a package requires only a folder with one or more python files in
    it, as well as a file called '__init__.py', which provides the
    initialisation code for a particular package when it is imported. Many
    packages require no separate initialisation, in which case the __init__.py
    file is still required, but it can be left empty. Generally it is good
    practice inside the __init__.py file to specify a variable called __all__,
    which is a list of the names of all the files in the package that are
    intended to be imported when a user asks to 'import all' the files of the
    package.

    When multiple packages are nested it can be valuable to make intra-package
    references throughout the structure. Deeper levels of nesting can be
    imported normally, and imports from higher levels of nesting than the
    current one use preceding dots for the number of folders up the structure
    are desired. This works as long as each folder in the package structure
    contains its own '__init__.py' file, and an example is provided below.
'''



# Intra-package Referencing
    # lower down the hierarchy (further nested)
    from folder1.folder2.file import function1, variable1, function2

    # higher up the hierarchy ('super' imports, less nested)
    from . import * # import all from one folder above the current one


# ----- NOTE: Additional Information ----- #
'''
    For additional information regarding python packages and modules, the
    official documentation of python, found online, covers in-depth examples of
    how to create packages and how to perform relative imports. This can be
    accessed at the following link:

    https://docs.python.org/3/tutorial/modules.html
'''




#-------------------------------- POLYMORPHISM --------------------------------#
'''
    Polymorphism in a programming language is the ability for functions to
    optionally accept multiple types of input. Python is implicitly polymorphic
    in that functions are not required to specify the type of input variables
    they accept, and python does not check the type of inputs to a function
    when running a program. This generally makes for simpler coding, but also
    means that if an input of an invalid type for a function is used, the
    program can sometimes throw an error and stop execution.

    Python's implicit polymorphism also comes with benefits, however. Robust
    python programs will often check for the type of input variables, which
    means valid variables are passed, and effective error handling can be used
    to present users with error messages informing them of allowable input
    types and why their input was invalid. Additionally, some different
    hardware types have different amounts of memory assigned to different
    variable types. This can be problematic if code is explicitly written to
    only allow, for example, numbers of a certain size, but a python program
    can instead allow a function to accept any size of the same variable and
    the program interpreter abstracts the memory considerations away from the
    programmer.

    To ensure users are able to input valid inputs to a function, if variables
    of a certain type are required they can be specified in the docstring (the
    documentation) of the function, as has been presented in the course thus
    far.
'''


# ----- NOTE: Docstring ----- #
'''
    The docstring in a python function is the documentation/specification at
    the top, that comes directly after the line where it is named (between the
    triple quotation marks).
