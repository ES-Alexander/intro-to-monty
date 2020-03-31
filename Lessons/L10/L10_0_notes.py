#!/usr/bin/env python3
################################################################################
#                                                                              #
#                                   Lesson 10                                  #
#                         Code Testing and Repositories                        #
#                                                                              #
################################################################################




#-------------------------------- CODE TESTING --------------------------------#
'''
    'Correct performance' in programming is determined by specification.
    Testing your code allows you to determine where bugs are in your program,
    and also where the specification is not being met. Sometimes a
    specification calls for behaviour which isn't logical, or even isn't
    possible, in which case testing can help you find out which aspect of the
    specification needs changing.

    So far, most of your own testing of code will fall under what's known as
    'exploratory testing'. This is testing where you run some code and try to
    check that features behave as expected and desired. Often exploratory
    testing is done using print statements throughout your code, as well as
    creating instances and running functions on some basic inputs, and seeing
    if the result seems to make sense. While this is great for testing small
    bits of a program, or finding out where a particular error originates, it
    becomes difficult to maintain with larger programs.

    As your programming gets more complicated, and incorporates more features,
    it can become difficult to keep track of what is and isn't working. What's
    more, sometimes fixing one bug can cause a bug in another part of your
    program that might be hard to notice or pick up. This is where automated
    testing comes in. You consider your specification and determine a set of
    inputs (known as 'test cases') to cover every aspect of your program's
    functionality. Creating such a test suite means you can provide your code
    to users with a guarantee that if used within the specification, as tested
    by your tests, your code will perform correctly. This also means that every
    time you modify your program you can test all its specified behaviour, and
    check that it performs correctly, without you having to remember or
    manually implement all the test cases. Many professional and open-source
    programming projects are made with a 'test first' mentality, whereby you
    write your test cases for your functions before you write the functions
    themselves. This forces you to consider the types of inputs and outputs you
    are dealing with, and the functionality you want, which also lends itself
    to writing clear documentation. Additionally, with the tests already
    written it is easy to check which components you have implemented correctly
    as soon as you write them, which means bugs get found as you write your
    code, instead of being hard to find at the end.

    The ideal case in testing is to literally test every possible input and
    respective output behaviour for your program. For some programs, with
    highly specific input requirements, this is possible and not unreasonable
    to do. For most programs, however, this is quite unrealistic, and often not
    possible within a reasonable time frame. Instead, tests should cover
    representative cases, whereby a few tests displaying the expected behaviour
    suggest that the implementation is likely to be correct. As you get more
    experienced with testing, which cases should be representative will become
    more obvious, but to start with try to test any and all possible edge
    cases, along with one or more cases of general input (e.g. a function
    accepting integers between -10 and +10 could be tested at -10 and 10, and a
    random value between -9 and 9). For greater certainty, once the edge cases
    have been tested, a function can potentially be tested multiple times with
    random inputs in its accepted range (e.g. run it 10000 times with random
    inputs), if its correct output can be predicted with some other function
    (perhaps a less efficient but proven correct implementation).
'''



# Unit and Integration Tests
'''
    Once the desired test-cases have been identified, the tests themselves must
    be written. Testing can be comprised of 'unit' or 'atomic' tests, which
    test one test-case each, and 'integration' tests, which may test multiple
    test-cases in the same test function, either passing all of them, or
    stopping at the first failure or error. Unit tests are generally more
    helpful when determining where exactly a problem is occurring, but will
    often take longer to write and implement than integration tests.
    Additionally, some test-cases which have their functionality implemented
    late in a function are likely reliant on other test-cases passing. This
    means several unit tests might fail due to a single error, which can give a
    sense of how important an error is, but can also make it difficult to
    determine the cause if you're unaware of the dependencies between the tests.

    The ideal test suite is one with minimal time spent writing and creating
    it, and the quickest results when debugging to find the cause of an issue.
    When writing integration tests, make sure to have them test related test
    cases, and try to have helpful error messages for every test-case which is
    tested.
'''


# Black Box Testing
'''
    Black box testing is known and used across a variety of industries, largely
    due to its effectiveness and broad applicability. To apply black box
    testing, your program should be treated as a black box, testing only the
    allowed inputs with the expected output, in accordance with its
    specification. Generally a program will have some general specification,
    with each function and/or class containing smaller parts of this
    specification in its documentation. If the documentation can be shown to
    correctly and fully represent the original specification, then testing can
    be applied to test against the program documentation. This has the benefit
    of being more specific than the general specification, so more test cases
    can be provided that test different test cases, as opposed to just doing
    more tests of the same general test case.

    A tradeoff must sometimes be made between testing and robustness. The more
    robust an application is supposed to be, the more it should be tested to
    make sure of its robustness. Conversely, the more a program has been
    tested, the more robust it can be assumed to be. If a robust function
    claims in its documentation that it returns -1 on any invalid input, care
    should be taken to ensure that this is indeed the case for all manner of
    invalid inputs. If, instead, a less robust function simply specifies a set
    of valid inputs, behaviour for invalid inputs cannot be tested against, and
    is not guaranteed to stay the same through different versions of the code,
    even if the specification doesn't change.

    Sometimes a function's documentation is quite broad, and difficult to
    determine specific test cases for. This is particularly the case for
    functions which are intended to have random behaviour, or to behave
    according to some statistical distribution. If applying black box testing
    to these it may be necessary to return probabilistic results, with some
    measure of certainty, as opposed to the normal pass-fail test behaviour.
    Mapping the behaviour to a statistical distribution generally requires
    running thousands or even millions of tests to see where the output falls,
    and with what kind of consistency. Alternatively, the intention of the
    programmer, through their implementation, can be tested using white box
    testing.
'''


# Black Box Example
'''
    Below we have the docstring for a factorial function, from an example in
    lesson 8. Recall that n! = n * (n-1)!, and that 0! = 1.
'''

def factorial(n):
    ''' Returns the factorial of n (n!) if n is valid, else returns -1.
    
    'n' must be a non-negative integer to be valid.

    Works up to at least n = 500.

    factorial(int) -> int

    '''
    pass

'''
    Treating this function as a black box, we know that valid inputs should be
    integers, between 0 and some value above 500, inclusive. The specification
    mentions that -1 is returned for invalid inputs, so it can be assumed that
    if 'n' is not an integer, or is a negative integer, or is an integer above
    the maximum working value, -1 should be returned. From this we can build up
    a set of representative test cases to test the specification, as below:

    N         EXPECTED OUTPUT      REASON FOR TEST
     0         1                    Edge case (min valid int)
     1         1                    Edge case (min valid int with non-explicit 
                                               result)
     500       500!                 Edge case (max guaranteed valid int)
     >1        n!                   General case (valid int)
     -1        -1                   Edge case (max invalid int below 0)
     <-1       -1                   General case (invalid int below 0)
     not int   -1                   General case (invalid type, not int)
    
    It may also be beneficial to find the largest valid input, and to check
    that any inputs above this value do indeed return -1. This can be done as
    an integration test, testing each integer input above 500 until -1 is
    returned, or an incorrect result is provided. In this case, the inbuilt
    python math library has an implementation of factorial, which we can assume
    to be correct. Without using this, we could still make a weak test by using
    our knowledge of the specification to note that each result for a larger n
    should be larger than the previous result. If this holds until the outputs
    start becoming -1, we at least have some reasonable belief that the
    function is likely to be working as specified.
'''


# White Box Testing
'''
    While black box testing treats a program as an impenetrable device which
    can only be studied from input-output behaviour, white box testing opens
    the box and tests directly against how the program is implemented*. This is
    generally an extension to black box testing, and can yield a number of
    additional test cases which are significant to the program implementation,
    but not necessarily to the specification itself. Depending on how robust an
    application needs to be, and how much time and budget is available for
    testing, white box testing may or may not be desirable for your application.

    To start with, black box test cases should always be identified first.
    White box testing may identify unnecessary black box tests, but white box
    edge cases may be outside the specification, whereas black box edge cases
    test at the specification limits. This helps to ensure that at the least
    the specification is tested against for a seemingly representative set of
    test cases, and there is some guarantee that can be made about the program
    being correct. From here, the implementation should be studied to identify
    every possible branch (if/else/loop) point, and build up a full set of
    possible input and output sets that the program should accept and produce.
    These should then be tested in the same manner as specification tests,
    checking edge cases and some general tests.

    White box tests should be treated as temporary, in the sense that they are
    only guaranteed to cover the implementation use-cases while the program
    remains in its original form. Any implementation change means the white box
    test cases could now test redundant cases, and miss new implementation
    details. The tests should still at least be valid 'general case' tests
    however, so long as the specification remains the same. When a program's
    specification is modified, both black box and white box tests may no longer
    be valid. Luckily, this is generally much less frequent than changes of
    implementation, and some tests may still be valid, or at least require only
    minor modification.

    * Testing against how the program is implemented involves using the
    implementation to determine important input values. The output resulting
    from these inputs should be tested against the specification, not against
    what it looks like the result would be.
'''


# ----- NOTE: White Box Loops ----- #
'''
    Loops in white box testing often provide a number of additional test cases.
    This is because to prove that a loop behaves as desired it must be shown to
    do so in edge cases (zero loops, one loop, maximum number of loops (if
    exists)), as well as for a general 'n-loops' test case. As with standard
    inputs, the ideal is if every possible case can be tested for each loop,
    but this is often not possible (or practical), particularly for loops with
    branch points inside them. Instead, effort should be made to do an
    inductive proof along the lines of 'if one input works correctly, and two
    inputs work correctly, and the same pattern is followed from there, then n
    inputs should also work correctly.' If such a statement can be made with
    proof, then only a set number of cases are required to be tested to
    effectively check the 'n-inputs' case (in the example statement, it would
    just be the inputs causing one and two loop iterations). Additional tests
    can still be performed in the 'n-loops' region, but these are just for
    peace of mind. Even for relatively simple programs, it is easy to see how
    white box testing can create large numbers of test cases.
'''



# White Box Example
'''
    We now consider the same factorial function, but with its implementation
    visible, as below.
'''

def factorial(n):
    ''' Returns the factorial of n (n!) if n is valid, else returns -1.
    
    'n' must be a non-negative integer to be valid.

    Works up to at least n = 500.

    factorial(int) -> int

    '''
    import sys # used for checking maximum number of recursive calls
    if not isinstance(n, int) or n < 0 or n > (sys.getrecursionlimit()*2)//3:
        # invalid input
        return -1
    elif n == 0 or n == 1:
        # terminating case
        return 1
    else:
        # make recursive call
        return n * factorial(n - 1)

'''
    Looking at the first branching statement, we should check a case where 'n'
    is not an integer, where n is an integer less than 0, and where n is an
    integer greater than 2/3 of the system recursion limit. These three cases
    are representative of the possible invalid inputs, and should all return
    -1. The latter two cases here give us validity limits, which means we can
    also test edge cases for the minimum and maximum values. In the black box
    test-cases, we had no explicit way of testing the maximum, and were
    planning to resort to repeated trials. Here we find that our analysis of
    white-box test-cases has reduced our testing load, because the main
    computationally expensive test-case from earlier is no longer necessary.

    The next branch occurs only if the first three conditions are not met, and
    if n is 0 or 1. As such, we should check the results for n=0 and n=1, for
    which the correct factorial result is 1. The expected output should always
    be with respect to the specification, if defined for that input.

    We now find that any other input results in a recursive call, forming a
    loop. Logically, we can see that this only occurs if n is an integer,
    between 2 and max=(sys.getrecursionlimit()*2)//3 inclusive. For no
    iterations of the loop, we should test the above cases with explicit
    results. For a single iteration of the loop, we should test n=2. For two
    iterations of the loop, we should test n=3. Since each iteration of the
    loop follows a consistent pattern, built upon the previous iterations, if
    the pattern is working for multiple iterations of that loop, it can be
    assumed that the next iteration should also be correct when following the
    same pattern. This in turn implies that all further valid inputs should be
    correct, so testing n=2 and n=3 is representative of testing every possible
    input to the loop. To test the maximum, we should check n=max. As a general
    case, we can test a random value between n=3 and n=max. We can use the
    inbuilt math library's factorial to test these two cases, as the numbers
    are too large to conveniently calculate by hand.

    From here, we build another table of test-cases:

    BRANCH 0 (invalidity)
    N           EXPECTED OUTPUT      REASON FOR TEST
     not int     -1                   General case (not an integer)
     -1          -1                   Edge case (max invalid int below 0)
     <-1         -1                   General case (invalid int below 0)
     max+1       -1                   Edge case (min invalid int above max)
     max+(+ve)   -1                   General case (invalid int above max)
    BRANCH 1 (explicit input value)
    N           EXPECTED OUTPUT      REASON FOR TEST
     0           1                    Edge case (min valid int, explicit result)
     1           1                    Edge case (max valid int, explicit result)
    BRANCH 2 (loop)
    N           EXPECTED OUTPUT      REASON FOR TEST
     2           2                    Edge case (1 loop iteration)
     3           6                    Edge case (2 loop iterations)
     max         max!                 Edge case (max loop iterations)

    We find here that our black box tests are almost fully encompassed by our
    white box tests. The only exception is if max < 500. This still provides
    one necessary black box testing case that isn't guaranteed by white box
    testing, so in general, take care to make sure you're covering all test
    cases. If you are unsure if you should be using one or more of your black
    box tests, implement any you are unsure about, unless doing so would be
    prohibitively expensive or time consuming. This is particularly useful if
    the implementation is likely to change, as you have a number of test-cases
    in place to guarantee the new implementation still matches the
    specification.

    As a positive, our implementation no longer requires testing the general
    case of n>1, and instead can be tested effectively with just n=2 and n=3.
    Often several random tests are performed when testing general regions, but
    loops that have been proven to work have certainty with only a few select
    cases. One or more additional random checks may still be worthwhile for
    peace of mind, but this can be significantly fewer than for a general
    region - particularly if its implementation is unknown.
'''


# Testing in Python
'''
    There are a few established methods of creating and running tests in
    python, including a builtin test library called unittest. Unittest
    unfortunately has a difficult to read output when more than a few tests are
    run. The other main library implementations are used in practice, but will
    not be used for this course. An IDLE-compatible test module can be found in
    the TestRun.py file in the Lessons folder, which has been developed for
    this course. It can also be used for other testing situations, particularly
    where you want a readable output, and don't require significant performance
    optimisation of your testing module. To use TestRun in your own projects,
    you can install it to your computer using pip, e.g. with 'python -m pip
    install testrun'.

    To use this test module, import the TestRun class* from TestRun.py, and
    create your own test class inheriting from TestRun. Test functions should
    be instance methods, should start with 'test_', and should use an 'assert'
    statement as the testing component. The functions should not have a return
    value, but should have a 'reason' provided with the assert, in case it
    fails (see example below). Multiple assertions can be tested in a single
    test function (an integration test), but in this case only the first one
    which fails will be explained in the results. As with normal functions,
    each test function should have an explanatory docstring so the purpose of
    the test can be discovered with help(MyTestClassInstance.test_name). Unlike
    normal methods, the running information for the test methods can be left
    off, as it is automatically set when the class is instantiated.

    Tests can be run individually using the run_test() method, but can also be
    run as a set using run_tests(['test_names']). Both running methods allow
    you to specify a boolean value for 'verbose' (e.g. verbose=True) to
    determine if additional explanation is provided for failed tests. Running
    individual tests has this set to True by default, whereas running a set of
    tests has it set to False, since this provides the cleanest output for the
    first run of tests. If run_tests is run without any arguments, it looks for
    and runs all methods of the class beginning with 'test_'.

    Automatic timeouts are available when not using IDLE, but if a test is
    taking too long you can manually cause a timeout by pressing CTRL+C to
    raise a KeyboardInterrupt. This is particularly useful for if a part of
    your program gets stuck in an infinite loop.

    The module also allows for logging of print and error statements printed to
    the terminal (in both IDLE and other terminals). For a full demonstration
    of all the module's features, including testing printed output, look at and
    run the example at the bottom of the TestRun.py file. Below is a more basic
    example, covering the implementation of the test cases discussed in the
    white-box and black-box testing sections.

    * Recall from lesson 5 that python treats the file being run as the
    top-level file in any hierarchy. As such, even if the file is a low-level
    file within a module, the module is not recognised until run from higher
    up. This can be resolved by manually adding the folder where your import
    file is stored to the path, as in the following example.
'''


# Implementing Our Testing Suite
'''
    We now implement the test cases identified in the white box tests example.

    The following test cases should all pass, because the function correctly
    implements its specification. For an example of possible failure results
    from the testing module, look at the bottom of TestRun.py, and run the file
    to see the outputs. Remember if you're using IDLE there are no automatic
    timeouts, so you'll need to use KeyboardInterrupts (CTRL+C) to cause
    user-generated timeouts where necessary.
'''

# add the parent folder to path because TestRun.py is in Lesson, not L10
import sys
sys.path.append('..')
from TestRun import TestRun

import math
from random import randint

# test definitions
class FactorialTests(TestRun):
    ''' A class of tests for testing a factorial implementation. '''
    def __init__(self):
        ''' Initialise variables for this test suite.

        Constructor: FactorialTests()

        '''
        super().__init__()
        self.max = (sys.getrecursionlimit() * 2) // 3

    # BRANCH 0
    def test_invalid_type(self):
        ''' Testing if factorial(not int) returns -1.

        General case (not an integer (float, str, tuple, list, dict)).

        '''
        for item in [1.3, '', tuple([1]), [1], {1:1}]:
            ret = factorial(item)
            assert ret == -1, "should return -1 on invalid type input, but " +\
                            "returned {}".format(ret)

    def test_invalid_int_negative(self):
        ''' Testing if factorial(-ve) returns -1 (invalid int < 0). '''
        # test edge case, max invalid int below 0
        ret = factorial(-1)
        assert ret == -1, "should return -1 on invalid int below 0, but " +\
                        "returned {}".format(ret)

        # test general case
        for i in range(500):
            ret = factorial(randint(-10000,-2))
            assert ret == -1, "should return -1 on invalid int below 0, " +\
                            "but returned {}".format(ret)

    def test_invalid_int_positive(self):
        ''' Testing if factorial(max+(+ve)) returns -1 (invalid int > max). '''
        # test edge case, min int > max
        ret = factorial(self.max + 1)
        assert ret == -1, "should return -1 on invalid int above max, but " +\
                        "returned {}".format(ret)

        # test general case
        for i in range(500):
            ret = factorial(self.max + randint(2,10000))
            assert ret == -1, "should return -1 on invalid int above max, " +\
                            "but returned {}".format(ret)

    # BRANCH 1
    def test_explicits_valid(self):
        ''' Testing if factorial(0/1) returns 0! = 1! = 1 (explicit result). '''
        # test edge case, min valid int with explicit result
        ret = factorial(0)
        assert ret == 1, "0! = 1, not {}".format(ret)

        # test edge case, max valid int with explicit result
        ret = factorial(1)
        assert ret == 1, "1! = 1, not {}".format(ret)

    # BRANCH 2
    def test_loop_iterations(self):
        ''' Testing if factorial(>1) returns n! (n loop iterations). '''
        # test edge case, 1 loop iteration
        ret = factorial(2)
        assert ret == 2, "2! = 2, not {}".format(ret)

        # test edge case, 2 loop iterations
        ret = factorial(3)
        assert ret == 6, "3! = 6, not {}".format(ret)

        # test general case (not strictly necessary, since proven valid)
        for i in range(100):
            n = randint(4, self.max)
            ret = factorial(n); n_fact = math.factorial(n)
            assert ret == n_fact, "{}! = {}, not {}".format(n, n_fact, ret)
        
        # test edge case, max loop iterations
        ret = factorial(self.max); n_fact = math.factorial(self.max)
        assert ret == n_fact, "{}! = {}, not {}".format(self.max, n_fact, ret)

    def test_max_guaranteed_valid(self):
        ''' Testing if factorial(500) returns 500! (max guaranteed valid). '''
        ret = factorial(500); n_fact = math.factorial(500)
        assert ret == n_fact, "500! = {}, not {}".format(n_fact, ret)

# run tests
Tests = FactorialTests()
Tests.run_tests()




#----------------------- REPOSITORIES (VERSION CONTROL) -----------------------#
'''
    As with all work on a computer, it's important to keep your files saved and
    backed up. This is particularly important for code, since losing recent
    changes could introduce bugs that you don't notice, or remove functionality
    that you've already implemented. Additionally, larger programs are often
    worked on collaboratively, which means you need some way of storing files
    on cloud storage. This also introduces the need to determine which changes
    are desired, and which ones should be accepted, particularly in cases where
    two people have separately tried to modify the same code.

    Repositories (commonly called repos) are the accepted response to these
    needs. They can be private or public, and allow multiple people to work on
    the same project at once, seamlessly 'merging' changes as they occur.
    Repositories are more than this however - they act as version control
    software, and allow you to restore files to previous versions, see
    differences between different versions, and see what changes have been made
    when, and who made them.
'''



# Git and Mercurial
'''
    The most widely used open-source, free repository systems are Git and
    Mercurial, which have mostly similar functionality. Both systems are
    'distributed', in the sense that all contributors to a repository store all
    the information of the repository on local storage (your own computer).
    Each local copy is known as a 'branch', and can retrieve the latest
    external updates with a 'pull', and can publish its own updates to others
    with a 'push'. One branch of the repository (known as the 'master' branch)
    must be hosted on a server to be accessible to contributors. Depending on
    the hosting service, some will allow contributors to perform a 'pull
    request', effectively notifying all other contributors that important
    changes have taken place. This then allows the other contributors to do a
    'pull' as soon as possible, before they start writing code which may
    conflict with the new changes. A hosting service may also allow for
    contributors to submit issues, track ongoing and future projects, and
    create downloadable releases.

    Below you will find the basics required when using a Git or Mercurial
    repository. Note that many of the commands described have several
    additional, undiscussed options, as these have been determined as
    non-essential. To see these options, you can use the 'help' command, as in
    'git help'/'hg help'. Mercurial commands are preceded by 'hg' because Hg is
    the element symbol for mercury, from the periodic table of elements.
'''


# Creating a Repository
'''
    To create your own repository, you can usually create one on the website of
    your hosting server, or initialise a blank one on your computer using the
    'init' command. Popular repository hosts such as GitHub or BitBucket will
    generally allow you to quickly and easily set up a new repository, which
    you can then access and work from on your local computer. If you already
    have Git or Mercurial installed on your device, you can manually create a
    repository from within a terminal/command prompt (CMD) window using 'git/hg
    init'.

    GitHub and BitBucket both offer desktop GUI clients for using their
    repository systems, but this course will focus on the command line
    implementations - it's good to be able to use a terminal to at least some
    degree (see note below).
'''


# ----- NOTE: Using a Terminal/Shell ----- #
'''
    A terminal or shell is essentially a command-line interface (CLI) to using
    your computer - as opposed to the overarching GUI generally available from
    startup. While GUIs provide helpful visual displays, CLIs are able to
    instead offer a set of powerful commands, giving you access to a range of
    functionality options not possible to access from the GUI.

    When using a terminal, commands are space-separated. A few common commands
    are listed below, to help with navigating a terminal window. For reference,
    a 'bash' terminal is commonly used on Unix systems (Linux/OSX/macOS),
    whereas 'CMD' is the Microsoft Windows command prompt. 'both' applies to
    both CMD and bash terminals. Paths in bash are specified as slash-separated
    and start at '/' (e.g. /Users/username/Desktop/filename), and in CMD are
    backslash-separated and start with a drive, at '\' (e.g. C:\Program
    Files\Interesting Program\filename). Paths can also be relative, with a
    single dot (.) referring to the current directory, and two dots (..)
    referring to the directory/folder containing the current one. Tab can be
    used for auto-completion, and pressing tab multiple times will either
    display all available options with the given starting characters (bash), or
    will cycle through them (CMD).

    For Git users on windows platforms, windows installations of Git come with
    their own version of bash (called git BASH), which opens its own shell and
    allows you to use bash commands on windows. It is also possible to run Git
    from CMD, but it may be easier to use git BASH, particularly if you use
    multiple operating systems to develop your programs.
'''



# Common Terminal Commands (Basic Navigating)
'''
    COMMAND TERMINAL USAGE
    cd <path> both Change directory (change folder).
    ls <path> bash List files and directories in <path> directory.
                                if <path> is left blank, uses the current
                                directory. Options include -a for 'all', which
                                shows hidden files, and -l for showing extra
                                information, such as permissions. <path> can be
                                used to specify one or more paths and/or
                                specific filenames.
    dir <path> CMD Similar to 'ls' for bash (above), but with
                                different option specifiers.
    mkdir <path> both Make directory (New Folder), as specified by
                                <path>.
    rm <path> both Remove the specified file(s) at <path>. In bash,
                                using the -r flag and <path> leading to a
                                directory will recursively delete all files
                                inside the specified directory.
    rmdir <path> both Remove the specified directory (folder). In bash,
                                this only deletes empty directories. For
                                deleting a directory and its contents, use rm
                                -r <path> (as above).
'''


# Accessing a Repository (Clone/Fork)
'''
    The hosting server you use determines if you are able to make repos
    private. Both GitHub and BitBucket allow all users to have both public and
    private repos.

    To get access to a repo from a hosting server (ie not one you've created
    locally on your computer), both mercurial and git support the 'clone <URL>'
    command. This downloads the repo to your device, and if you're copying it
    from someone else's account, registers the cloned repo in your name. Some
    hosting servers support a modified version of cloning, using the 'fork'
    command, whereby they actively track the differences between the clone(s)
    and the original repo.

    Cloning allows multiple people to work on the same project simultaneously,
    and can also allow you to create your own separate branches for working on
    different parts of the code without needing to worry about damaging the
    main code until the modifications are complete.
'''


# Using a Repository (Commit/Push/Pull)
'''
    Once you have access to a repository, you can create changes, and track
    them using the 'commit' command. This opens up your computer's default
    editor, and gets you to specify a commit message to say what has changed in
    the files you are committing. Using the -m flag allows you to also include
    the commit message in the command line (e.g. 'git commit filename.txt -m
    "useful commit message"'). If you wish to make all available commits
    simultaneously, swap out filename for the -a flag (e.g. 'git commit -a').

    Whenever you want to provide external access to your work, use the 'push'
    command. If you're working on a repository yourself from multiple devices,
    this will often be every time you commit, or at least every time you are
    about to leave a device. For working simultaneously with others, it's best
    to avoid pushing until you have code which works. Instead track changes
    with regular commits, and only push once your changes have been tested.

    If you're using a repo for simultaneous work, and want to keep up to date
    with the latest changes (from others or from other devices), use the 'pull'
    command for Git (e.g. 'git pull') or the 'update' command for Mercurial
    (e.g. 'hg update'). This will get all the latest changes from the master
    branch and attempt to merge them with your files. If there are any
    conflicts in the automatic merging process (e.g. you and someone else have
    committed edits to the same lines of code in a file), you will have to open
    the files with conflicts and determine which code should be used in the
    conflicting region.

    When you're setting up a new repository, generally the first file to create
    is a ReadMe file, which can be in .txt or .md format. A ReadMe specifies
    how to use your repo, including any running instructions, formatting
    specifications, and other relevant notes to users and/or other
    contributors. Files ending in '.txt' are standard text files, and in '.md'
    are markdown files. The markdown format allows for some additional
    formatting options such as bold/italicised/underlined text, and text of
    different sizes.
'''


# Tracking Files
'''
    In a repo it's important to determine which types of files you want
    tracked. One of the first files to create in a repository is the ignore
    file, which specifies file formats you'd like to automatically ignore.
    Often this will include things like automatically generated files when
    compiling code, since these files are machine specific and won't work on
    other people's devices. An ignore file must be called '.gitignore' in Git
    repos, and '.hgignore' in Mercurial ones. Each line of the file specifies
    one file format to ignore, which can include specific filenames as well as
    more general file types, or even just folder names. It's often best to have
    a general overarching ignore file in the top-level folder in your repo, and
    then additional ignore files in folders where you want to ignore specific
    files. Note that ignore files only influence the folder they are in and
    everything that folder contains. The different repos have different ignore
    file formats, which have detailed guides online. Note also that the
    preceding dot in the filename makes the ignore file generally hidden from
    view (can be viewed with 'ls -a' in bash).

    To add a file to be tracked by the repo, use the 'add <path/filename>'
    command. If you are satisfied that your ignore file is automatically
    ignoring all files you don't want, you can add all files in the current
    directory (e.g. 'hg/git add .').

    Sometimes you want to move, rename, or delete a file. It's best to involve
    your repository system while doing this, to avoid having to manually update
    the files being tracked afterwards. To move a file, use 'git/hg mv
    <filename> <new_path>'. To rename a file, use the mv command with the new
    desired filename at the end of the new_path (e.g. 'git mv old_file.txt
    my_folder/moved_file.txt'). To delete a file use 'git rm <filename>' or 'hg
    remove <filename>'.

    While setting up a general .gitignore file early on is a good idea,
    sometimes you still miss certain file-types. If you want to stop tracking a
    file, use 'git rm --cached <filename>', or 'hg forget <filename>'.
'''


# Viewing Status/Changes (Status/Log/Diff)
'''
    Before committing it's often good to know which changes have been modified,
    so you can write meaningful commit messages. It's also useful to know when
    your current branch has commits which haven't been pushed to the master
    branch, particularly when you're discussing with collaborators. To check
    which changes will be committed in the next commit, as well as which files
    are yet to be added to the repository tracking and how many commits have
    been done since the last push, use the 'status' command (e.g. 'git/hg
    status').

    It can also be helpful to view your previous commit messages, which can be
    checked using the 'log' command. In Mercurial, if any files have been moved
    at some point, you should use the -f flag, as in 'hg log -f'.

    To check the changes that have occurred between the current version of a
    file and the last committed version, use the 'diff' command (e.g. 'git/hg
    diff <filename>')
'''


# Restoring a Previous State
'''
    Since Git is a reasonably complicated repository system, 'undoing' previous
    changes, or restoring to a previous state can be accomplished in a number
    of different ways - depending on what it is you actually want to achieve.
    This GitHub blog post goes through most of these ways, for if you ever need
    to reset or restore some or all of your repository:
        https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/
'''


# Issues, Projects, and Releases
'''
    Some hosting services also provide additional features with a repository.
    GitHub provides Issues, Projects, and Releases, which are convenient
    abstractions for things that are generally desirable to track with the rest
    of your repo data. Other hosts may offer similar functionality, but the
    GitHub implementation is explicit, and useful for explaining.

    Issues denotes any and all issues that are known to be part of the repo.
    This allows contributors to track bugs that occur, and discuss with one
    another exactly what effects a particular bug has, and potentially how to
    fix it. Issues can also be assigned to a specific contributor, which is
    useful if they wrote the section of code causing one or more issues. Having
    issues openly accessible also means general users can check if unexpected
    behaviour they're experiencing is known about, or if they need to raise an
    issue so it can be fixed or explained.

    Projects are a helpful way of explaining to users and fellow contributors
    the future aims of a repo, and what's being worked on at the moment. If
    regularly updated, they can provide accurate information as to which
    features are available, what's planned, and who is working on what. This
    helps suggestions be targeted to the correct people, and can also encourage
    suggestions if a user or contributor wants a feature that isn't yet planned
    for.

    Releases are official compilations of the code, at stages where it is ready
    for testing (alpha), ready for users but likely to contain known or unknown
    bugs (beta), or a stable release with no known or expected bugs (official
    release). Releases should have version numbers (e.g. v-alpha.1, v-beta.3,
    v-1.0.0). Only have the number of decimal points useful to your project -
    depending on how important your changes are across versions. If you never
    release small changes, only have one decimal point. Major changes,
    particularly those that are not backwards compatible, should have their own
    full version number (e.g. v-1.3.9 -> v-2.0.0).
'''


# ----- NOTE: Subversion (SVN) ----- #
'''
    Another open-source repository is subversion (SVN), which is a
    'centralised' system. Instead of storing all the repository data on all
    branches, contributors work off local copies of the latest files, called
    'working copies', and the central server is the true repository.
    Centralised repositories don't allow for local commits with separate
    publishes - every commit goes directly to the server, which stores the
    relevant change-log and metadata. This is best suited for smaller projects
    with small numbers of contributors - particularly for private development
    where you just want to be able to restore to a previous version if
    something goes wrong.

    SVN supports add, mv, rm, log, status, and diff commands. To get a new
    working copy of a repository, you use svn checkout URL/svn co URL. To
    update to the latest changes, use 'svn update', as in Mercurial.
'''




#-------------------------- RECAP, AND WHERE TO NOW? --------------------------#
'''
    This wraps up this introductory course to programming with Python. You've
    learnt about commenting, variables, conditionals, functional programming,
    object-oriented programming, GUIs, libraries, recursion, testing, and
    repositories, as well as a few other specifics. You should now understand
    enough about programming to be able to write useful programs to solve many
    problems and improve your efficiency and workflow. Additionally, should you
    need to learn a new programming language, you now have the tools to
    understand the principles behind what a high-level programming language can
    can't do, as well as how to use programming effectively to create desired
    functionality and outputs.

    It's possible you will only use python rarely in future, but as the world
    moves further into automation it may well give you an edge over your peers,
    and enable you to progress faster, due to your better understanding of what
    drives automation and how it can be accomplished. If you're interested in
    pursuing more programming, consider delving into the world of statistical
    analysis, where you'll find out about machine learning and artificial
    intelligence, and training programs to recognise useful patterns that we
    humans can't determine, and sometimes can't even comprehend. If you found
    learning python fun, consider learning one or more other programming
    languages (e.g. HTML5/CSS for websites, or C for low-level high-performance
    code). Perhaps you'll find your calling in programming ethics, determining
    how algorithms can be ethical and avoid bias, while still being efficient
    and maintaining their performance benefits.

    I hope that this course has been both fun and informative for you, and wish
    you all the best for your future, especially in the world of programming.

    Sincerely,

    ES Alexander
'''
