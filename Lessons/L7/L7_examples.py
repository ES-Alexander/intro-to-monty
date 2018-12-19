#!/usr/bin/env python3
# L7 Practice

'''
    Write the basics of the following classes, including __init__, __str__, and
    __repr__ methods, and at least one unique instance property and instance
    method for each class (can be quite simple, but should have correct
    commenting/docstrings):
        PhysicalObject (completed below)
            -> FlyingObject
            -> LandObject
            -> Bird
        (FlyingObject, Bird)
            -> Parrot
        (LandObject, Bird)
            -> Emu

    Ensure that any methods that need redefinition in a subclass at least meet
    the specification of that method in its defining class.

    At least one class should include a useful class property/variable, and at
    least one class should include a relevant classmethod.
'''

class PhysicalObject(object):
    ''' A class for physical objects. '''
    def __init__(self, name, mass):
        ''' A class for storing and tracking physical objects.

        Constructor: PhysicalObject(str, float)
        
        '''
        # initialise instance variables
        self._name = name
        self._mass = mass

    def get_name(self):
        ''' Returns the name of this.

        PhysicalObject.get_name() -> str

        '''
        return self._name

    def get_mass(self):
        ''' Returns the mass of this.

        PhysicalObject.get_mass() -> float

        '''
        return self._mass

    def set_name(self, new_name):
        ''' Sets the name of this to the specified 'new_name'.

        PhysicalObject.set_name(str) -> None

        '''
        self._name = new_name

    def set_mass(self, new_mass):
        ''' Sets the mass of this to the specified 'new_mass'.

        PhysicalObject.set_mass(float) -> None

        '''
        self._mass = new_mass

    def __repr__(self):
        ''' Returns the formal representation of this PhysicalObject.

        Output is of the form 'PhysicalObject(name="str", mass=float)'.

        PhysicalObject.__repr__() -> str

        '''
        return 'PhysicalObject(name="{0!r}", mass={1!r})'.format(self._name,
                                                                 self._mass)

    def __str__(self):
        ''' Returns a human readable representation of this PhysicalObject.

        Output is of the form:
            'Physical Object:
                name: str
                mass: float'

        PhysicalObject.__str__() -> str

        '''
        return 'Physical Object:\n\tname: {0!s}\n\tmass: {1!s}'.format(
            self._name, self._mass)

class FlyingObject(PhysicalObject):
    ''' A class for flying objects. '''
    def __init__(self, name, mass, other_vars, *args, **kwargs):
        ''' docstring here. '''
        super().__init__(name, mass, *args, **kwargs)
        pass # rest of the __init__ function here
    
