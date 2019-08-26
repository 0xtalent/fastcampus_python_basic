# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모


class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show" Method!'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return 'Car Info: %s %s %s' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # Super에서 가져옴
print(model1.type)  # Super에서 가져옴
print(model1.car_name)  # Sub에서 가져옴
print(model1.show())  # Super에서 가져옴
print(model1.show_model())  # Sub에서 가져옴
print(model1.__dict__)

# 이해는 완전 이해 가는데, 누가 이거 활용해서 만들어봐라 하면 아직은 못만들 것 같아요
# 더 열심히 공부하자 진도 쭉쭉 빼보자

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "suv", "black")
print(model2.show())  # 부모에 있는 것을 모두 사용하는 것이 아니라, 자식에서 상속받을 것은 받고...

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inhertance Info(상속 정보를 리스트 형태로 반환:mro)
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속


class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())
