# -*- coding: cp949 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' # %s 한 부분 뒤에 snow 라는 문자가 출력된다.
print "And everywhere that Mary went."
print "." * 10  # what'd that do? 점이 10개 반복적으로 찍히게 된다.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# end 하나마다 명령어를 지정해 두고 + 연산자를 사용하면 그 알파벳들이 연속적으로 출력되며, 뒤에 쉼표을 사용하였기 때문에 이어져서 출력되게 된다.
# 쉼표를 제거하면 행이 다음 줄로 넘어가게 된다.