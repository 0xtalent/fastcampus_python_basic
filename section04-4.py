# # Section04-4
# # 파이썬 데이터 타입(자료형)
# # 디셔너리, 집합 자료형

# # 딕셔너리(Dictionary) : 순서 x, 중복 x, 수정 ㅇ, 삭제 ㅇ

# # key, Value (Json) -> MongDB
# # 선언
# # a = {'name': 'Jung', 'Phone': '010-4381-5297', 'birth': 930418}
# # b = {0: 'Hello Python', 1: 'Hello Coding'}
# # c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a))

# # 출력
# print(a['name'])
# print(a.get('address'))
# print(c['arr'][1:3])

# # 딕셔너리 추가
# a['address'] = 'Gwangju'
# print(a)
# a['rank'] = [1, 3, 4]
# print(a)

# # keys, values, items
# print(a.keys())
# print(a.values())
# print(list(a.keys()))
# temp = list(a.keys())
# print(temp[1:3])
# # 리스트 안에 튜플이 된 형태로 반환
# print(list(a.items())

# 집합(sets) (순서 x, 중복 x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)

print(l)
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)

print(s3)
s3.remove(15)
print(s3)

print(type(s3))
