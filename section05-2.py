# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1, 11):
    print("v3 is :", v3)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1, 101)))
print('1 ~ 100 : ', sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 리스트~~
names = ['kim', "Park", "Cho", "Choi", "Yoo"]

for v in names:
    print("You are : ", v)

# 문자열 : imutable 한번 할당하면 수정이 불가능, 순서가 있고, 한단어 한단어가 할당이 되어 있기 때문에
word = "dreams"

for s in word:
    print("Word : ", s)

# 딕셔너리
my_info = {
    "name": "Jung",
    "age": 27,
    "city": "Gwang-ju"
}

# 기본 값은 키
for key in my_info:
    print("my_info", key)

# 값
for key in my_info.values():
    print("my_info", key)

# 키
for key in my_info.keys():
    print("my_info", key)

# 키, 값
for k, v in my_info.items():
    print("my_info", k, v)


name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for hehe in numbers:
    if hehe == 33:
        print("33 찾았다!!")
        break
    else:
        print("없는디::")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for hehe in numbers:
    if hehe == 33:
        print("33 찾았다!!")
        break
    else:
        print("없는디::")
else:
    print("없는디;;;;")

# continue : 조건이 맞으면 다음으로 PASS

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
# 처리기사 조금 더
# 영어공부
# 놀기
# 실천할 거 준비
