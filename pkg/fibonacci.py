class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    @staticmethod
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    @staticmethod
    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result


# 아왜 @classmethod 써야지 오류메시지 없어지는 거지
# 썼는데 호출하니까 호출하는 쪽에서 에러남
# 아 이거가지고 30분 넘게 고민하고 있네
# 아 모르겠다
# 그냥 problem 뜬 채로 쓸래 실행은 되잖아
# 아 찾음 @staticmethod 이거 쓰면 된다는데 해봐야지
# https://hashcode.co.kr/questions/1051/클래스-메소드에-self를-적고-안적고는-무슨-차이인가요
# 된다. 아오 거의 40-50분 고민했네ㅋㅋㅋ구글 검색하면서
# 답은 참 쉽다... 잘 이해는 안감...ㅎㅎㅎ...
# 공부 열심히 합시다~~~
