# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1


def hello(world):
    print("Hello", world)


hello("Hayong")

# 예제2


def hello_return(world):
    val = "Hello " + str(world)
    return val


abc = hello_return("Hayong!!!")
print(abc)

# 예제3(다중리턴)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4(데이터 타입 반환)


def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul2(100)
print(lt)

# 리스트 [], 튜플 ()

# 예제4
# *args 인자, *kwargs 가변인자
# 이거 잘 모르겠어요


def args_func(*args):
    # for t in args:
    #     print(t)
    for i, v in enumerate(args):
        print(i, v)


args_func('Jung')
args_func('Jung', 'Park')
args_func('Jung', 'Park', 'Choi')

# kwargs 키워드 인자
# * 하나일 때는 튜플로 받는데, ** 일 때는 딕셔너리로 받는다.


def kwargs_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1='Jung')
kwargs_func(name1='Jung', name2='Park', name3='Choi')

# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, 'Jung', 'Park', age1=27, age2=54)

# 잘 모르겠어서 구글 검색 : 가변인자 함수는 함수가 몇 개의 인자를 받을지 정해지지 않은 함수입니다.
# 파이썬에서는 가변인자 함수를 지원하고 있습니다.
# 파이썬에서는 가변인자를 받을 때 *를 붙여서 받습니다.
# 가변인자 함수를 통해 좀 더 유연하게 동작하는 함수 작성이 가능합니다.
# 출처 : https://psychoria.tistory.com/530

# 아 모르겠어 다시 검색
# 파이썬 코드를 보다보면 가끔 *args, **kwargs를 볼 수 있습니다.
# 이것은 함수의 인자(parameter 또는 arguments)가 가변 길이일 때 사용합니다.
# args, kargs는 원하는 이름대로 쓸 수 있고, *, **는 각각 non-keyworded argumnets, keworded arguments를 뜻합니다.
# 출처: https://3months.tistory.com/347

# 아 모르겠어 다시 검색
# 오 뭔가 이해 갈 것 같다. 출처 : https://brunch.co.kr/@princox/180
# 파이썬에서 *, **는 주소값을 저장하는 의미가 아닙니다.
# 바로 여러 개의 인수를 받을 때, 키워드 인수를 받을 때 사용하는 표시입니다.
# 먼저 *args부터 알아보자
# *.args는 *arguments의 줄임말입니다.
# 그러니까..꼭 저 단어를 쓸 필요가 없다는 말입니다.
# *a 라고 써도 되고, *arsdkljfksdjfs 라고 적어도 된다는 말입니다.
# 이 지시어는 여러 개(복수개의)의 인자를 함수로 받고자 할 때 쓰입니다.
# 사람의 이름을 받아서 성과 이름을 분리한 후 출력을 하고 싶습니다.
# 근데 문제가 생겼습니다.
# 사용자가 '몇 개의' 이름을 적어 넣을 지 알 수 가 없는 것이죠.
# 이럴 때 *args를 인자로 받습니다.


def lastName_and_FirstName(*아무변수):
    for 아무아무변수 in 아무변수:
        print("%s %s" % (아무아무변수[0], 아무아무변수[1:3]), end=' ')
    print("\n")


lastName_and_FirstName('정하용')
lastName_and_FirstName('정하용', '염정아')
lastName_and_FirstName('정하용', '염정아', '윤세아')
lastName_and_FirstName('정하용', '염정아', '윤세아', '박소담')

# 와 대박 이해 한방에 감
# lastName_and_FirstName 함수에서는 인자를 *아무변수 를 받습니다.
# args를 출력해보면 tuple(튜플) 형태임을 알 수 있습니다.
# 여러 개의 인자로 함수를 호출할 경우, 함수 내부에서는 튜플로 받은 것처럼 인식한다는 것이죠.
# 이렇게 여러개의 인자를 받기 위해서 *args의 형태로 함수 파라미터를 작성합니다.
# 와 이해 감
# 대박 대박 감사합니다. 개미님.

# **kwargs을 알아보자
# kwargs는 keyword argument의 줄임말로 키워드를 제공합니다.


def introduceEnglishName(**아무아무아무거나):
    for 아무거나, 아무거나거나 in 아무아무아무거나.items():
        print("{0} is {1}".format(아무거나, 아무거나거나))


introduceEnglishName(MyName='Jung Hayong')
# 와 이해 한방에 간다!!! 그런데 살짝 궁금해진게, 그그 key 하고 value
# 를 적잖아요 그게 이 함수, 파이썬이 첫번째 위치, 두번째 위치라고 기억해서 뱉어 내는거에요?
# 아니면 key, value 값이라고 명확하게 인지한 상태에서 뱉어내는 거에요?

# **kwargs는(키워드 = 특정값) 형태로 함수를 호출할 수 있습니다.
# 그것은 그대로 딕셔너리 형태로 {'키워드':특정값} 요렇게 함수 내부로 전달됩니다.
# 그렇게 전달받은 딕셔너리를 마음대로 조리하면 되겠죠?

# 여기까지 이해하고, 더 읽어내려 나가자
# 감사합니다. 이분 브런치 더 열심히 읽고
# 공부해야지

# 아하 키워드 아규먼트를 이용해서 무슨 키워드가 입력되면 이렇게 출력하고
# 또 다르게 키워드가 입력되면 저렇게 출력하는 함수를 만들 수 있겠구나
# 감사합니다

# https://brunch.co.kr/@princox/180
# https://brunch.co.kr/@princox/180
# https://brunch.co.kr/@princox/180

# 공부는 이렇게 해야겠다
# 구글에게 물어봐
# 구글은 답을 알고 있다
# 너가 못찾을 뿐
# -정하용-

# 예제5
# 중첩함수(클로저)
print()


def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 10000)


nested_func(10000)

# 데코레이터 클로저 공부해보기!!!
# 지금은 감만 오네~
# 오늘 공부 끝!!

# 예제6(hint)


def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(500))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))


def lambda_mul_10(num): return num * 10


print('>>>', lambda_mul_10(10))
# 람다식: 람다함수를 사용함으로써 가독성, 코드를 간결하게
# 많은 메모리가 절약되는 것은 아니지만 메모리 절약됨
# 데이터 전처리라든지 데이터 베이스에서 게시판 데이터들을 대량으로 가져와서
# 날짜를 바꿔준다던지, 내용을 수정한다던지, 형태소 분석을 한다던지,
# 문자열과 문자열을 연결해서 새로운 문자열을 만든다던지 그럴때 좋다


def func_final(x, y, func):
    print(x*y*func(10))


func_final(10, 10, lambda_mul_10)
# 람다함수를 넣을 수도 있다

print(func_final(10, 10, lambda x: x * 1000))
# 즉시 람다식을 바로 작성해서 함수에 인자로 함수를 넘긴것을 확인할 수 있다
