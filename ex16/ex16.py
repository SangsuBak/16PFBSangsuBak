# -*- coding: utf8 -*-
# http://learnpythonthehardway.org/book/ex16.html
from sys import argv

script, filename = argv

print "We've going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()
#truncate란 명령어는 파일안에 내용을 모두 지워지게 하는 것이다.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
# 여기에 있는 명령어들이 수행되면 새로운 파일이 생성됨.
