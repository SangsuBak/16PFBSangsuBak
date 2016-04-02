# -*- coding: cp949 -*-
formatter = "%r %r %r %r" # formatter이라는 문자에 특수한 기호들을 지정한다.

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)