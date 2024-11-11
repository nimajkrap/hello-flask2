import nvapi

keyword = input("맛집검색: ") # 입력창에 입력 받기
nvapi.blog(keyword)


# 밑에는 연습
def hello(msg):
    #print(f"나는 귀염둥이 {msg}")
    #return "출력" # 결과 값(있어도 그만 없어도 그만)
    return f"둘이 먹다 한명이 죽어도 모를 {msg}"

    #keyword = input("맛집 검색: ") # 입력창에 입력 받가
    # 입력 받은 값은 keyword에 저장
    # 입력 받은 데이터를 hello 함수에 입력값으로 넣기

    #result = hello("keyword") # 위 함수에서 전달된 값을 result에 전달
    #print(result) # 전달된 값을 화면에 출력