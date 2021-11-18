##################################################################
#                                                                #
#       Python Basics                                            #
#       Interacting with Files ad the OS                         #
#       The code below walks through the building blocks         #
#       of the Python programing language                        #
#       Author: Brennnan Bouchard, brebouch@cisco.com            #
#                                                                #
###################################################################


import os

#       Manipulating Working Directory

directory = os.getcwd()
print(directory)

new_directory = '/Applications'
os.chdir(new_directory)
print(os.getcwd())

os.chdir(directory)


#       Opening and reading files
#
with open('file_for_reading.txt', 'r') as file_reader:
    read_file = file_reader.read()


# Opening a file to write or append then closing

log = open('test_file.txt', 'a')

for r in range(10):
    log.write('This is loop number: ' + str(r))

log.close()

