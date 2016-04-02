# -*- coding: utf8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)

# 출력되는 질문들에 값을 입력하면 문장이 완성 되어서 나온다.
# %r 에서는 말풍선 기호가 나오고, %s 에서는 말풍선 기호가 나오지 않는다.