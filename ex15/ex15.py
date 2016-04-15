# -*- coding: utf8 -*-
# http://learnpythonthehardway.org/book/ex15.html
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
# edit configurations에서 ex15_sample.txt를 추가시켜줘야함
# file을 만들때 확장자 명을 잘 선택해줘야 파일이 실행됨.
