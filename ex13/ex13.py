# -*- coding: utf8 -*-
from sys import argv

print("argv = " + str(argv))
script, first, second, third = argv

print("The script is called: %s" % script)
print("Your first variable is: %s" % first)
print("Your second variable is: %s" % second)
print("Your third variable is: %s" % third)
# edit configurations에서 script parameters에 어떠한 값을 입력하여야 출력이 가능해졌다.
# PyCharm 에서 .py 파일을 실행시킬 때 사실은 뒤에서 python.exe 가 작동하고 있음
# PyCharm 은 우리가 작성한 .py 파일의 상세한 위치를 python.exe 에 전달하고, python.exe 가 해당 .py 파일을 실행하면서
# 출력하는 내용을 Console 칸에 표시함
# 이 예제에서는 “뒤에서 실행되고 있던 “ python.exe 를 명령행 command line 에서 실행시켜 보는 것임
# 그래서 우리가 작성한 .py 파일이 매개변수에 따라 다르게 작동할 수 있음을 보이고자 했음
