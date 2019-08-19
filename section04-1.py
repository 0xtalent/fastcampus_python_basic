# 데이터 타입
import json as simplejson
import math
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name": "Jung",
    "age": 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_bool))
print(type(v_str1))


i1 = 39
i2 = 979
big_int1 = 999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777
f1 = 1.234
f2 = 3.794
f3 = .5
f4 = 10.
print(i1 * i2)
print(f1 ** f2)
print(f3 + i2)

a = 5.
b = 4

print(type(a), type(b))
result2 = a + b
print(result2)
print(84-72.5)
# 형변환
print(int(result2))

y = 100
y += 100
print(y)

# 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

print(math.ceil(5.1))
