# -*- coding: cp949 -*-
# coding: cp 949는 문자열에 한글이 포함되어 있을 경우 출력과정에서 오류가 나는 것을 막아준다.
x = "There are %d types of people." % 10 # debrugging, %d는 정수를 나타낼 때 사용(%g는 실수)
binary = "binary" #binary = 이진수
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # %s는 문자열을 표시할 때 사용

print x # 알파벳에 문자열을 등록해 놓을수 있다.
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # %r은 객체를 출력할 수 있는 문자열 형태로 변환하여 돌려주는 함수이다

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e #알파벳에 문자열을 등록해놓고 + 기호를 사용하면 문자열이 이어져서 출련된다.

