# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공강
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

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

# 예제2
# self의 이해
class SelfTest():
    @staticmethod
    def function1():
        print('function1 called!')
# 이거 왜 오류 뜨지...실행은 되는데...
# 짜증나서 구글검색
# https://hashcode.co.kr/questions/1051/클래스-메소드에-self를-적고-안적고는-무슨-차이인가요
# self를 붙인 쪽을 bound, 안 붙인 쪽은 unbound 메소드라 합니다.
# self가 받아주는 역할로 있어야 하는데 self가 없기 때문에 인자가 너무 많이 들어왔다는 겁니다.
# self를 쓰기 싫으면 데코레이트터를 써서 이 메소드는 bound method를 만들지 마라고 설정할 수 있습니다.
# 무슨 말인지는 잘 모르겠지만, 대충 무슨 느낌인지 알겠어서, 데코레이터를 서서 해결

    def function2(self):
        print(id(self))
        print('function2 called!')


self_test = SelfTest()
# self_test.function1()
SelfTest.function1()
self_test.function2()

print(id(self_test))
# self_test = 인자가 위에 자동으로 넘어간겨
# 너무 복잡하게 생각하지 말고 인스턴스를 생성하는 메소드는 셀프인자가 자동으로 넘어간다
# 셀프가 없는 것들은 클래스에서 직접 호출한다
# 깊은 내용을 하고 있으니 어렵게 느껴질 수 있으니, 공부 하는 과정 속에서 자동적으로 이해가 갈 것임
# 이해 하고 넘어가도 괜찮습니다

# 예제3
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num += 1


user1 = WareHouse('Jung')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)
# 흑흑 잘 모르겠어요...클래스 변수...
# 나중에 다시 공부할게요...유튜브로도 공부할게요...
# 더 진행하면서 이해되니까 스트레스 받지 말라고 하시네요...ㅎㅎ

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)
