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

    def __repr__(self):
        ''' Returns the formal representation of this PhysicalObject.

        Output is of the form 'PhysicalObject(name="str", mass=float)'.

        PhysicalObject.__repr__() -> str

        '''
        return 'PhysicalObject(name="{0}", mass={1})'.format(self._name,
                                                             self._mass)

    def __str__(self):
        ''' Returns a human readable representation of this PhysicalObject.

        Output is of the form:
            'Physical Object:
                name: str
                mass: float'

        PhysicalObject.__str__() -> str

        '''
        return 'Physical Object:\n\tname: {0}\n\tmass: {1}'.format(self._name,
                                                                   self._mass)
