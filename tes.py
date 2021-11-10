class book:
    def __init__(self,책제목,저자,역자,출판사,ISB10):
        self.책제목 = 책제목
        self.저자 = 저자
        self.역자 = 역자
        self.출판사 = 출판사
        self.ISB10 = ISB10


book1 = book("헴","저자1","역자1","출판사1","ISB10")
print(book1.책제목)