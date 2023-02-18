def task1() :
    num = int(input('Введите 3-х значное число : '))
    if num < 100 or num > 999 :
        print('Число должно быть 3-х значным')
        return
    sum = 0
    for i in range(0, 3, 1) :
        temp = num % 10
        num //= 10
        sum += temp
    print(sum)

def task2() :
    ## x - pet x - serg 4x - k найти чему равен х  6x = s x = s/6
    S = int(input('Введите число журавликов : '))
    if S % 6 != 0 :
        print("Число журавликов должно быть кратно 6 (иначе получаются знаменитые полтора землекопа")
        return
    x = S // 6
    Petya = x
    Seryozha = x
    Katya = 4 * x

    print(f"Серёжа сделал - {Seryozha} \n Петя сделал -  {Petya} \n Катя сделала -  {Katya}" )

#task1()
task2()