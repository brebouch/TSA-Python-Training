##################################################################
#                                                                #
#       Python Basics                                            #
#       Objects and Data Types                                   #
#       The code below walks through the building blocks         #
#       of the Python programing language                        #
#       Author: Brennnan Bouchard, brebouch@cisco.com            #
#                                                                #
###################################################################

#
#                           Simple data types
#


# Strings - Worlds, spaces, numbers, and punctuation as a single object (Python handles these as Char Arrays)
# Written in double " or single ' quotes for single line,  triple quotes ''' or """ for multiline
example_string = 'Example String'
print(type(example_string))
print(example_string)


# Bool - (Boolean) True or False
example_bool = True
print(type(example_bool))
print(example_bool)


# Int - (Integer) Whole number
example_int = 50
print(type(example_int))
print(example_int)


# Float - Number with decimal place, additional lengths exist depending on memory need
example_float = 1.5
print(type(example_float))
print(example_float)


#
#                           Complex data types
#


# List - Ordered iterable data, similar to array in C languages
# Written with [ ] and can contain just about any data type
example_list = ['text', 450, ['inner list', 'another string']]
print(type(example_list))
print(example_list)


# Tuple - Immutable list
# Written with ( ) and can contain just about any data type
example_tuple = ('string', 456)
print(type(example_tuple))
print(example_tuple)


# Dictionary - Key:value pair
# Written with { } and keys must be unique and of basic type, string, int, char
# Values accessed by calling the 'key' value in square brackets following the variable
example_dictionary = {'key': 'value'}
print(type(example_dictionary))
print(example_dictionary['key'])

