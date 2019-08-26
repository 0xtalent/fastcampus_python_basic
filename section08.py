# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)

import builtins
import pkg.prints as p
from pkg.calculations import div as d
import pkg.calculations as c
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용2(클래스) : 권장하지 않는 방법입니다
# from pkg.fibonacci import *

# Fibonacci.fib(400)

# print("ex2 : ", Fibonacci.fib2(400))
# print("ex2 : ", Fibonacci().title)

# 사용3(클래스)
# from pkg.fibonacci import Fibonacci as fb

# fb.fib(1000)

# print("ex3 : ", fb.fib2(400))
# print("ex3 : ", fb().title)

# 아 왜 맘대로 수정하냐
# 뭐를 해제해야 수정 안되는지 몰라서 주석처리 할게요...허접의 서러움...

# 사용4(함수)

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
print("ex5 : ", int(d(100, 10)))

# 사용6
p.prt1()
p.prt2()
print(dir(builtins))
