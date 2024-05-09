import sys
from PyQt5.QtWidgets import *
from PyQt5 import  uic #ui를 연결
from collections import  Counter
#ui 파일 연동
from_class=uic.loadUiType("calculator2.ui")[0]
calculator_icon_list=["+","-","÷","x","."]
class Window(QWidget,from_class): #QWidget from class 상속받아서 사용자 Window 클래스 생성

    def __init__(self):#생성자
        super().__init__()#QWidget 클래스의 생성자 호출
        self.initUI()#사용자가 정의한 아래 함수 호출
        self.show()

    def initUI(self):
        self.setupUi(self)# 현재 클래스에 있으면 호출하지만 없으니까 부모의 메서드 호출
        self.btn_0.clicked.connect(self.btn_0_click)#이벤트를 함수에 연결(on)
        self.btn_1.clicked.connect(self.btn_1_click)#이벤트를 함수에 연결(on)
        self.btn_2.clicked.connect(self.btn_2_click)#이벤트를 함수에 연결(on)
        self.btn_3.clicked.connect(self.btn_3_click)#이벤트를 함수에 연결(on)
        self.btn_4.clicked.connect(self.btn_4_click)#이벤트를 함수에 연결(on)
        self.btn_5.clicked.connect(self.btn_5_click)#이벤트를 함수에 연결(on)
        self.btn_6.clicked.connect(self.btn_6_click)#이벤트를 함수에 연결(on)
        self.btn_7.clicked.connect(self.btn_7_click)#이벤트를 함수에 연결(on)
        self.btn_8.clicked.connect(self.btn_8_click)#이벤트를 함수에 연결(on)
        self.btn_9.clicked.connect(self.btn_9_click)#이벤트를 함수에 연결(on)

        self.btn_del.clicked.connect(self.btn_delete_click)
        self.btn_plus.clicked.connect(self.btn_plus_click)
        self.btn_minus.clicked.connect(self.btn_minus_click)
        self.btn_obelus.clicked.connect(self.btn_obelus_click)
        self.btn_times.clicked.connect(self.btn_times_click)
        self.btn_equal.clicked.connect(self.btn_equal_click)
        self.btn_point.clicked.connect(self.btn_point_click)
        # self.display.clicked.connect(self.display_click)
        # self.display_result.clicked.connect(self.display_result_click)

    def number(self,num):
        #예외 처리
        #소수점 없이 0으로 시작하는 숫자 예외 처리
        #0을 찍고 . 없이 숫자를 쓰면 0 삭제후 마지막 입력 숫자만 등록
        select_btn=self.sender()
        #클릭된버튼에 표기된 text 반환
        select_btn_text=select_btn.text()
        #. 기호 유무 파악을 위한 변수 선언
        exist_text=self.display.toPlainText()
        #각 변수에 해당 조건이 충족 안되면 최종 입력값만 기록
        if exist_text=="0" and select_btn_text !=".":
            self.display.setText(select_btn_text)
        else:
            #조건이 충족되면 추가입력
            self.display.setText(exist_text+num)
    #수식삭제
    def del_num(self):
        exist_text=self.display.toPlainText()
        self.display.setText(exist_text[:-1])
            #사칙 연산 기호 중복 입력 방지 함수
    def no_double_math_icon(self):
        exist_text=self.display.toPlainText()
        if exist_text[-1] in calculator_icon_list:
            # 슬라이싱 문법 공부 필수
            self.display.setText(exist_text[:-1])
    def no_double_point_icon(self):
        exist_text=self.display.toPlainText()
        if exist_text[-1] in calculator_icon_list:
            # 슬라이싱 문법 공부 필수
            self.display.setText(exist_text[:-1])
    # . 기호 생성 제한 알고리즘 변수

    def point_generator(self):
        #디스플레이 str 값 변수 선언
        exist_text = self.display.toPlainText()
        #Counter 문법 확인 필수: 존재하는 인자 갯수 확인하여 dict 형식 생성
        counter_exist_text=Counter(exist_text)
        #형변환:Counter =>dict
        counter_dict=dict(counter_exist_text)
        ### 중요
        # 1. 없는 key 값은 에러를 발생시키는 dict 구조문 dict.get로 해결=>return None 타입
        # 2. NoneType 형식 반환이 문제 -> int(value or 0) 문법으로 None ->0 변환
        # exist_text_icon_count= 연산 기호의 총 갯수
        exist_text_icon_count=int(counter_dict.get("x")or 0)+ \
            int(counter_dict.get("%")or 0)+int(counter_dict.get("-")or 0)+ \
            int(counter_dict.get("+")or 0)
        #연산 기호의 갯수사 "." 갯수보다 많을 때만 추가 "." 입력 가능 조건문
        if exist_text_icon_count>=exist_text.count("."):
            self.number(".")
    ################################
    ############ 사칙연산 함수  ############
    ###################################
    def btn_delete_click(self):
        self.del_num()

        # 사칙연산
        # 아무 내용 없을 때 연산 기호 입력 에러 예외 처리 추가

    def btn_plus_click(self):
        exist_text = self.display.toPlainText()
        if exist_text:
            self.plus()

    def btn_minus_click(self):
        exist_text = self.display.toPlainText()
        if exist_text:
            self.minus()

    def btn_times_click(self):
        exist_text = self.display.toPlainText()
        if exist_text:
            self.times()

    def btn_obelus_click(self):
        exist_text = self.display.toPlainText()
        if exist_text:
            self.obelus()
        # 결과

    def btn_equal_click(self):
        self.equal()

        # . 기호

    def btn_point_click(self):
        exist_text = self.display.toPlainText()
        if exist_text:
            self.point()

    ################################
    ############ 기호 함수  ############
    ###################################
    ###########기호 입력 조건 ########
    # 1. 최초 숫자 없이 "." 입력불가
    # 2. 연산 기호 입력 전 숫자에는 단 1개의 "." 만 존재 가능
    # 3. 연산 기호 후 2번째 "."  입력 가능
    # 4. 연산 기호 보다 "." 적거나 같아야 함

    #연산 기호 n개 삽입 기준 총 n+1 개의 point가 있을 수있다
    def point(self):
        #1. point 연달아 기재 금기 함수
        self.no_double_point_icon()
        #2. point 2개 이하 사칙 연산 앞 뒤 1개씩 입력
        self.point_generator()
        ################################
        ############ 결과 도출 함수  ############
        ###################################

    def equal(self):
        #문자열은 배열 형식이지만 수정 불가 (튜플) -> 수정 가능한 list 변환과정
        exist_text=self.display.toPlainText()
        #list 형으로 변환
        exist_text_list=list(exist_text)
        try:
            #UI 통일감을 주기 위한 코드: 사칙 연산 기호 내부 변환
            for i in exist_text_list:
                if i=="x":
                    exist_text_list[exist_text_list.index(i)]="*"
                elif i =="%":
                    exist_text_list[exist_text_list.index(i)]="/"
            #다시 join 메서드를 통해서 문자열로 변환
            str_text_list="".join(exist_text_list)
            #Eval 함수는 문자열 식 값을 산수하여 int로 변환
            answer= eval(str_text_list)
            #소수점 길이 설정
            answer_round=round(answer,6)

            #setText에 맞는 str 형 변환
            self.display_result.setText(str(answer_round))
            #display 화면 초기화
            self.display.setText("")
        except Exception as e:
            print("error",e)
    def btn_0_click(self): print('0번 버튼이 눌렷어요')
    def btn_1_click(self):print('1번 버튼이 눌렷어요')
    def btn_2_click(self):print('2번 버튼이 눌렷어요')
    def btn_3_click(self):print('3번 버튼이 눌렷어요')
    def btn_4_click(self):print('4번 버튼이 눌렷어요')
    def btn_5_click(self):print('5번 버튼이 눌렷어요')
    def btn_6_click(self):print('6번 버튼이 눌렷어요')
    def btn_7_click(self): print('7번 버튼이 눌렷어요')
    def btn_8_click(self):print('8번 버튼이 눌렷어요')
    def btn_9_click(self):print('9번 버튼이 눌렷어요')


    def btn_del_click(self):print('del 버튼이 눌렷어요')
    def btn_equal_click(self):print('equal 버튼이 눌렷어요')
    def btn_minus_click(self):print('minus 버튼이 눌렷어요')
    def btn_plus_click(self):print('plus 버튼이 눌렷어요')
    def btn_point_click(self):print('point 버튼이 눌렷어요')
    def btn_times_click(self):print('times 버튼이 눌렷어요')
    def btn_display_click(self): print('display 버튼이 눌렷어요')
    def btn_display_result_click(self):print('display 버튼이 눌렷어요')




if __name__=='__main__':
    app=QApplication(sys.argv)#Application 생성
    myCalc=Window()#위에서 생성한 클래스 기반의 객체 생성
    sys,exit(app.exec_())
