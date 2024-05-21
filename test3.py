#!/usr/bin/env python3

with open("C:\\Users\\EVRINCDIF\\PycharmProjects\\pythonProject\\text.txt", 'w') as the_file:
    the_file.write('This text will be written to the file.')
    the_file.write('Here is more text.')

with open('C:\\Users\\EVRINCDIF\\PycharmProjects\\pythonProject\\file4.txt', 'x') as the_file:
    the_file.write('ok')
