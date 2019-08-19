# Section04-3
# 파이썬 데이터 타입(짜료형)
# 리스트, 튜플

# 리스트(순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()
print()
# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.remove(2)
print(y)
y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)

# append는 리스트 자체를 삽입
# extend는 연장

# 삭제 : del, remove, pop

# 튜플(순서ㅇ, 중복ㅇ, 수정x, 삭제x)
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(d[2:])
print(c + d)
print(c * 3)
print()
print()
print()
# 튜플 함수
# 왜 콤마 찍고, 찍어서 나오는 거지?
z = (5, 2, 1, 3, 4)
