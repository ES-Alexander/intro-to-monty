#!/usr/bin/env python3
################################################################################
# This file contains tests for the L7_1_exercises.py file.                     #
################################################################################

import sys; sys.path.append('..')
from TestRun import TestRun

class L7Tests(TestRun):

    def __init__(self):
        ''' '''
        super().__init__()
        self._required_methods = ['__init__', '__str__', '__repr__']

    # helper method
    def class_test(self, test_class, *parents):
        ''' General test for a class (required methods, parents). '''
        class_name = test_class.__name__
        assert eval('{}.__doc__'.format(class_name)), \
                    "Missing class docstring."
        for method in self._required_methods:
            assert eval('{}.{}'.format(class_name, method)), \
                   "Missing {} method.".format(method)
            assert eval('{}.{}.__doc__'.format(class_name, method)), \
                   "Missing {} method docstring.".format(method)
            assert eval('{!r} in {}.__dict__'.format(method, class_name)), \
                   "{} method for this class ".format(method) +\
                   "should be defined directly, not inherited."

        methods = dict(vars(test_class))
        for parent_class in parents:
            assert parent_class in test_class.__bases__, \
                   "Missing parent class '{}'".format(parent_class.__name__)
            for var in vars(parent_class):
                methods.pop(var, None)
        assert len(methods) > 0, 'Should have at least one unique instance ' +\
               'property and instance method (for each class).'
            
    # test functions
    def test_physical_object(self):
        ''' Tests the PhysicalObject class. '''
        self.class_test(PhysicalObject, object)

    def test_flying_object(self):
        ''' Tests the FlyingObject class. '''
        self.class_test(FlyingObject, PhysicalObject)

    def test_land_object(self):
        ''' Tests the LandObject class. '''
        self.class_test(LandObject, PhysicalObject)

    def test_bird(self):
        ''' Tests the Bird class. '''
        self.class_test(Bird, PhysicalObject)

    def test_parrot(self):
        ''' Tests the Parrot class. '''
        self.class_test(Parrot, FlyingObject, Bird)

    def test_emu(self):
        ''' Tests the Emu class. '''
        self.class_test(Emu, LandObject, Bird)

    def test_type_counts(self):
        ''' Tests the method and variable type counts. '''
        # initialise types and counts
        types = {'instance method':0, 'static method':0, 'class method':0,
                 'class variable':0}

        # Can't test instance variables, because don't have instances.
        # Without major alteration though, PhysicalObject should always have
        #   at least one instance variable anyway.

        # unbound instance methods have the same type as external functions
        instancemethod = type(lambda:None)
        exclusions = ['__module__','__doc__','__dict__','__weakref__']
        
        for cls in [PhysicalObject, FlyingObject, LandObject,
                    Bird, Parrot, Emu]:
            cls_vars = vars(cls)
            cs = [cls_vars[c] for c in cls_vars if c not in exclusions]
            for c in cs:
                if isinstance(c, classmethod):
                    types['class method'] += 1
                elif isinstance(c, staticmethod):
                    types['static method'] += 1
                elif isinstance(c, instancemethod):
                    types['instance method'] += 1
                else:
                    types['class variable'] += 1

        for key in types:
            assert types[key] > 0, "Should have at least one {}.".format(key)


        


#------------------------------ Example Solutions -----------------------------#

if __name__ == '__main__':
    
    from random import randrange # used by Parrot class

    """
        As you may have found, __str__ and __repr__ methods are often quite
        similar across classes, particularly if you use consistent formats for
        your variable names. In this solution, I've modified PhysicalObject to
        include automatic generation of the __str__ and __repr__ methods, which
        can then easily be re-used in subclasses. Note that subclasses still
        have their own docstring describing the expected output of each method,
        since __str__ and __repr__ outputs are always unique to their class
        (at minimum, they include their class' name).
    """

    class PhysicalObject(object):
        ''' A class for physical objects. '''
        def __init__(self, name, mass):
            ''' A class for storing and tracking physical objects.

            Constructor: PhysicalObject(str, float)
            
            '''
            # initialise instance variables
            self._name = name
            self._mass = mass

            # initialise automatic str/repr generation variables
            self._repr_except = ['_repr_except','_str_except',
                                 '_repr_replace','_str_replace',
                                 '__module__','__doc__','__dict__',
                                 '__weakref__']
            self._str_except = list(self._repr_except) # copy
            self._repr_replace = {}; self._str_replace = {} # no replacements

        def get_name(self):
            ''' Returns the name of this.

            self.get_name() -> str

            '''
            return self._name

        def get_mass(self):
            ''' Returns the mass of this.

            self.get_mass() -> float

            '''
            return self._mass

        def set_name(self, new_name):
            ''' Sets the name of this to the specified 'new_name'.

            self.set_name(str) -> None

            '''
            self._name = new_name

        def set_mass(self, new_mass):
            ''' Sets the mass of this to the specified 'new_mass'.

            self.set_mass(float) -> None

            '''
            self._mass = new_mass

        def _get_params(self, mode, *exceptions, **replacements):
            ''' Returns the parameters of this in a useful format for str/repr.

            First returned value is the name. Subsequent values are key-value
                pairs of variable names/descriptors and their values.

            'mode': can be 'str' or 'repr' -> modifies name output, and
                determines if classvariables are considered.
            'exceptions': a set of variables which should be excluded from
                the returned output.
            'replacements' is a mapping of existing variable names which should
                be replaced by the specified names/descriptors.

            self._get_params(str, *str, **{str'var_name':str'replacement'})
                    -> list[str, list[str, object]]

            '''
            # set name as first param
            if mode == 'repr':
                params = [type(self).__name__]
            elif mode == 'str':
                params = [self.parse_class_name(type(self).__name__)]
                
            # get instance name/value pairs and add to output
            instance_vars = vars(self)
            for var in instance_vars:
                if var in exceptions:
                    continue
                value = instance_vars[var]
                if var in replacements:
                    var = replacements[var]
                elif mode == 'str':
                    var = var.replace('_',' ').strip()
                    
                params += [[var.lstrip('_'), value]]
                
            if mode == 'repr':
                return params # don't consider class variables
            
            # get class name/value pairs and add to output
            class_vars = vars(self.__class__)
            func = type(lambda:None) # get function type (id instance methods)
            for var in class_vars:
                if var in exceptions or var in instance_vars:
                    continue # skip if manually excepted or already covered
                value = class_vars[var]
                if isinstance(value, func) or \
                   isinstance(value, classmethod) or\
                   isinstance(value, staticmethod):
                    continue # skip if not a class-variable
                if var in replacements:
                    var = replacements[var]
                else:
                    var = var.replace('_',' ').strip()
                    
                params += [[var, value]]
            return params

        def _general_repr(self, *exceptions, **replacements):
            ''' Returns a generalised __repr__ result with valid format.

            Takes the specified exceptions and replacements into account.

            self._general_repr(*str, **{str'var_name':str'replacement'}) -> str

            '''
            params = self._get_params('repr', *exceptions, **replacements)
            name = params.pop(0) + '('
            param_str = ', '.join(
                ['{}={!r}'.format(p[0],p[1]) for p in params])
            return name + param_str + ')'

        def _general_str(self, *exceptions, **replacements):
            ''' Returns a generalised __str__ result with consistent format.

            Takes the specified exceptions and replacements into account.

            self._general_str(*str, **{str'var_name':str'replacement'}) -> str

            '''
            params = self._get_params('str', *exceptions, **replacements)
            header = params.pop(0) + ':\n\t'
            param_str = '\n\t'.join(
                ['{}: {!r}'.format(p[0],p[1]) for p in params])
            return header + param_str

        def __repr__(self):
            ''' Returns a formal representation of this PhysicalObject.

            Output is of the form 'PhysicalObject(name="str", mass=float)'.

            self.__repr__() -> str

            '''
            return self._general_repr(*self._repr_except, **self._repr_replace)

        def __str__(self):
            ''' Returns a human readable representation of this PhysicalObject.

            Output is of the form:
                'Physical Object:
                    name: str
                    mass: float'

            self.__str__() -> str

            '''
            return self._general_str(*self._str_except, **self._str_replace)
                
        @staticmethod
        def parse_class_name(name):
            ''' Returns the class name with spaces between words.

            PhysicalObject.parse_class_name(str) -> str

            '''
            output = ''
            for letter in name:
                if letter.isupper():
                    output+= ' ' + letter
                else:
                    output += letter
            return output.strip()


    class FlyingObject(PhysicalObject):
        ''' A class for flying objects. '''
        def __init__(self, name, mass, average_alt, *args, **kwargs):
            ''' A class for storing and tracking flying objects. 

            Constructor: FlyingObject(str, float, float)

            '''
            # run parent initialisation
            super().__init__(name, mass, *args, **kwargs)
            # add additional variables
            self._average_alt = average_alt
            self._current_alt = 0

            # modify automatic str/repr variables
            self._repr_except += ['_current_alt']
            self._str_replace.update({'_current_alt':'current altitude',
                                      '_average_alt':'average altitude'})

        def set_current_alt(self, current_alt):
            ''' Sets the current altitude of this.
            
            self.set_current_alt(float) -> None

            '''
            self._current_alt = current_alt

        def get_current_alt(self):
            ''' Returns the current altitude of this.

            self.get_current_alt() -> float

            '''
            return self._current_alt

        def __repr__(self):
            ''' Returns a formal representation of this FlyingObject.

            Output is of the form:
                'self.name="str", mass=float, average_alt=float)'

            self.__repr__() -> str

            '''
            return super().__repr__()

        def __str__(self):
            ''' Returns a human readable representation of this FlyingObject.

            Output is of the form:
                'Flying Object:
                    name: str
                    mass: float
                    average altitude: float
                    current altitude: float'

            self.__str__() -> str

            '''
            return super().__str__()


    class LandObject(PhysicalObject):
        ''' A class for land objects. '''
        def __init__(self, name, mass, latitude, longitude, *args, **kwargs):
            ''' A class for storing and tracking land objects. 

            Constructor: LandObject(str, float, float, float)

            '''
            super().__init__(name, mass, *args, **kwargs)
            self._latitude = latitude
            self._longitude = longitude
            

        def set_location(self, location):
            ''' Sets a new location for this.

            'location': must be a list containing the updated latitude and
                longitude of the object.

            self.set_location(list[float,float]) -> None

            '''
            self._latitude, self._longitude = location

        def __repr__(self):
            ''' Returns a formal representation of this LandObject.

            Output is of the form:
                'LandObject(name="str", mass=float, latitude=float,
                            longitude=float)'

            self.__repr__() -> str

            '''
            return super().__repr__()

        def __str__(self):
            ''' Returns a human readable representation of this LandObject.

            Output is of the form:
                'Land Object:
                    name: str
                    mass: float
                    latitude: float
                    longitude: float'

            self.__str__() -> str

            '''
            return super().__str__()
            
            
    class Bird(PhysicalObject):
        ''' A class for birds. '''

        _main_surface = 'feathers'

        def __init__(self, name, mass, lifespan, life_mate, *args, **kwargs):
            ''' A class for storing and tracking birds.

            'lifespan': years this Bird is expected to live for.
            'life_mate': boolean for if this bird mates for life.

            Constructor: Bird(str, float, float, bool)

            '''
            super().__init__(name, mass, *args, **kwargs)
            self._lifespan = lifespan
            self._life_mate = life_mate

            print(self.get_mating_type())
            if self._life_mate == True:
                print('cute')

            # update str/repr auto-generation variables
            self._str_replace.update({'_life_mate':'mates for life'})

        def get_mating_type(self):
            ''' Returns true if the bird mates for life.

            self.get_mating_type() -> bool

            '''
            
            if self._life_mate:
                return '{} mates for life <3 '.format(self._name)
            else:
                return '{} does not mate for life...'.format(self._name)
            
        def set_surface(self, new_surface):
            ''' Sets the main surface of this.

            The new surface is printed for confirmation.

            self.set_surface(str) -> None

            '''
            self._main_surface = new_surface
            print("New main surface is:", new_surface)

        def __repr__(self):
            ''' Returns a formal representation of this Bird.

            Output is of the form:
                'Bird(name="str", mass=float, lifespan=float, life_mate=bool)'

            self.__repr__() -> str

            '''
            return super().__repr__()

        def __str__(self):
            ''' Returns a human readable representation of self.

            Output is of the form:
                'Bird:
                    name: str
                    mass: float
                    lifespan: float
                    mates for life: bool
                    main surface: str'

            self.__str__() -> str

            '''
            return super().__str__()

        @classmethod
        def get_main_surface(cls):
            ''' Returns the main surface for the Bird class.

            cls.get_main_surface() -> str

            '''
            return cls._main_surface

        @staticmethod
        def calc_wings(birds_num_wings_1, *birds_num_wings_N):
            ''' Calculates the total number of wings in a flock.

            'birds_num_wings_1': a tuple of (number of birds, wings per bird)
                for the first value of wings per bird.
            'birds_num_wings_N': a tuple of (number of birds, wings per bird)
                for the nth value of wings per bird.

            Bird.calc_wings(tuple(int, float), *tuple(int, float)) -> float

            '''
            num_birds_1, num_wings_1 = birds_num_wings_1
            # sum over birds_num_wings_N, starting at birds_num_wings_1
            return sum([w[0]*w[1] for w in birds_num_wings_N],
                       num_birds_1 * num_wings_1)
                    

    class Parrot(FlyingObject, Bird):
        ''' A class for parrots. '''
            
        def __init__(self, name, mass, average_alt, lifespan, life_mate,
                     last_input, *args, **kwargs):
            ''' A class for storing and tracking parrots.

            'last_input': the last thing someone has said to this parrot.
            
            Constructor: Parrot(str, float, float, float, bool, str)

            '''
            super().__init__(name, mass, average_alt, lifespan, life_mate,
                             *args, **kwargs)
            self._last_input = last_input
            self._prev_input = [last_input]

            # update str/repr auto-generation variables
            self._repr_except += ['_prev_input']
            self._str_replace.update({'_prev_input':'previous inputs'})

        def speak(self):
            ''' Returns the parrot's speach (somewhat based off previous input).

            The Parrot SPEAKS! :-O

            self.speak() -> str

            '''
            speak_options = [*self._prev_input, "Squark!", 
                             "{0} want a cracker".format(self._name),
                             "Oh the humanity!", "You're amazing", "Land ho!",
                             "*farts*"]

            return speak_options[randrange(0, len(speak_options))]

        def listen(self, *speech):
            ''' Adds 'speech' to the recorded previous inputs.

            self.listen(*str) -> None

            '''
            self._prev_input += speech
            if len(speech) > 0:
                self._last_input = speech[-1]

        def __repr__(self):
            ''' Returns a formal representation of this Parrot.

            Output is of the form:
                "Parrot(name='str', mass=float, lifespan=float, life_mate=bool,
                        average_alt=float, last_input='str')"

            self.__repr__() -> str

            '''
            return super().__repr__()

        def __str__(self):
            ''' Returns a human readable representation of this Parrot.

            Output is of the form:
                'Parrot:
                    name: str
                    mass: float
                    lifespan: float
                    mates for life: bool
                    average altitude: float
                    current altitude: float
                    last input: str
                    previous inputs: list[str]'

            self.__str__() -> str

            '''
            return super().__str__()

            
    class Emu(LandObject, Bird):
        ''' A class for emus. '''

        def __init__(self, name, mass, latitude, longitude, lifespan, life_mate,
                     num_eggs, *args, **kwargs):
            ''' A class for storing and tracking Emus.

            'num_eggs': the current number of eggs in possession of this.

            Constructor: Emu(str, float, float, float, float, bool, int)

            '''
            super().__init__(name, mass, latitude, longitude, lifespan,
                             life_mate, *args, **kwargs)
            self._num_eggs = num_eggs

        def will_fight(self):
            '''Returns True if this will fight others, else False.

            Tendency to fight depends on the main surface and number of eggs
                in possession.

            self.will_fight() -> bool

            '''
            return self._main_surface == 'feathers' and self._num_eggs > 0
        
        def __repr__(self):
            ''' Returns a formal representation of this self.

            Output is of the form:
                'Emu(name="str", mass=float, lifespan=float, life_mate=bool,
                    latitude=float, longitude=float, num_eggs=int)'

            self.__repr__() -> str

            '''
            return super().__repr__()

        def __str__(self):
            ''' Returns a human readable representation of self.

            Output is of the form:
                'self.
                    name: str
                    mass: float
                    lifespan: float
                    mates for life: bool
                    latitude: float
                    longitude: float
                    num eggs: int'

            self.__str__() -> str

            '''
            return super().__str__()

    Tests = L7Tests().run_tests(verbose=True)
