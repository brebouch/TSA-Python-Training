##################################################################
#                                                                #
#       Python Basics                                            #
#       Functions, Classes                                       #
#       The code below walks through the building blocks         #
#       of the Python programing language                        #
#       Author: Brennnan Bouchard, brebouch@cisco.com            #
#                                                                #
###################################################################

#
#                               Functions
#
#       Sections of code which perform a certain action, built for reusability so that
#       rather than writing the same code over again and again you can simple call a
#       function. Functions can take zero or more arguments and can return values but
#       they do not have to. Very simple "Hello" example included below
#


def say_hi(name):
    hello = 'Hello ' + name
    print(hello)
    return hello


say_hi('Bob')


#       As you can see here, we created a function called say_hi that takes a single
#       argument we call name. As with all programming you are free to name your functions
#       and variables whatever you want so long as they begin with an alphabetical
#       character and are not a system keyword. We then do a little string concatenation to
#       create a new string variable we call hello, which is then printed, and returned from
#       the call to be used later in the application.


#
#                               Classes
#
#       Classes allow for Python to act as an object-oriented programming language.
#       By creating a class, you define the blueprint of everything that makes up the class.
#       This will include things like variables and functions to be called on class objects
#       as methods. Classes will be initialized when an object is created and can require
#       certain properties to be defined at this point, or defaulted. Similarly, the initialization
#       flow can. Be defined in a class or if left to the default it will simply run from the top
#       down instantiating variables and running any code not contained in a function call.
#
#       Another component of a class that is critical to understand is the idea of self. Objects of
#       classes may be created many times with vastly different values that will remain persistent
#       to the life of the class object. Within the declaration you must work with variables by
#       calling the self.VARIABLE_NAME in order to maintain persistence within the scope.


# Example class
class Example:
    def __init__(self):
        self.variable = 'class string variable'

    def class_method(self):
        print(self.variable)


# Create instantiation of class
e = Example()
# Change class variables
e.variable = 'new variable'
# Call objects class methods
e.class_method()
