# -*- coding: utf8 -*-
# 상위 클래스 이름이 너무 길어져서 fron import as 적용
from CashCardClass import SimpleCashCard as CashCard


# CashCardClass 모듈의 SimpleCashCard 클래스를
# 상속 받아 SafeCashCard 클래스를 정의한다
# SimpleCashCard 는 SafeCashCard 의 상위 클래스
# SafeCashCard 는 SimpleCashCard 의 하위 클래스
class SafeCashCard(CashCard):
    # SimpleCahsCard의 다른 기능을 그대로 사용하고
    #       {__init__(), despoit(), check_balance()}
    #   withdraw() 메소드만 다시 정의한다
    def withrdraw(self, amount_won):
        """
        SafeCashCard withdraw method
        Chek balance before withdraw
        """
        print("SafeCashCard withdraw()") # 함수 호출 표식
        # 잔고가 충분하다면
        if self.check_balance() >= amount_won:
            # 출금한다
            # 상위 클래스의 withdraw 메소드 호출
            CashCard.withdraw(self, amount_won)
        # 그렇지 않으면
        else:
            # 오류를 표시한다
            print("** 오류 발생 **")
            print("잔고가 부족합니다")
            print("인출되지 않았습니다")
# SafeCashCard 클래스 정의 끝
