"""
Написать функцию printn() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 

"""
n = 0


def printn(text):
    global n
    n += 1
    for i in text:
        print(n, text)
        printn(text)
    return   


print(printn(input("  :")))