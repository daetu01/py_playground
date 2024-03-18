from PyPDF2 import PdfReader
from konlpy.tag import Okt
from collections import Counter


filepath = input("패스를 입력하세요")

def parsetodata (filepath) :
    reader = PdfReader(filepath)
    pages = reader.pages
    text = ""
    for page in pages:
        sub = page.extract_text()
        text += sub
# 데이터 정제
    okt = Okt() 
    noun = okt.nouns(text)
    counter =  Counter(noun)
    top_100_noun_list = counter.most_common(100)
    for i in top_100_noun_list :
        print(i)
    return text

print(filepath)
print()

# 한글에서 데이터를 단어 단으로 정제시켜서 넘겨줄 필요가 있음 . 
# 여기서 이 작업을 해야