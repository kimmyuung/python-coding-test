S, tmp = input(), ""

ck = False
ans = ""

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + " "
            print(tmp[::-1], end=" ")
            # 현재 보고 있는 단어 역순으로 마지막을 공백으로 출력
            tmp = ""
        else:
            print(" ", end="")   
            ans += " "         
    elif i == '<':
        ck = True
        ans += tmp[::-1] + "<"
        print(tmp[::-1] +"<" , end=" ")
        tmp = ""
    elif i == '>':
        ck = False
        ans += ">"
        print(">", end="")
    else: # 알파벳과 숫자
        if ck:
            ans += i
            print(i, end="")
        else:
            tmp += i # 숫자와 문자열 저장

ans += tmp[::-1]
print(tmp[::-1])