def task1(num) :
    if num < 100 or num > 999 :
        print('Число должно быть 3-х значным')
        return
    sum = 0
    for i in range(0, 3, 1) :
        temp = num % 10
        num //= 10
        sum += temp
    print(sum)





num = int(input('Введите 3-х значное число : '))
task1(num)