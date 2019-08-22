# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
# 첫 글자는 대문자로, 단어와 단어 연결할 때도 대문자로


class UserInfo:
    # Class는 속성과 메소드로 구성되어 있다.
    def __init__(self, name):
        self.name = name

    def print_user_info_p(self):
        print("Name : ", self.name)


# 네임스페이스
user1 = UserInfo("Jung")
user1.print_user_info_p()
user2 = UserInfo("Park")
user2.print_user_info_p()

# 모르겠어...잘...ㅋㅋ
print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 잘 모르겠어서 유튜브 검색 ㄱㄱ
# https://youtu.be/YQhJsWj6ydU
# 클래스(Class): 반복되는 불필요한 소스코드를 최소화 하면서
# 현실 세계의 사물을 컴퓨터 프로그래밍 상에서 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
# 오 강의들으니까 쫌 이해가 간다. 그런데 내가 이걸 만들려면 쫌 반복 숙달이 필요할 듯

# https://youtu.be/8IC2z0F9YX4
# 객체 지향 프로그래밍 언어 Object Oriented Programming Language OOP
# 우리가 해야 하는 것 = 세상을 만드는 것
# 세상에 무엇이 있는가 = 객체
# 병원 환자를 관리하는 프로그램 => 세상
# 이 안에는 어떠한 객체들이 있을까?
# 환자! 간호사 + 의사! 병실! 아침 식사!
# 환자 = 면회를 간다 ! [동작]
# 의사 = 진찰을 한다 ! [동작] + 환자를[목적어]
# 의사.진찰한다(환자를)

# https://youtu.be/Np6Wy5mpyMA
# 설명 진짜 잘하신다...윤인성님...당신은 대체...

# 클래스 선언 class <이름 Camel Case>:


# class Student:
#     # 자기자신을 생성하는 함수 = 생성자, self = 객체 자신
#     # 생성자


# def __init__(self, name, korean, math, english, science):
#     self.name = name
#     self.korean = korean
#     self.math = math
#     self.english = english
#     self.science = science

# 파이썬에 있는 모든 클래스 내부의 함수들은 첫번째 매개변수를 self로 개발자들끼리 약속


# 학생 리스트들을 선언
# students = [
#     student("정하용", 100, 100, 100, 100),
#     student("용하정", 92, 84, 80, 72, 64)
# ]

# 생략합니다. 영상보세요
# 오 어제처럼 이해감!! 감사합니다 윤인성님!!
# section07-1 강의는 다시 한번 공부하기
