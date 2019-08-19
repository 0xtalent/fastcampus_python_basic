# section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = 'NiceMan'
str3 = ''
print(len(str1), len(str2))

excape_str1 = "Do you have a \"big collection\""
print(excape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r"C:\Programs\Test\Bin"
print(raw_s1)

# 멀티라인
multi = \
    """
문자열 

멀티라인 

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
print(str_o1 * 100)
print(str_o2 + str_o3)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수

a = 'niceman'
b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(list(reversed(b)))
# 주석처리하기 ctrl + /? 나 이거 오늘 알았네ㅋㅋ

print(a[:])
print(a[::-1])
