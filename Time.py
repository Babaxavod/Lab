print('Введите ДВА числа через ОДИН пробел в ОДНУ строчку, первое число - часы, от 0 до 23 включительно. второе - минуты, от 0 до 59 включительно')
#вывод правил ввода
while 1:
    vvod = list(map(str,input().split()))
    if len(vvod)!= 2:
        print('введите ДВА элемента')
    else:
        if vvod[0].isdigit() and vvod[1].isdigit():
            if int(vvod[0])>=0 and int(vvod[0])<24 and int(vvod[1])>=0 and int(vvod[1])<60:
                #print('ввод принят')
                hour = int(vvod[0])
                min = int(vvod[1])
                break
            else:
                print('введите числа в заданном диапазоне')               
        else:
            print('ввдедите целые числа')
#ввод и проверка его на правильность

            
def hour_ending(a):
    ending = ''
    if (a>=5 and a<=20) or a == 0:
        ending = 'ов'
    if (a>= 2 and a<=4) or (a>= 22 and a<=23):
        ending = 'а'
    return ending
#функция для определения окончаний часов


def minut_ending(a):
    ending = ''
    if a%10 == 1 and a !=11:
        ending = 'а'
    if a%10 >= 2 and  a%10 <= 4 and (a>20 or a<10):
        ending = 'ы'
    return ending
#функция для определения окончаний минут


if hour>=0 and hour<6:
    time = 'ночи'
if hour>=6 and hour<12:
    time = 'утра'
if hour>=12 and hour<18:
    time = 'дня'
if hour>=18 and hour<24:
    time = 'вечера'
#опреденеие времени суток

    
if hour == 0 and min == 0:
    print('полночь')
elif hour == 12 and min == 0:
    print('полдень')
else:
    if min == 0:
        print(hour, ' час',hour_ending(hour), ' ', time, ' ровно', sep = '')
    else:
        print(hour, ' час',hour_ending(hour), ' ', min, ' минут' , minut_ending(min),  ' ', time, sep = '')     
#вывод информации
