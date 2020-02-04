# 2050. 알파벳을 숫자로 변환


for c in input():
    print( ord(c)-64, end=' ' )


# ord(text) : text의 첫 문자를 아스키코드로 변환해주는 함수
# ord('A') = 65