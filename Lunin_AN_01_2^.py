'''
#задание 1 Написать программу, которая будет делить введенные пользователем два вещественных числа
#и выводить результат на экран, сообщая об ошибке в случае деления на ноль.
a=float(input('введите делимое '))
b=float(input('введите делитель '))
if b!=0:
    print(a/b)
else:
    print('error: нельзя делить на 0!')
'''
'''
#задание 2 Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю,
# если сумма покупки превышает 20 у.е. Сумму покупки ввести с клавиатуры, а результаты округлить до сотых
# (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.
a=float(input('введите сумму покупки '))
if a>20:
    print('скидка: ',round(a*0.35,2))
    print('итоговая сумма: ',round(a*0.65,2))
else:
    print('скидка 0')
    print('итоговая сумма: ',round(a,2))
'''
'''
#задание 3 Напишите скрипт, который по введенному пользователем числу от 1 до 12,
#будет выводить на экран сообщение в виде названия месяца и времени года.
#Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
months=["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
number=int(input("введите номер месяца "))
if number>=1 and number<=12:
    m_name=months[number-1]
    print(m_name)
    if 1<=number<=2 or number==12:
        print('зима')
    elif 3<=number<=5:
        print('весна')
    elif 6<=number<=8:
        print('лето')
    elif 9<=number<=11:
        print("осень")
'''