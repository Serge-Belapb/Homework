"""
Написать функцию printn() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 

"""
n = 1


def printn(text):
    global n
    for i in text:
        print(n, text)
        n += 1
    return   


print(printn(input("  :")))