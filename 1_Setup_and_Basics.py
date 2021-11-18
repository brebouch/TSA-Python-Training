##################################################################
#                                                                #
#       Python Basics                                            #
#       Setup & Basics                                           #
#       The code below walks through the building blocks         #
#       of the Python programing language                        #
#       Author: Brennnan Bouchard, brebouch@cisco.com            #
#                                                                #
###################################################################

# Basic IDE Overview and install setup
# Were to find python - https://www.python.org/downloads/
# PyCharm - https://www.jetbrains.com/pycharm/download
# pip & w3school https://www.w3schools.com/python/


#
#
#                              Pip
#
#       Pip is the package installer that is built in to python and allows for easy extension of
#       capabilities without the need to re-create the wheel.
#
#       Installing single package: pip install requests
#
#       Installing bulk dependencies from requirements.txt document: pip install -r requirements.txt


#
#
#                               Importing Modules
#
#        Pythons functionality is dependant on leveraging modules to enhance its base capabilities.
#        These modules can be native to the python distribution, imported from external resources,
#        or from local files. The below imports represent the various options

#   Importing built in json module
import json

#   Importing requests library installed using pip install requests
import requests

#   Importing the local_import.py file as a module to use objects and functions
import local_import

#
#                               Execution flow
#
#
#
#        Program will execute from the top down unless dictated otherwise by control
#        statements, function calls, or class instantiation.

start = 'First thing to be executed'
middle = 'Then this gets called'
if start == middle:
    print('The start and next variables match....')
last = 'Final thing to be done'

#
#
#                               Variable Scope
#
#
#        Variables lifetime depends on the scope in which it is created.
#        For example, variables declared outside any control statements
#        are considered to be Global and will exist for the entire lifetime
#        of the app. Variables defined as arguments in function calls will
#        only exist during the call, in order to access data from function
#        variables, they must be returned. Similarly, variables created in
#        loops will only exist for that iteration, in order to modify a
#        variable within a loop it must already exist.

global_variable = 'This can be accessed anywhere within the app'


def sample_function():
    function_scope = 'This variable can only be used within this function'


for r in range(10):
    loop_scope = 'This variable is only usable within each iteration of the loop'

#
#                           Control Statements
#
#
#           Control the flow of an application to dictate the way
#           it should act and under what conditions.
#
#           Examples:
#           If/Then/Else
#           For Loop
#           While Loop
#           Switch


#        If statement performs a comparison and takes an action depending on if the result is True or False
#        Statement ends in colon and indention following determines the scope

if 5 > 2:
    print('Its true 5 is greater than 2')

if not 2 > 5:
    print('Also true, 2 is not greater than 5')
elif 2 == 5:
    print('This will never execute')
else:
    print('This is the catch all in the sequence')

#
#
#                               For Loop
#
#        For Loops iterate through a list or range to execute a finite number of times
#        upon completion of the iterations the execution flow continues
#        A local variable containing the value of the iteration can be used during each execution

fruit_list = ['apple', 'bananas', 'orange', 'pear']

for fruit in fruit_list:
    print('This time around the fruit variable is: ' + fruit)

#
#
#                               While Loop
#
#        While Loops run a comparison opertation each iteration and stop only if the condition is no longer True or
#        the loop is ended via a break statement, an endless loop can be created by comparing directly against True
#
#        Example while loop with comparison

a = 5
b = 2
while a > b:
    print('b currently equals: ' + str(b))
    b += 1

#        Example while loop with break statement

outside_variable = 1
while True:
    print('will keep looping until variable equals 5 in check below, current value: ' + str(outside_variable))
    if outside_variable == 5:
        print('time to go')
        break
    outside_variable += 1

#
#
#                               Error Handling
#
#       When an error is encountered, for example the action you are attempting is unavailable for
#       the variable type you supply, the application will throw an exception and fail immediately.
#       There are cases where exceptions may be expected and those that may not, each of the two
#       should be handled accordingly.
#
#       Try and catch statements allow for exception handling of all or specific exceptions in
#       cases where you understand they may be present. The syntax below demonstrates two
#       potential uses.

#       Catching any exception
try:
    print('I cannot concatenate strings and integers natively like 1 + ' + 1 + ' doesn’t work')
except:
    print('Caught Exception… moving on now')

#       Catching any exception as a variable
try:
    print('I cannot concatenate strings and integers natively like 1 + ' + 1 + ' doesn’t work')
except Exception as e:
    print(e)

#       Catching a specific exception
try:
    print('I cannot concatenate strings and integers natively like 1 + ' + 1 + ' doesn’t work')
except TypeError as t:
    print('Caught only a TypeError as you can see: \n\n ' + str(t) + '\n\n… moving on now')
