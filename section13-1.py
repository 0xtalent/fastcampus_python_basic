# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본완성

import random
import time

words = []                                   # 영어 단어 리스트(1000개 로드)

n = 1                                        # 게임 시도 횟수
cor_cnt = 0                                  # 정답 개수
# 전역변수 선언
with open('./resource/word.txt', 'r') as f:  # 문제 txt 파일 로드/as alias를 달아주고
    for c in f:
        words.append(c.strip())
# 리스트기 때문에 어펜드 시켜주면 되겠죠/양쪽 공백 제거 strip 함수
# print(words)                                 # 단어 리스트 확인

input("준비됐니? 아무키나 눌러봐!")            # Enter Game Start!

start = time.time()                          # Start Time
# 타임에 타임함수를 가져와서 시작시간을 기록하기
while n <= 5:                                # 5회 반복
    random.shuffle(words)                    # List shuffle!
    q = random.choice(words)                 # List -> words random extract!
# 섞은 다음에 랜덤으로 하나 뽑아옴
    print()

    print("*Question # {}".format(n))
    print(q)                                 # 문제 출력
# 파이썬 포맷팅에는 두가지 방법이 있습니다.
# %와 format 함수를 이용하는 것
# % 포맷팅은 % 연산자와 포맷스트링을 사용하는 방법
# 대표적인 포맷 스트링으로는 %d, %s, %f가 있습니다.
# format 포맷팅은 {} 괄호를 이용한 포맷팅 방법입니다.
# 변수의 타입과 상관없이 괄호와 숫자만 이용하면 됩니다.
    x = input()                              # 타이핑 입력
# 위 단어랑 똑같은 글자를 치는지 확인하기 위해 인풋함수로 입력 받기
    print()

    if str(q).strip() == str(x).strip():     # 입력 확인(공백제거)
        print("오우 게임좀 할줄 아는 분인가!")
        cor_cnt += 1                         # 정답 개수 카운트
# 공백을 제거한 값이 키보드로 입력한 값과 같으면 통과/정답을 1 늘려줌
    else:
        print("뭐야 이걸 왜 틀려!")

    n += 1                                   # 다음 문제 전환

end = time.time()                            # End Time
# 타임에서 타임함수를 호출해서 end time을 기록
et = end - start                             # 총 게임 시간
# 총시간은 끝 시간에서 시작시간을 빼주면 됩니다.
et = format(et, ".3f")                       # 소수 셋째 자리 출력(시간)
# 총시간을 포맷함수를 이용해서 소수 자리를 지정 셋째자리까지 float 형태로 나오도록
if cor_cnt >= 3:                             # 3개 이상 합격
    print("당신은 우리와 함께 갈 수 있습니다.")
else:
    print("당신은 우리와 함께하지 못하게 되었습니다. ")

# 수행 시간 출력
print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass
# 이건 뭔지 잘 모르겠다
# 찾아보니...__main__ 은 최상위 코드가 실행되는 스코프의 이름입니다.
# 모듈의 __name__ 은 표준 입력, 스크립트 또는 대화식 프롬프트에서 읽힐 때 __main__으로 설정됩니다.
# 모듈은 자신의 __name__을 검사하여 메인 스코프에서 실행 중인지를 확인할 수 있습니다.
# 이 때문에 임포트될 때는 실행되지 않지만, 스크립트로 실행되거나 python-m 으로 실행될 때 조건부로 동작하는 공통 관용구를 사용할 수 있습니다.
# 뭔 말이여
# https://medium.com/@chullino/if-name-main-은-왜-필요할까-bc48cba7f720
# 해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령입니다.
# https://battlewithmyself.tistory.com/49
# 요약하자면 해당 모듈이 직접 실행되는 경우에는 __name__ 은 __main__ 으로 설정되어 if문 아래를 실행하지만, 외부에서 실행된 경우에는 __name__ 이 __main__이 아니기 때문에 if문 아래를 실행하지 않는다.
# 뭔 말인지는 알겠는데 왜 하는지는 모르겠음
