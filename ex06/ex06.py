# -*- coding: cp949 -*-
# coding: cp 949�� ���ڿ��� �ѱ��� ���ԵǾ� ���� ��� ��°������� ������ ���� ���� �����ش�.
x = "There are %d types of people." % 10 # debrugging, %d�� ������ ��Ÿ�� �� ���(%g�� �Ǽ�)
binary = "binary" #binary = ������
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # %s�� ���ڿ��� ǥ���� �� ���

print x # ���ĺ��� ���ڿ��� ����� ������ �ִ�.
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # %r�� ��ü�� ����� �� �ִ� ���ڿ� ���·� ��ȯ�Ͽ� �����ִ� �Լ��̴�

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e #���ĺ��� ���ڿ��� ����س��� + ��ȣ�� ����ϸ� ���ڿ��� �̾����� ��õȴ�.

